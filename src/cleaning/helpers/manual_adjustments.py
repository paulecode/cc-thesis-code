import re

def manual_adjustments(title):
    title = re.sub(r'\bmoll\b', 'minor', title)
    title = re.sub(r'\bmin\b', 'minor', title)
    title = re.sub(r'\bbb\b', 'b flat', title, flags=re.IGNORECASE)
    title = re.sub(r'\b\d*\/\d+\b', lambda x: x.group(0).replace('/', ' no '), title)
    title = re.sub(r'\bin 3\b', 'in e', title)
    title = re.sub(r'\besp\b', 'espagnole', title, flags=re.IGNORECASE)
    title = re.sub(r'\bspanish\b', 'espagnole', title, flags=re.IGNORECASE)

    return title
