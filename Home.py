import streamlit as st

#set page title and icon
st.set_page_config(page_title='Iris Dataset Explorer', page_icon='🌸')


st.title('Iris Dataset Explorer')
st.subheader('Welcome the the Iris dataset explorer app')
st.write("""
    This app provides an interactive platform to explore the famous Iris dataset.
         You can visualize the distribution of data, explore relationships between features, and even make predictions on new data!
""")
st.image('imgs/iris.jpg', caption="The Iris Flower")



