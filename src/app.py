import streamlit as st
from pickle import load
import pandas as pd

model = load(open("../models/decision_tree_classifier_default_42.pkl", "rb"))

st.title("Heart Disease Prediction")

HighBP = st.slider("HighBP: ", min_value = 0, max_value = 1, step = 1)
HighChol = st.slider("HighBP: ", min_value = 0, max_value = 1, step = 1)
BMI = st.slider("BMI: ", min_value = 0, max_value = 100, step = 1)
Smoker = st.slider("Smoker: ", min_value = 0, max_value = 1, step = 1)
Stroke = st.slider("Stroke: ", min_value = 0, max_value = 1, step = 1)
Diabetes = st.slider("Diabetes: ", min_value = 0, max_value = 1, step = 1)
PhysActivity = st.slider("PhysActivity: ", min_value = 0, max_value = 1, step = 1)
HvyAlcoholConsump = st.slider("HvyAlcoholConsump: ", min_value = 0, max_value = 1, step = 1)
Sex = st.slider("Sex: ", min_value = 0, max_value = 1, step = 1)

if st.button("Predict"):
    colums = ['HighBP','HighChol','BMI','Smoker','Stroke','Diabetes','PhysActivity','HvyAlcoholConsump','Sex']
    data = pd.DataFrame([[HighBP, HighChol, BMI, Smoker, Stroke, Diabetes, PhysActivity, HvyAlcoholConsump, Sex]], columns=colums)
    prediction = str(model.predict(data)[0])    
    st.write("Prediction:", prediction)