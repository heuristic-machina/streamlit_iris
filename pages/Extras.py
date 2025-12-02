import streamlit as st

st.title('Adding Columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('A cat')
    