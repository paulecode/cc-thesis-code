import re
import unicodedata
from src.notebook import manual_adjustments

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
