import librosa
import librosa.display
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_mel_spectrogram(y, sr):
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

    S_dB = librosa.power_to_db(S, ref=np.max)

    fig, ax = plt.subplots(figsize=(14, 5))
    img = librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', fmax=8000, ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    ax.set(title='Mel-Spectrogram')

    st.pyplot(fig)
