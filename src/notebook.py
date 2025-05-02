# %% Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.formats.style import Subset
import seaborn as sns
import os
import unicodedata
import re
import uuid

# %%
os.makedirs('../plots', exist_ok=True)
os.makedirs('../data/processed', exist_ok=True)

# %%
sns.set_theme()

# %%
# No regex
# Missing key
# Missing Musical form

no_regex = re.compile(r'\s?\bno\s?(\d+)')
opus_regex = re.compile(r'\s?\bop(?:us)?\s?(\d+)')
s_regex = re.compile(r'\s?\bs\s?(\d+)')
d_regex = re.compile(r'\s?\bd\s?(\d+)')
bwv_regex = re.compile(r'\s?\bbwv\s?(\d+)')
quoted_regex = re.compile(r'"([^"]*)"(?!.*")')
key_regex = re.compile(r'\s?\b(?:in\s+)?([a-g]\s+(?:(?:flat|sharp)(?:\s+(?:minor|major))?|minor|major))\b')

regex_dict = {
    no_regex: 'no_number',
    opus_regex: 'opus_number',
    s_regex: 's_number',
    d_regex: 'd_number',
    quoted_regex: 'quoted_title',
    key_regex: 'key',
    bwv_regex: 'bwv'
}

# %%
def manual_adjustments(title):
    title = re.sub(r'\bmoll\b', 'minor', title)
    title = re.sub(r'\bmin\b', 'minor', title)
    title = re.sub(r'\bbb\b', 'b flat', title, flags=re.IGNORECASE)
    title = re.sub(r'\b\d*\/\d+\b', lambda x: x.group(0).replace('/', ' no '), title)
    title = re.sub(r'\bin 3\b', 'in e', title)
    title = re.sub(r'\besp\b', 'espagnole', title, flags=re.IGNORECASE)
    title = re.sub(r'\bspanish\b', 'espagnole', title, flags=re.IGNORECASE)
    # title = re.sub(r'\b\(?complete\)?\b', '', title, flags=re.IGNORECASE)

    return title

# %%
def standardize_canonical_title(title):

    title = title.strip()
    title = title.lower()

    title = title.replace('“', '"')
    title = title.replace('”', '"')
    title = title.replace('\'', '"')

    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('utf-8')

    title = title.replace("-", " ")

    title = re.sub(r'[^\w\s/"]', '', title)

    title = " ".join(title.split())

    title = manual_adjustments(title)

    return title

# %%
def extract_music_form(row: pd.Series) -> pd.Series:
    music_form_dict = {
        'ballade': 'ballade',
        'sonata': 'sonata',
        'son': 'sonata',
        'etude': 'etude',
        'etudes': 'etude',
        'rhapsody': 'rhapsody',
        'rhapsodie': 'rhapsody',
        'waltz': 'waltz',
        'valse': 'waltz',
        'impromptu': 'impromptu',
        'impromptus': 'impromptu',
        'nocturne': 'nocturne',
        'prelude': 'prelude',
        'preludes': 'prelude',
        'scherzo': 'scherzo',
        'mazurka': 'mazurka',
        'fantasie': 'fantasie',
        'fantasia': 'fantasie',
        'fantasy': 'fantasie',
    }

    new_row = row.copy()
    new_row['music_form'] = 'other/unclassified'

    title = row['standardized_title']

    for key in music_form_dict:
        # if key in title:
        if re.search(fr'\b{key}\b', title, re.IGNORECASE):
            new_row['music_form'] = music_form_dict[key]
            new_title = re.sub(fr'\s?\b{key}\b', '', title, flags=re.IGNORECASE).strip()
            new_row['standardized_title'] = new_title
            return new_row

    return new_row

# %%
def extract_quoted_title(row: pd.Series) -> pd.Series:
    title = row['standardized_title']

    quote_regex = re.compile(r'"([^"]*)"')

    match = quote_regex.search(title)

    if match:
        new_row = row.copy()
        new_row['quoted_title'] = match.group(1)
        new_row['standardized_title'] = quote_regex.sub('', title).strip()
        return new_row

    return row

# %%
def extract_key(row: pd.Series) -> pd.Series:
    title = row['standardized_title']

    key_regex = re.compile(
        r'\b(?:in\s+)?([CDEFGAB](?:[-\s]*(?:#|b|flat|sharp))?(?:\s+(?:major|maj|minor|min))?)\b',
        re.IGNORECASE
    )

    match = key_regex.search(title)
    if match:
        new_row = row.copy()
        new_row['key'] = match.group(1).strip()
        new_row['standardized_title'] = key_regex.sub('', title).strip()
        return new_row

    return row

# %%
def regex_extract(row, regex, new_column_name):
    title = row['standardized_title']

    match = regex.search(title)
    if match:
        new_row = row.copy()
        new_row[new_column_name] = match.group(1).strip()
        new_row['standardized_title'] = regex.sub('', title).strip()
        return new_row

    return row

# %%
def manual_row_adjustments(row: pd.Series) -> pd.Series:
    if row['standardized_title'] == "transcendental":
        row['s_number'] = '139'

    if row['standardized_title'] == 'mephisto':
        row['s_number'] = '514'
        row['no_number'] = '1'

    if row['standardized_title'] == 'dante':
        row['s_number'] = '161'
        row['no_number'] = '7'

    if row['standardized_title'] == 'espagnole':
        row['s_number'] = '254'
        # row['no_number'] = 1

    if row['standardized_title'] == 'hungarian':
        row['s_number'] = '244'

    # row['audio_filename'] = row['audio_filename'].split('/', 1)[-1]
    return row

# %%
def group_identicals_pass_one(group: pd.DataFrame):
    composer = group.name
    if composer == "Bach":
        group['identifieable'] = group.groupby('bwv', dropna=True)['bwv'].transform(lambda x: str(uuid.uuid4()))
        group = group.dropna(subset='identifieable')

    if composer == "Beethoven":
        group = group.dropna(subset=['opus_number', 'no_number'], how='all')
        group['identifieable'] = group.groupby(['opus_number', 'no_number'], dropna=False)['opus_number'].transform(lambda x: str(uuid.uuid4()))

    if composer == "Chopin":
        group = group.dropna(subset=['opus_number', 'no_number'], how='any')
        group['identifieable'] = group.groupby(['opus_number', 'no_number'], dropna=True)['opus_number'].transform(lambda x: str(uuid.uuid4()))

    if composer == "Liszt":
        group['identifieable'] = group.groupby(['s_number', 'no_number'], dropna=True)['s_number'].transform(lambda x: str(uuid.uuid4()))

        no_id = group[group['identifieable'].isna()]
        yes_id = group[group['identifieable'].notna()]

        for index, row in no_id.iterrows():
            for id_index, id_row in yes_id.iterrows():
                if row['quoted_title'] == id_row['quoted_title']:
                    group.at[index, 'identifieable'] = id_row['identifieable']
                    break

        group = group.dropna(subset='s_number')

        no_id_mask = group['identifieable'].isna()

        group.loc[no_id_mask, 'identifieable'] = group[no_id_mask].groupby(['s_number', 'standardized_title'], dropna=True)['s_number'].transform(lambda x: str(uuid.uuid4()))

    if composer == "Schubert":
        group['identifieable'] = group.groupby(['opus_number', 'no_number'], dropna=True)['d_number'].transform(lambda x: str(uuid.uuid4()))

        group = group.dropna(subset='identifieable')
        # group['identifieable'] = group.groupby(['opus_number', 'no_number','d_number'], dropna=True)['d_number'].transform(lambda x: str(uuid.uuid4()))
        # no_id_mask = group['identifieable'].isna()

        # group.loc[no_id_mask, 'identifieable'] = group[no_id_mask].groupby('d_number', dropna=True)['d_number'].transform(lambda x: str(uuid.uuid4()))

    return group

# %%

# %%
# metadata = pd.read_csv('../data/maestro-v3.0.0/maestro-v3.0.0.csv')
metadata = pd.read_csv('data/maestro-v3.0.0/maestro-v3.0.0.csv')

# %%
metadata_filtered = metadata[metadata['canonical_composer'].isin(['Frédéric Chopin', 'Franz Schubert', 'Ludwig van Beethoven', 'Johann Sebastian Bach', 'Franz Liszt'])].copy()

composer_mapping = {
'Frédéric Chopin': 'Chopin',
'Ludwig van Beethoven': 'Beethoven',
'Johann Sebastian Bach': 'Bach',
'Franz Schubert': 'Schubert',
'Franz Liszt': 'Liszt'
}

standardized_titles = metadata_filtered['canonical_title'].apply(standardize_canonical_title)

insert_loc = metadata_filtered.columns.get_loc('canonical_title') + 1

metadata_filtered.insert(insert_loc, 'standardized_title', standardized_titles)

metadata_filtered = metadata_filtered.apply(extract_music_form, axis=1)

for regex, column_name in regex_dict.items():
    metadata_filtered = metadata_filtered.apply(regex_extract, axis=1, args=(regex, column_name))

metadata_filtered.loc[:, 'canonical_composer'] = metadata_filtered['canonical_composer'].replace(composer_mapping)

metadata_filtered = metadata_filtered.apply(manual_row_adjustments, axis=1)

metadata_filtered = metadata_filtered[~metadata_filtered['standardized_title'].str.contains(r'\b\(?complete\)?', case=False)]

metadata_filtered = metadata_filtered.groupby(['canonical_composer']).apply(group_identicals_pass_one).reset_index(drop=True)

# metadata_filtered.dropna(subset=['bwv'], inplace=True)
# %%
# metadata_filtered = metadata_filtered[metadata_filtered['canonical_composer'] == "Schubert"]
# metadata_filtered = metadata_filtered[metadata_filtered['canonical_composer'].isin(['Bach', 'Beethoven', 'Chopin', 'Liszt'])].copy()


# %%

metadata_filtered = metadata_filtered.drop_duplicates(subset=['identifieable'])
metadata_filtered.to_csv('data/processed/maestro-v3.0.0_filtered.csv', index=False)


controlframe = metadata_filtered.copy().drop(['audio_filename', 'midi_filename', 'split', 'year'], axis=1).to_csv('../data/processed/controlframe.csv', index=False)
# metadata_filtered[[ 'canonical_composer', 'canonical_title', 'standardized_title', 'duration', 'music_form', 'opus_number', 'd_number', 'no_number', 'quoted_title' ]].to_clipboard(index=False)
# metadata_filtered[[ 'canonical_composer', 'canonical_title', 'standardized_title', 'duration' ]].to_csv('../data/processed/maestro-v3.0.0_filtered_titles.csv', index=False)
metadata_filtered.to_csv('../data/processed/preselection.csv', index=False)
metadata_filtered.drop(['bwv', 'midi_filename', 'audio_filename'], axis=1).sort_values(['identifieable', 'canonical_title']).to_csv('numbers.csv', index=False, decimal=',')
metadata_filtered.sort_values(['canonical_composer' ,'identifieable', 'canonical_title']).to_csv('st.csv', index=False)

# %%
metadata_filtered['canonical_composer'].value_counts().sort_values(ascending=False).reset_index()
print(metadata_filtered.groupby('canonical_composer')['identifieable'].nunique())
print(metadata_filtered.groupby('canonical_composer')['duration'].sum())

# Ensure only one row per unique 'identifieable'
# metadata_filtered = metadata_filtered.drop_duplicates(subset=['identifieable'])
os.system('open preselection.csv')
