import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_fft(y, sr):
    fft_result = np.fft.fft(y)
    fft_magnitude = np.abs(fft_result)
    frequencies = np.fft.fftfreq(len(fft_result), 1/sr)

    positive_freqs = frequencies[:len(frequencies)//2]
    positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]

    positive_freqs = positive_freqs[1:]
    positive_magnitude = positive_magnitude[1:]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(positive_freqs, positive_magnitude)
    ax.set_title('Fourier Transform (Frequency Spectrum)')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Magnitude')
    ax.set_xscale('log')
    ax.set_xlim([20, sr//2])
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
