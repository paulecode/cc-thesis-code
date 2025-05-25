import librosa
import librosa.display
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_spectrogram(y, sr):
    D = np.abs(librosa.stft(y))

    DB = librosa.amplitude_to_db(D, ref=np.max)

    fig, ax = plt.subplots(figsize=(14, 5))
    img = librosa.display.specshow(DB, sr=sr, x_axis='time', y_axis='log', ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    ax.set(title='Spectrogram')

    st.pyplot(fig)
