import re

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
