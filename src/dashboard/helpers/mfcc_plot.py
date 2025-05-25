import librosa
import librosa.display
import streamlit as st
import matplotlib.pyplot as plt

def draw_mfcc(y, sr):
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

    fig, ax = plt.subplots(figsize=(14, 5))
    img = librosa.display.specshow(mfccs, x_axis='time', sr=sr, ax=ax)
    fig.colorbar(img, ax=ax)
    ax.set(title='MFCC')

    st.pyplot(fig)
