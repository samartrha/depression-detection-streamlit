import streamlit as st 
import joblib

# Load the model and vectorizer
model = joblib.load("depression_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App title
st.title("🧠 Mental Health Depression Detection App")

# User input
user_input = st.text_area("Enter your thoughts or message:")

# Predict button
if st.button("Predict"):
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)

    if prediction[0] == 1:
        st.error("⚠️ Depression Detected. Please consider talking to a mental health professional.")
    else:
        st.success("✅ No signs of depression detected. Stay positive!")
