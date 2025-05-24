import pandas as pd

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

    return group
