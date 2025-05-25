import streamlit as st

def select_piece_list(df, **kwargs):
    columns=['canonical_composer', 'canonical_title', 'music_form']

    with st.expander("Select a piece"):
        selection = st.dataframe(
            df,
            column_order=columns,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row",
            key=kwargs.get('key', 'default_key')
        )

    return selection
