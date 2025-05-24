import pandas as pd

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

    return row
