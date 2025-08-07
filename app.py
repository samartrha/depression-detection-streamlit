import streamlit as st
import joblib

# Page setup
st.set_page_config(page_title="🧠 Mental Health Checker", layout="centered")

# Load vectorizer and model
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("depression_model.pkl")

# Custom styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            color: #2c3e50;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: gray;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🧠 Mental Health Detection App</p>', unsafe_allow_html=True)
st.write("✨ Enter a journal entry, thought, or sentence. The app will detect if there are signs of depression.")

# Text input
user_input = st.text_area("💬 Type your message here:", height=200)

# Predict button
if st.button("🔍 Check for Depression"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text before checking.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)

        if prediction[0] == 1:
            st.error("⚠️ This input indicates **signs of depression**. Consider reaching out to someone you trust or a professional.")
        else:
            st.success("✅ This input **does not indicate signs of depression**. Keep taking care of your mental well-being! 😊")

# Footer
st.markdown('<p class="footer">🔒 Your text is private and never stored.</p>', unsafe_allow_html=True)
