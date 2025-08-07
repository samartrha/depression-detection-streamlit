import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("depression_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ---------------------------
# 🌟 Page Config & Styling
# ---------------------------
st.set_page_config(page_title="Mental Health App", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stTextArea > label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# 🧠 App Title
# ---------------------------
st.markdown("<h1 style='text-align: center; color: #4B6CB7;'>🧠 Mental Health Depression Detector</h1>", unsafe_allow_html=True)

# ---------------------------
# 📋 User Inputs
# ---------------------------
with st.form("input_form"):
    st.subheader("💬 Share Your Thoughts")
    user_input = st.text_area("Type something you're feeling or thinking...", height=150)

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("🎂 Age", min_value=10, max_value=100, step=1)
    with col2:
        gender = st.selectbox("🚻 Gender", ["Prefer not to say", "Male", "Female", "Other"])

    submitted = st.form_submit_button("🔍 Analyze")

# ---------------------------
# 🧾 Prediction Logic
# ---------------------------
if submitted:
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]

        st.subheader("🧾 Prediction Result")
        if prediction == 1:
            st.error("⚠️ Signs of depression detected. Please consider speaking to a mental health professional.")
        else:
            st.success("😊 No signs of depression detected. Keep taking care of your mental well-being!")

# ---------------------------
# 📌 Footer
# ---------------------------
st.markdown("---")
st.markdown("<small><i>This is a demo tool and should not be used as a substitute for professional advice.</i></small>", unsafe_allow_html=True)
st.markdown("Built with ❤️ by [Samartha Rama](https://github.com/samartrha)")
