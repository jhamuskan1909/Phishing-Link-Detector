from flask import Flask, request, jsonify, render_template
import joblib, re, pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

def extract_features(url):
    return {
        'url_length': len(url),
        'has_https': int(url.startswith('https')),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'has_at': int('@' in url),
        'suspicious_words': int(bool(re.search(
            r'login|verify|secure|bank|account|free|click', url, re.I))),
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.json['url']
    features = pd.DataFrame([extract_features(url)])
    scaled = scaler.transform(features)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]
    return jsonify({
        'prediction': int(pred),
        'probability': round(float(prob) * 100, 1)
    })

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))