import streamlit as st
import plotly.express as px
from data_utils import load_iris


df=load_iris()

num_cols = df.select_dtypes(include='number').columns.tolist()
obj_cols = df.select_dtypes(include='object').columns.tolist()


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

if 'Box Plots' in eda_type:
    st.subheader('Box Plots - Visualizing Numerical Distributions')
    b_selected_col = st.selectbox('Select a numerical column for the box plot:', num_cols)
    if b_selected_col:
        chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
        st.plotly_chart(px.box(df, x='species', y=b_selected_col, title=chart_title, color='species'))

if 'Scatter Plots' in eda_type:
    st.subheader('Scatterplots - Visualizing Relationships')
    selected_col_x = st.selectbox('Select x-axis variable:', num_cols)
    selected_col_y = st.selectbox('Select y-axis variable:', num_cols)
    if selected_col_x and selected_col_y:
        chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
        st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, color='species', title=chart_title))

if 'Count Plots' in eda_type:
    st.subheader('Count Plots - Visualizing Categorical Distributions')
    selected_col = st.selectbox('Select a categorical variable:', obj_cols)
    if selected_col:
        chart_title = f'Distribution of {selected_col.title()}'
        st.plotly_chart(px.histogram(df, x=selected_col, color='species', title=chart_title))