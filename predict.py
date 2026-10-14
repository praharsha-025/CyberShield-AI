
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "scam_model.joblib"

model = joblib.load(MODEL_PATH)


def predict_message(message):
    message = message.strip()

    if not message:
        return {
            "message": message,
            "prediction": "Invalid input",
            "risk": "Please enter a message."
        }

    prediction = model.predict([message])[0]

    if prediction == "spam":
        result = "Spam/Suspicious"
        risk = "Potentially suspicious. Verify before responding."
    else:
        result = "Legitimate"
        risk = "Classified as legitimate by the model. Still verify links and requests."

    return {
        "message": message,
        "prediction": result,
        "risk": risk
    }


if __name__ == "__main__":
    test_message = input("Enter a message to check: ")
    result = predict_message(test_message)

    print("\n--- CyberShield AI Result ---")
    print("Message:", result["message"])
    print("Prediction:", result["prediction"])
    print("Risk:", result["risk"])
