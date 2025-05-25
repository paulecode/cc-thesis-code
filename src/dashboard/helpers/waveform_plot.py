import streamlit as st
import librosa
import matplotlib.pyplot as plt

def draw_waveform(y, sr):
    fig, ax = plt.subplots(figsize=(14, 5))
    librosa.display.waveshow(y, sr=sr, ax=ax)
    ax.set(title='Waveform', xlabel='Time (s)', ylabel='Amplitude')

    st.pyplot(fig)
