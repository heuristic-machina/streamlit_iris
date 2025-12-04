import streamlit as st
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

from data_utils import load_iris

df=load_iris()

st.title('🛠️ Model Training and Evaluation')

#model selection sidebar
st.sidebar.subheader('Choose a Machine Learning Model')
model_option = st.sidebar.selectbox('Select a model', ['K-Nearest Neighbors', 'Logistic Regression', 'Random Forest'])

#data prep
X = df.drop(columns='species')
y = df['species']

#train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)

#scale the data
sc=StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

#initialize selected model
if model_option == 'K-Nearest Neighbors':
    k=st.sidebar.slider('Select number of neighbors (k)', min_value=1, max_value=20, value=3)
    model=KNeighborsClassifier(n_neighbors=k)
elif model_option == 'Logistic Regression':
    model = LogisticRegression()
else:
    model = RandomForestClassifier()

#train model of scaled data
model.fit(X_train_sc, y_train)

#display accuracy
st.write(f'**Model Selected: {model_option}**')
st.write(f'Training Accuracy: {model.score(X_train_sc, y_train):.2f}')
st.write(f'Test Accuracy: {model.score(X_test_sc, y_test):.2f}')

#display confusion matrix
st.subheader('Confusion Matrix')
fig, ax = plt.subplots()
ConfusionMatrixDisplay.from_estimator(model, X_test_sc, y_test, ax=ax, cmap='Greens')
st.pyplot(fig)
