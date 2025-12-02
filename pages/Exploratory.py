import streamlit as st
import pandas as pd
import plotly.express as px
from data_utils import load_iris


df=load_iris()
num_cols = df.select_dtypes(include='number').columns.tolist()

st.title('Exploratory Data Analysis')
st.subheader('Select the type of Visualization to Explore')
eda_type= st.multiselect('Visualization Options', ['Histograms', 'Box Plots', 'Scatter Plots', 'Count Plots'])

if 'Histograms' in eda_type:
    st.subheader('Histograms - Visualizing Numerical Distributions')
    h_selected_col = st.selectbox('Select a numerical column for the histogram', num_cols)
    if h_selected_col:
        chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
        if st.checkbox('Show by Species'):
            st.plotly_chart(px.histogram(df, x=h_selected_col, color='species', title=chart_title, barmode='overlay'))
        else:
            st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))

# if 'Box Plots' in eda_type:
#     st.subheader('Box Plots - Visualizing Numerical Distributions')
#     b_selected_col = st.selectbox('Select a numerical column for the box plot:', num_cols)
#     if b_selected_col:
#         chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
#         st.plotly_chart(px.box(df, x='species', y=b_selected_col, title=chart_title, color='species'))