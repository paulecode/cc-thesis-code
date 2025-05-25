import streamlit as st

st.set_page_config(page_title='Dashboard', page_icon='📊', layout='wide')

st.header('Dashboard')

explore_1_page = st.Page('1_explore_i.py', title='Exploration I')
explore_2_page = st.Page('2_explore_ii.py', title='Exploration II')


pg = st.navigation([explore_1_page, explore_2_page])

pg.run()
