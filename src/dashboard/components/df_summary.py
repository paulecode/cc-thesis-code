import streamlit as st

def composer_summary(df):
    st.subheader("Composer distribution")

    st.dataframe(
        df.groupby('canonical_composer')
        .agg(count=('canonical_composer', 'count'), duration=('duration', 'sum'))
        .reset_index()
        .rename(columns={'canonical_composer': 'Composer', 'count': 'Number of pieces', 'duration': 'Total duration'}),
        hide_index=True
    )

    st.subheader("Music form distribution")

    st.dataframe(
        df.groupby('music_form')
        .agg(count=('music_form', 'count'), duration=('duration', 'sum'))
        .reset_index()
        .rename(columns={'music_form': 'Music form', 'count': 'Number of pieces', 'duration': 'Total duration'}),
        hide_index=True
    )

    st.divider()
