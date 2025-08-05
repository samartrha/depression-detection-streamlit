import streamlit as st
import pickle

# Load the trained model and vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('depression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title and instructions
st.title("🧠 Depression Detection App")
st.write("Enter a message or journal entry to check for signs of depression.")

# Text input
user_input = st.text_area("Type your text here:")

# Prediction
if st.button("Check for Depression"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vectorized_input = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_input)

        if prediction[0] == 1:
            st.error("⚠️ The input indicates signs of depression.")
        else:
            st.success("✅ The input does not indicate signs of depression.")
