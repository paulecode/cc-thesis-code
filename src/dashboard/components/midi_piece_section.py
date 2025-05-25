import pandas as pd
from helpers.create_scatterplot import create_scatter_plot
from helpers.duration import calculate_duration

def midi_section(row):
    midi_notes = pd.read_csv(f"data/midi_processed/{row['midi_filename']}_notes.csv")

    # Not needed just yet
    # midi_meta = pd.read_csv(f"data/midi_processed/{row['midi_filename']}_meta.csv")

    # TODO Put this in the preprocessor
    midi_notes['duration'] = midi_notes.apply(lambda x: calculate_duration(x, midi_notes), axis=1)
    midi_notes = midi_notes[midi_notes['velocity'] != 0]

    create_scatter_plot(
        data=midi_notes,
        x_col='time',
        y_col='note',
        xlabel='Time',
        ylabel='Note',
        s=25,
    )

    # TODO Create Velocity plot
