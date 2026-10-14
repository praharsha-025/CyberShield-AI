# 🛡️ CyberShield AI

### AI/ML-Based Message Spam and Phishing URL Detection

CyberShield AI is an individual machine learning and MLOps project that demonstrates how machine learning models can classify suspicious messages and potentially phishing URLs through a REST API.

The project combines two features in one application:

- **ScamShield:** Classifies messages as spam or legitimate.
- **PhishGuard:** Classifies URLs as potentially phishing or legitimate.

## 🚀 Live Demo

- **API Home:** https://cybershield-ai-latest.onrender.com/
- **Health Check:** https://cybershield-ai-latest.onrender.com/health
- **Interactive API Documentation:** https://cybershield-ai-latest.onrender.com/docs

## ✨ Features

- Message classification using TF-IDF and Logistic Regression.
- Separate machine learning model for URL classification.
- REST API built with FastAPI.
- Interactive API testing using Swagger UI and Postman.
- Docker image creation and container testing.
- Docker Hub image publishing.
- Cloud deployment using Render.
- Source code management using Git and GitHub.

## 🧰 Technology Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Pandas, TF-IDF, Logistic Regression
- **API Framework:** FastAPI
- **Server:** Uvicorn
- **API Testing:** Postman, Swagger UI
- **Version Control:** Git and GitHub
- **Containerization:** Docker
- **Image Registry:** Docker Hub
- **Deployment:** Render

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays the API welcome message |
| GET | `/health` | Checks API health |
| POST | `/predict` | Classifies a message |
| POST | `/predict-url` | Classifies a URL |

## 🧪 Example API Requests

### 1. ScamShield — Message Detection

Send a POST request to:

`https://cybershield-ai-latest.onrender.com/predict`

Request body:

```json
{
  "message": "Congratulations! You won a prize. Click this link to claim your reward."
}
```

### 2. PhishGuard — URL Detection

Send a POST request to:

`https://cybershield-ai-latest.onrender.com/predict-url`

Request body:

```json
{
  "url": "http://paypal-login-security.example"
}
```

Use the interactive API documentation to submit these requests and view the model's predictions.

## 🖥️ Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/praharsha-025/CyberShield-AI.git
cd CyberShield-AI
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment on Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Start the API

```bash
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs in your browser.

## 🐳 Docker Hub

Published image:

`mogullapraharsha/cybershield-ai:latest`

Pull the image:

```bash
docker pull mogullapraharsha/cybershield-ai:latest
```

Run the container locally:

```bash
docker run --rm -p 8000:8000 mogullapraharsha/cybershield-ai:latest
```

Then open http://127.0.0.1:8000/docs.

## ⚙️ Project Workflow

1. Prepare sample datasets for messages and URLs.
2. Train the machine learning models.
3. Build API endpoints using FastAPI.
4. Test the endpoints with Swagger UI and Postman.
5. Build a Docker image.
6. Upload the image to Docker Hub.
7. Deploy the application on Render.
8. Verify the deployed API endpoints.

## ⚠️ Limitations

This project uses small demonstration datasets. Its predictions may be inaccurate and must not be treated as proof that a message or website is safe or malicious. The project does not perform live website scanning or check real-time threat intelligence feeds.

Do not enter passwords, banking details, or other sensitive information into suspicious websites.

## 👩‍💻 Project Type

Individual B.Tech Computer Science and Engineering project focused on AI/ML, REST APIs, containerization, and deployment.
