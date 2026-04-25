import pandas as pd
import re
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv('phishing_site_urls.csv')

# Convert 'good'/'bad' to 0/1
df['label'] = df['Label'].map({'good': 0, 'bad': 1})

def extract_features(url):
    url = str(url)
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

print("Extracting features from 500K URLs... please wait ⏳")
X = pd.DataFrame(df['URL'].apply(extract_features).tolist())
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

acc = accuracy_score(y_test, model.predict(X_test_scaled))
print(f"✅ Accuracy: {acc*100:.2f}%")

joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("✅ model.pkl and scaler.pkl saved!")