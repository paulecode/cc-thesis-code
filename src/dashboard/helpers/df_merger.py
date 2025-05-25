import pandas as pd

def merger(df):
    note_csv_files = [f"data/midi_processed/{midi_file}_notes.csv" for midi_file in df['midi_filename']]

    note_data = []

    for file in note_csv_files:
        note_df = pd.read_csv(file)

        total_note_count = len(note_df)
        average_velocity = note_df['velocity'].mean()

        midi_file = file.split('/')[-2:]
        midi_file = '/'.join(midi_file).replace('_notes.csv', '')

        note_data.append({'midi_filename': midi_file, 'total_note_count': total_note_count, 'average_velocity': average_velocity })

    note_data_df = pd.DataFrame(note_data)

    return pd.merge(note_data_df, df, on='midi_filename', how='inner')
