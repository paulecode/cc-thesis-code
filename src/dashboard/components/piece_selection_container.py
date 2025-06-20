import streamlit as st

from components.midi_piece_section import midi_section
from components.wav_piece_section_container import wav_section_container

from .piece_selection import select_piece_list

def select_piece(df, id):
    st.write(f"Selection {id}")
    segments = True
    chart_selection = None
    chart_selection_options = ['None', 'RMS', 'Waveform', 'Spectrogram', 'Mel-Spectrogram', 'MFCC', 'STFT', 'FFT']
    normalize = True
    scrollable = True

    selection = select_piece_list(df, key=f"dfs{id}")
    if selection and 'selection' in selection and 'rows' in selection['selection'] and selection['selection']['rows']:
        index = selection['selection']['rows'][0]
        row = df.iloc[index]
        st.markdown(f"You selected: _{row['canonical_title']}_")
        st.sidebar.write(row)

        with st.expander("Config display", expanded=True):
            midi_or_wav = st.radio("View piece in", ["MIDI", "WAV"], captions=["Symbolic data", "Audio data"], horizontal=True, key=f"mow{id}")
            if midi_or_wav == "WAV":
                segments_yes_or_no = st.radio("Split piece into 10 second clips?", ["Yes", "No"], horizontal=True, key=f"syon{id}")
                if segments_yes_or_no == "Yes":
                    segments = True
                else:
                    segments = False
                chart_selection = st.selectbox("Which chart to display", options=chart_selection_options, key=f"cs{id}")
                normalize_yes_or_no = st.radio("Normalize", ["Yes", "No"], horizontal=True, key=f"na{id}")
                if normalize_yes_or_no == "Yes":
                    normalize = True
                else:
                    normalize = False
                scrollable_container = st.radio("Scrollable container", ["Yes", "No"], horizontal=True, key=f"sc{id}")
                if scrollable_container == "Yes":
                    scrollable = True
                else:
                    scrollable = False

        if midi_or_wav == "MIDI":
            midi_section(row)

        if midi_or_wav == "WAV":
            wav_section_container(row, normalize, segments, chart_selection, scrollable, id)
