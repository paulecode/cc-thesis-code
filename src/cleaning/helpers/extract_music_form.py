import pandas as pd
import re

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
