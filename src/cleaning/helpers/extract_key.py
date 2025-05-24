import re

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
