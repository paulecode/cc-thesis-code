import streamlit as st
import librosa

from components.wav_chart_container import draw_chart

def wav_section_element(row, normalize, chart_selection, segment_index=None):
    if segment_index is not None:
        segment_index += 1
        y, sr = librosa.load(f"data/wav_processed/{row['audio_filename'][:-4]}/segment_{segment_index}.wav")

        st.write(f"{row['canonical_title']} - Section {segment_index}")
        st.audio(f"data/wav_processed/{row['audio_filename'][:-4]}/segment_{segment_index}.wav")
        draw_chart(y, sr, normalize, chart_selection)
    else:
        y, sr = librosa.load(f"data/maestro-v3.0.0/{row['audio_filename']}")

        st.audio(f"data/maestro-v3.0.0/{row['audio_filename']}")
        draw_chart(y, sr, normalize, chart_selection)
    st.divider()
