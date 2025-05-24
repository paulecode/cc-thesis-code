def regex_extract(row, regex, new_column_name):
    title = row['standardized_title']

    match = regex.search(title)
    if match:
        new_row = row.copy()
        new_row[new_column_name] = match.group(1).strip()
        new_row['standardized_title'] = regex.sub('', title).strip()
        return new_row

    return row
