import pandas as pd
import streamlit as st
from components.piece_selection_container import select_piece

st.header("Exploration")

st.sidebar.header("Exploration II")

st.sidebar.success("Granular exploration and comparison of individual pieces")

df = pd.read_csv("data/processed/maestro-v3.0.0_filtered.csv")


col1, col2 = st.columns([1,1])

with col1:
    select_piece(df, 1)

with col2:
    select_piece(df, 2)
