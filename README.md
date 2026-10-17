# Network Security Phishing Detection System

An end-to-end Machine Learning pipeline and web service for detecting phishing websites and malicious network activity.

---

## Architecture Overview

```
MongoDB (Atlas)
       │
       ▼
1. Data Ingestion ────────► Feature Store & Train/Test Split
       │
       ▼
2. Data Validation ───────► Schema Validation & KS-test Drift Detection
       │
       ▼
3. Data Transformation ───► KNNImputation & Target Encoding (preprocessor.pkl)
       │
       ▼
4. Model Training ────────► GridSearchCV across 5 Classifiers:
                            - Random Forest
                            - Gradient Boosting
                            - Decision Tree
                            - Logistic Regression
                            - AdaBoost
       │
       ▼
5. Artifacts & Models ────► Saved to `final_model/` and `Artifacts/`
       │
       ▼
6. FastAPI Web Service ───► Interactive `/predict` UI & API
```

---

## Prerequisites & Environment Setup

### 1. Python Environment
This project runs on Python 3.10 / 3.11:

```powershell
# Activate your virtual environment
.\venv1\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Install package in editable mode
pip install -e .
```

### 2. Environment Variables (.env)
Create a `.env` file in the root directory:

```ini
MONGO_DB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0"
MONGODB_URL_KEY="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0"
DATA_INGESTION_DATABASE_NAME="Ritesh"
```

---

## How to Run Locally

### 1. Run the Full ML Training Pipeline
To run data ingestion, validation, transformation, model evaluation, and export the trained model:

```powershell
python main.py
```

Trained models and preprocessors will be automatically saved to `final_model/model.pkl` and `final_model/preprocessor.pkl`.

### 2. Run the FastAPI Application
Start the web service:

```powershell
python app.py
```
Or with Uvicorn:
```powershell
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

- **Interactive API Docs (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Trigger Training via API**: `GET http://localhost:8000/train`
- **Predict from CSV via API**: `POST http://localhost:8000/predict` (upload a CSV, e.g. `valid_data/test.csv`)

---

## Docker Deployment

### Build the Docker Image
```bash
docker build -t networksecurity:latest .
```

### Run the Docker Container
```bash
docker run -p 8000:8000 --env-file .env networksecurity:latest
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

---

## CI/CD Pipeline (GitHub Actions)

The repository includes an automated CI/CD workflow (`.github/workflows/main.yml`) that:
1. Runs lint and unit test checks on pushes to `main`.
2. Builds the Docker container and pushes to **Amazon ECR**.
3. Deploys the container to a continuous deployment runner.

Required GitHub Secrets for AWS deployment:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ECR_LOGIN_URI`
- `ECR_REPOSITORY_NAME`