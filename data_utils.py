# data_utils.py
import pandas as pd
import streamlit as st

DATA_PATH = "data/iris.csv"

@st.cache_data
def load_iris():
    """Load the Iris dataset from local file, cached by Streamlit."""
    return pd.read_csv(DATA_PATH)
