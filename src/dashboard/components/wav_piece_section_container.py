import streamlit as st
import os

from components.wav_section import wav_section_element

def wav_section_container(row, normalize, segments, chart_selection, scrollable, id):
    if segments:
        number_of_sections = len(os.listdir(f"data/wav_processed/{row['audio_filename'][:-4]}/"))
        st.write(f"Piece chopped into {number_of_sections} sections")
        if scrollable:
            with st.container(height=1000):
                for x in range(number_of_sections):
                    wav_section_element(row, normalize, chart_selection, x)
        else:
            for x in range(number_of_sections):
                wav_section_element(row, normalize, chart_selection, x)
    else:
        wav_section_element(row, normalize, chart_selection)
