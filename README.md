# Phishing-Link-Detector
ML-based phishing URL detector using Logistic Regression and Flask


#  Phishing Link Detector (ML-Based)

A machine learning web application that detects phishing URLs in real-time.

##  About
This project classifies URLs as **safe** or **phishing** using a 
Logistic Regression model trained on 500,000+ real URLs.

##  How It Works
- Extracts features from URLs (length, HTTPS, IP address, suspicious keywords, etc.)
- Uses Logistic Regression to classify the URL
- Displays risk percentage to the user

##  Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas & NumPy
- HTML/CSS/JavaScript

##  Model Performance
- Dataset: 500,000+ URLs
- Algorithm: Logistic Regression
- Accuracy: 92%+

##  How to Run
1. Install dependencies: `pip install -r dependencies.txt`
2. Train the model: `python train.py`
3. Run the app: `python app1.py`
4. Open browser: `http://127.0.0.1:5000`

##  Made by Muskan Jha
