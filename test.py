import streamlit as st

st.title("Test")

age = st.slider("Age", 18, 100, 40)
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Predict"):
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")