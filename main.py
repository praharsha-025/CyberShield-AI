from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent

# Load both trained models
MESSAGE_MODEL_PATH = BASE_DIR / "models" / "scam_model.joblib"
URL_MODEL_PATH = BASE_DIR / "models" / "phishing_url_model.joblib"

message_model = joblib.load(MESSAGE_MODEL_PATH)
url_model = joblib.load(URL_MODEL_PATH)

app = FastAPI(
    title="CyberShield AI",
    description="AI-powered suspicious message and phishing URL detection API",
    version="1.1.0"
)


class MessageRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="The message you want to check"
    )


class URLRequest(BaseModel):
    url: str = Field(
        ...,
        min_length=1,
        max_length=2048,
        description="The website URL you want to check"
    )


@app.get("/")
def home():
    return {
        "message": "Welcome to CyberShield AI",
        "status": "API is running",
        "features": [
            "ScamShield message detection",
            "PhishGuard URL detection"
        ]
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message_model_loaded": True,
        "url_model_loaded": True
    }


@app.post("/predict")
def predict_message(request: MessageRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    prediction = message_model.predict([message])[0]

    if prediction == "spam":
        result = "Spam/Suspicious"
        risk = "Potentially suspicious. Verify before responding."
    else:
        result = "Legitimate"
        risk = (
            "Classified as legitimate by the model. "
            "Still verify links and requests."
        )

    return {
        "message": message,
        "prediction": result,
        "risk": risk
    }


@app.post("/predict-url")
def predict_url(request: URLRequest):
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="URL cannot be empty."
        )

    # Accept only web URLs
    if not url.lower().startswith(("http://", "https://")):
        raise HTTPException(
            status_code=400,
            detail="Enter a URL beginning with http:// or https://."
        )

    prediction = url_model.predict([url])[0]

    if prediction == "phishing":
        result = "Potentially Phishing"
        risk = (
            "The model detected suspicious URL patterns. "
            "Avoid entering personal information until verified."
        )
    else:
        result = "Classified as Legitimate"
        risk = (
            "The model classified this URL as legitimate, "
            "but this does not guarantee that the website is safe."
        )

    return {
        "url": url,
        "prediction": result,
        "risk": risk
    }