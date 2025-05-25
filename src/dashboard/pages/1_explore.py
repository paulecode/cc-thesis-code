import streamlit as st
import pandas as pd
from components.df_summary import composer_summary
from components.general_comparisons import general_comparison_section

st.set_page_config(page_title="Exploration", page_icon="🌍")
st.header("Exploration")

st.sidebar.header("Exploration")

df = pd.read_csv("data/processed/maestro-v3.0.0_filtered.csv")
