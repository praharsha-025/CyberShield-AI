# CyberShield AI

AI-powered suspicious message and phishing URL detection using
Machine Learning and FastAPI.

## Features

- Detects potentially suspicious messages.
- Classifies website URLs as potentially phishing or legitimate.
- Provides REST API endpoints using FastAPI.
- Supports testing through Postman.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- FastAPI
- Pydantic
- Joblib
- Git and GitHub
- Docker (planned)
- Docker Hub (planned)
- Render deployment (planned)

## Project Structure

```text
CyberShield-AI/
├── data/
│   ├── messages.csv
│   └── urls.csv
├── models/
│   ├── scam_model.joblib
│   └── phishing_url_model.joblib
├── main.py
├── predict.py
├── train_model.py
├── train_url_model.py
├── README.md
└── .gitignore