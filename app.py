import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sklearn

# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()

# Function for text transformation
def transformed_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# Load vectorizer and model
with open('vectorizer.pkl', 'rb') as file:
    tidif = pickle.load(file)  

with open('model.pkl', 'rb') as file:
    Model = pickle.load(file)  

# --------------- Streamlit UI -------------------

# Set page config for better UI
st.set_page_config(page_title="Spam Detector", page_icon="📩", layout="centered")

# Stylish Header
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>📩 Email / SMS Spam Classifier</h1>", unsafe_allow_html=True)

# Description
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>🔍 Enter a message below and let AI determine whether it's Spam or Not!</p>",
    unsafe_allow_html=True
)

# Input Box
Message = st.text_area(
    "✏️ **Enter the Message:**",
    placeholder="Type or paste your message here...",
    height=150
)

# Predict Button
if st.button('🚀 Predict'):
    if Message.strip() == "":
        st.warning("⚠️ Please enter a message to classify.")
    else:
        with st.spinner('🔍 Analyzing message...'):
            # Preprocessing
            transform_message = transformed_text(Message)

            # Vectorizing
            vector_input = tidif.transform([transform_message])

            # Predicting
            result = Model.predict(vector_input)[0]

            # Display Result
            if result == 1:
                st.markdown(
                    "<h2 style='color: red; text-align: center;'>🚨 Spam Alert!</h2>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<h2 style='color: green; text-align: center;'>✅ Not Spam</h2>",
                    unsafe_allow_html=True
                )

# Footer
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: #A9A9A9;'>⚡ Powered by Machine Learning | Created with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
