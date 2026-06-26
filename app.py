import streamlit as st
import pandas as pd
import joblib

model=joblib.load('Knn_heart.pkl')
scaler=joblib.load('scaler.pkl')
expected_columns=joblib.load('columns.pkl')

st.title('Heart Disease Prediction')
st.markdown('This app predicts the likelihood of heart disease based on user input features.')


age=st.slider("Age",18,100,40)
sex=st.selectbox("Sex",["Male","Female"])
chest_pain=st.selectbox("Chest Pain Type",['ATA','NAP','ASY','TA'])
resting_bp=st.number_input("Resting Blood Pressure (mm Hg)",80,200,120)
cholesterol=st.number_input("Serum Cholesterol (mg/dl)",100,600,200)
fasting_bs=st.selectbox("Fasting Blood Sugar > 120 mg/dl",["0","1"])
resting_ecg=st.selectbox("Resting Electrocardiographic Results",['Normal','ST','LVH'])
max_hr=st.slider("Maximum Heart Rate Achieved",60,220,150)
exercise_angina=st.selectbox("Exercise Induced Angina",["Yes","No"])
oldpeak=st.slider("Oldpeak (ST depression induced by exercise)",0.0,6.0,1.0)
st_slope=st.selectbox("Slope of the Peak Exercise ST Segment",['Up','Flat','Down'])

if st.button("Predict"):
    raw_input={
        'Age': age,
        'Sex'+ sex: 1,
        'ChestPainType'+ chest_pain: 1,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'RestingECG'+ resting_ecg: 1,
        'MaxHR': max_hr,
        'ExerciseAngina'+ exercise_angina: 1,
        'Oldpeak': oldpeak,
        'ST_Slope'+ st_slope: 1
    }
    input_df=pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0
    input_df=input_df[expected_columns]
    scaled_input=scaler.transform(input_df)
    prediction=model.predict(scaled_input)[0]
    if prediction==1:
        st.error("The model predicts that you are likely to have heart disease. Please consult a healthcare professional for further evaluation.")
    else:
        st.success("The model predicts that you are unlikely to have heart disease. However, please consult a healthcare professional for personalized advice.")