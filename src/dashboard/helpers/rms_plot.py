import librosa
import matplotlib.pyplot as plt
import streamlit as st

def draw_rms(y, normalize):
    rms = librosa.feature.rms(y=y)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(rms[0], color='orange', label='RMS')
    ax.set_xlabel("Time")
    ax.set_ylabel("RMS Energy")
    ax.set_title("RMS Energy over Time")
    if normalize:
        ax.set_ylim(0,0.5)
    ax.legend()
    st.pyplot(fig)
