# 🧠 Mental Health Depression Detection App

This is a simple web-based application built with **Streamlit** and **Machine Learning** that detects possible signs of depression based on user-inputted text.

## 🔍 Features
- Input free-form text (thoughts or feelings)
- Predicts whether signs of depression are detected
- User-friendly web interface using Streamlit
- Trained with Natural Language Processing (NLP) techniques

## 🛠 Technologies Used
- Python
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

## 📊 Dataset

The model was trained using a dataset from Kaggle:  
**[Student Depression - Text Data](https://www.kaggle.com/datasets/nidhiy07/student-depression-text)**  
This dataset contains textual responses from students, labeled as "depressed" or "not depressed", which was used to train the sentiment classification model using TF-IDF vectorization and machine learning techniques.

## 🚀 How to Run Locally

1. Clone the repo:
   git clone https://github.com/samartrha/depression-detection-streamlit.git
   cd depression-detection-streamlit
   
2. Install dependencies (if not already):
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run streamlit_app.py


🗂️ Repository Structure
📁 depression-detection-streamlit/
├── app.py                 # Model training (optional)
├── streamlit_app.py       # Main Streamlit frontend app
├── vectorizer.pkl         # Saved TfidfVectorizer
├── depression_model.pkl   # Trained model
└── README.md              # Project documentation


## 📁 Files Included
- `streamlit_app.py` - Streamlit frontend script
- `app.py` - Testing script
- `depression_model.pkl` - Trained machine learning model
- `vectorizer.pkl` - Text vectorizer (TF-IDF or CountVectorizer)

## 📦 Deployment
You can deploy this app easily using [Streamlit Cloud](https://streamlit.io/cloud).

## 🧑‍💻 Author
- **Samartha Rama**
- 
---
📧 samartharama7@gmail.com  
🌐 [GitHub Profile](https://github.com/samartrha)

## ⚠️ Disclaimer
This tool is only for educational/demonstration purposes. It is **not a substitute** for professional mental health advice.

Let me know if you'd like me to add:
- 📸 Screenshot of the app  
- 🧪 Model accuracy / performance section  
- 📚 References or citation for the dataset

Happy coding!


