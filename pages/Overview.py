import streamlit as st
import pandas as pd
from data_utils import load_iris


st.title('Overview')
#load dataset


df=load_iris()
# Data Overview

st.title("🔢 Data Overview")

st.subheader("About the Data")
st.write("""
        The Iris dataset is one of the most famous datasets in the literature of machine learning and data analysis.
        It contains 150 samples of iris flowers from three different species (Iris-setosa, Iris-versicolor, Iris-virginica).
        For each flower, the dataset includes the length and width of the sepals and petals.
    """)

url = 'https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png'
st.image(url, caption="Iris Dataset")

    # Dataset Display
st.subheader("Quick Glance at the Data")
if st.checkbox("Show DataFrame"):
        st.dataframe(df)

    # Shape of Dataset
if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
#navigation sidebar
#page = st.sidebar.selectbox('Select a Page', ['Home', 'Data Dashboard', 'About'])
