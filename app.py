import streamlit as st

with open('readme.md', 'r') as f_read:
    readme = f_read.read()
    f_read.close()

st.markdown(readme, unsafe_allow_html=True)