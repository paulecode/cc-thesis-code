import streamlit as st
from helpers.create_scatterplot import create_scatter_plot
from helpers.df_merger import merger

def general_comparison_section(df):
    df = merger(df)

    #====================#
    # Music form section #
    #====================#

    st.header("Comparing music forms")

    music_forms = df['music_form'].unique()
    selected_music_forms = st.multiselect(
        "Select Music Forms to Include:",
        options=music_forms,
        default=[],
    )

    filtered_df = df[df['music_form'].isin(selected_music_forms)]

    axis_options = ['Note count', 'Average velocity', 'Duration']

    axis_dict = {
    'Note count': 'total_note_count',
    'Average velocity': 'average_velocity',
    'Duration': 'duration',
    }

    x_axis_music_form = st.selectbox('Select data for the x-axis', options=axis_options, key='xmf')
    y_axis_music_form = st.selectbox('Select data for the y-axis', options=axis_options, key='ymf')

    if selected_music_forms and x_axis_music_form and y_axis_music_form:
        create_scatter_plot(
        data=filtered_df,
        x_col=axis_dict[x_axis_music_form],
        y_col=axis_dict[y_axis_music_form],
        hue='music_form',
        xlabel=x_axis_music_form,
        ylabel=y_axis_music_form,
        legend_title='Music Form'
        )
    else:
        st.write("Please select options")

    st.divider()

    #==================#
    # Composer section #
    #==================#

    st.header("Comparing composers")

    composers = df['canonical_composer'].unique()  # Get unique composers

    selected_composers = st.multiselect(
        "Select composers to include:",
        options=composers,
        default=[],
    )

    filtered_df = df[df['canonical_composer'].isin(selected_composers)]

    axis_options = ['Note count', 'Average velocity', 'Duration']

    axis_dict = {
    'Note count': 'total_note_count',
    'Average velocity': 'average_velocity',
    'Duration': 'duration',
    }

    x_axis_composers = st.selectbox('Select data for the x-axis', options=axis_options, key='xcc')
    y_axis_composers = st.selectbox('Select data for the y-axis', options=axis_options, key='ycc')


    if selected_music_forms and x_axis_music_form and y_axis_music_form:
        create_scatter_plot(
        data=filtered_df,
        x_col=axis_dict[x_axis_composers],
        y_col=axis_dict[y_axis_composers],
        hue='canonical_composer',
        xlabel=x_axis_composers,
        ylabel=y_axis_composers,
        legend_title='Composer'
        )
    else:
        st.write("Please select options")

    st.divider()
