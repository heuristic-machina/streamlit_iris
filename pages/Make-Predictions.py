import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from data_utils import load_iris

df=load_iris()

st.title('🌸 Make Predictions (KNN = 9)')
st.subheader('Adjust the values below to make predictions on the Iris dataset:')

#user inputs for prediction
sepal_length = st.slider('Sepal Length (cm)', min_value=4.0, max_value=8.0, value=5.1)
sepal_width = st.slider('Sepal Width (cm)', min_value=2.0, max_value=4.5, value=3.5)
petal_length = st.slider('Petal Length (cm)', min_value=1.0, max_value=7.0, value=1.4)
petal_width = st.slider('Petal Width (cm)', min_value=0.1, max_value=2.5, value=0.2)

#user input dataframe
user_input = pd.DataFrame({
    'sepal_length': [sepal_length],
    'sepal_width': [sepal_width],
    'petal_length': [petal_length],
    'petal_width': [petal_width]
})

st.write('### Your Input Values')
st.dataframe(user_input)

#use knn k=9 as the prediction model
model = KNeighborsClassifier(n_neighbors=9)
X = df.drop(columns='species')
y = df['species']

#scale data
sc = StandardScaler()
X_sc = sc.fit_transform(X)

#scale user input
user_input_sc = sc.transform(user_input)

#train scaled data
model.fit(X_sc, y)

#make predictions
prediction = model.predict(user_input_sc)[0]

#display result
st.write(f'The model predicts that the iris is of the species: **{prediction}**')
st.balloons()