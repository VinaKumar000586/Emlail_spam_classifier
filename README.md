📩 Email & SMS Spam Classifier
🚀 Detect spam messages with AI-powered classification!


📌 Overview
This project is an AI-powered Email and SMS Spam Classifier built using Machine Learning . It helps detect whether a message is Spam or Not Spam by analyzing its text features.
🔹 Technologies Used:
✅ Python (NLP, ML)
✅ Streamlit (Web UI)
✅ Scikit-learn (Machine Learning)
✅ NLTK (Text Processing)
✅ Matplotlib & Seaborn (Data Visualization)

📂 Project Structure
📂 SpamClassifier
├── 📜 email_classification.py  # Machine Learning Model & Training
├── 📜 app.py                   # Streamlit Web App
├── 📜 model.pkl                # Trained ML Model
├── 📜 vectorizer.pkl           # TF-IDF Vectorizer
└── 📜 README.md                # Project Documentation

🎯 Features
✔️ Preprocesses text data (Tokenization, Stopwords Removal, Stemming)
✔️ Trains multiple ML models (Naïve Bayes, Decision Trees, Random Forest, Gradient Boosting)
✔️ Uses TF-IDF vectorization for text feature extraction
✔️ Interactive Web UI using Streamlit
✔️ Real-time message classification

##🚀 How to Run the Project
🔹 1. Install Dependencies
     pip install -r requirements.txt
🔹 2. Run the Streamlit App
      streamlit run app.py

🧪 Model Training
🔹 The email_classification.py script performs the following:
✅ Exploratory Data Analysis (EDA)
✅ Data Cleaning & Preprocessing
✅ Feature Extraction using TF-IDF
✅ Model Training & Evaluation
✅ Hyperparameter Tuning for Optimization

📊 Best Performing Model: Multinomial Naïve Bayes (Highest accuracy & precision)
![image](https://github.com/user-attachments/assets/9ebfb159-e567-450e-86da-1bc21cc839e0)

📂 Project Structure
bash
Copy code
📂 SpamClassifier
│── 📜 app.py                 # Streamlit Web Application
│── 📜 email_classification.py # Model Training & Text Processing
│── 📜 model.pkl              # Trained ML Model (Naïve Bayes)
│── 📜 vectorizer.pkl         # TF-IDF Vectorizer
│── 📜 requirements.txt       # Dependencies for running the project
│── 📜 README.md              # Project Documentation
│
├── 📂 data
│   ├── email.csv             # Dataset for training
│
├── 📂 notebooks
│   ├── email_classification.ipynb  # Jupyter Notebook for EDA & Model Training
│
└── 📂 assets
    ├── spam_wordcloud.png    # Spam WordCloud Visualization
    ├── ham_wordcloud.png     # Non-Spam WordCloud Visualization
    ├── ui_screenshot.png     # Screenshot of the Streamlit UI

    

    
