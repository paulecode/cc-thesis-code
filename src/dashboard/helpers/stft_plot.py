import librosa
import librosa.display
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_stft(y, sr):
    stft_result = librosa.stft(y, n_fft=2048, hop_length=512, win_length=2048)
    stft_db = librosa.amplitude_to_db(np.abs(stft_result), ref=np.max)

    fig, ax = plt.subplots(figsize=(10, 6))
    img = librosa.display.specshow(stft_db, sr=sr, hop_length=512, x_axis='time', y_axis='log', cmap='viridis', ax=ax)
    ax.set_title('STFT Spectrogram')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (Hz)')
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    st.pyplot(fig)
