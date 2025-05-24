import pandas as pd
from src.cleaning.helpers import standardize_canonical_title
from src.cleaning.helpers import extract_music_form
from src.cleaning.helpers import regex_extract
from src.cleaning.constants import regex_dict
from src.cleaning.constants.composer_selection import composer_selection_list
from src.cleaning.constants.composer_selection import composer_mapping_dict
from src.cleaning.helpers.group_identicals import group_identicals_pass_one

metadata = pd.read_csv('data/maestro-v3.0.0/maestro-v3.0.0.csv')

# Use these composers only
df = metadata[metadata['canonical_composer'].isin(composer_selection_list)].copy()

# Standardize titles
standardized_titles = df['canonical_title'].apply(standardize_canonical_title)
insert_loc = df.columns.get_loc('canonical_title') + 1
df.insert(insert_loc, 'standardized_title', standardized_titles)

# Extract music form
df = df.apply(extract_music_form, axis=1)

# Extract Regexes
for regex, column_name in regex_dict.items():
    df = df.apply(regex_extract, axis=1, args=(regex, column_name))

# Rename composers
df.loc[:, 'canonical_composer'] = df['canonical_composer'].replace(composer_mapping_dict)

# Manual row adjustments
df = df.apply(manual_row_adjustments, axis=1)

# Remove pieces that contain 'complete' in title
df = df[~df['standardized_title'].str.contains(r'\b\(?complete\)?', case=False)]

# Group pieces
df = df.groupby(['canonical_composer']).apply(group_identicals_pass_one).reset_index(drop=True)

# Only unique pieces should remain
df = df.drop_duplicates(subset=['identifieable'])

df.to_csv('../../data/processed/maestro-v3.0.0_filtered.csv', index=False)
