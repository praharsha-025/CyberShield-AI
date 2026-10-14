import pandas as pd
import joblib
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "messages.csv"
df = pd.read_csv(DATA_PATH)

if not {"message", "label"}.issubset(df.columns):
    raise ValueError("Dataset must contain message and label columns.")

df = df.dropna(subset=["message", "label"])
df["message"] = df["message"].astype(str)
df["label"] = df["label"].astype(str).str.strip().str.lower()

if set(df["label"].unique()) != {"spam", "legitimate"}:
    raise ValueError("Labels must be 'spam' and 'legitimate'.")

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(df["message"], df["label"])

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "scam_model.joblib"
joblib.dump(model, MODEL_PATH)

print("ScamShield model trained successfully!")
print(f"Training messages: {len(df)}")
print(f"Saved model to: {MODEL_PATH}")