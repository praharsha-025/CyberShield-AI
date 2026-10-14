import pandas as pd
import joblib
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent

# Load URL training data
DATA_PATH = BASE_DIR / "data" / "urls.csv"
df = pd.read_csv(DATA_PATH)

# Validate the dataset
if not {"url", "label"}.issubset(df.columns):
    raise ValueError("CSV must contain url and label columns.")

df = df.dropna(subset=["url", "label"])
df["url"] = df["url"].astype(str).str.strip()
df["label"] = df["label"].astype(str).str.strip().str.lower()

if set(df["label"].unique()) != {"phishing", "legitimate"}:
    raise ValueError("Labels must be phishing and legitimate.")

# Build the URL classification model
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            analyzer="char",
            ngram_range=(2, 5),
            lowercase=True
        )
    ),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train the model
model.fit(df["url"], df["label"])

# Save the model
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "phishing_url_model.joblib"
joblib.dump(model, MODEL_PATH)

print("PhishGuard URL model trained successfully!")
print(f"Training URLs: {len(df)}")
print(f"Saved model to: {MODEL_PATH}")