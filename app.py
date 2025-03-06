import streamlit as st

page1 = st.Page("page1.py", title="Page 1", icon=":material/add_circle:")

pg = st.navigation([page1])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()