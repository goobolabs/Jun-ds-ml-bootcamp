# Bank Customer Intelligence System

A full-stack machine learning application for bank customer analysis. The system predicts whether a customer is likely to subscribe to a term deposit and assigns the customer to one of two customer segments.

## Main Features

- Term-deposit subscription prediction: `Yes` or `No`
- Prediction probability between `0` and `1`
- Customer segmentation: `Cluster 0` or `Cluster 1`
- Human-readable cluster descriptions
- React analytics dashboard
- FastAPI REST API with Swagger documentation
- Classification and clustering notebooks

## Project Structure

```text
Bank-Customer-Intelligence-System/
├── backend/
│   ├── api/
│   │   ├── app.py
│   │   ├── predict.py
│   │   ├── cluster.py
│   │   └── config.py
│   ├── models/
│   └── src/
├── dataset/
│   └── bank-full.csv
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   └── package.json
├── notebooks/
│   ├── eda.ipynb
│   ├── classification.ipynb
│   └── clustering.ipynb
├── tests/
├── requirements.txt
└── README.md
```

## Setup

Create and activate a Python virtual environment, then install the dependencies:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Install the frontend dependencies:

```bash
cd frontend
npm install
```

## Run the Project

### 1. Start the Backend

From the project root:

```bash
uvicorn backend.api.app:app --reload
```

Backend API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 2. Start the Frontend

```bash
cd frontend
npm run dev
```

Frontend dashboard:

```text
http://localhost:5173
```

## Prediction API

**POST** `/predict`

Example input:

```json
{
  "age": 35,
  "job": "technician",
  "marital": "married",
  "education": "secondary",
  "balance": 2500,
  "housing": "no",
  "loan": "no",
  "campaign": 2
}
```

Example response:

```json
{
  "prediction": "Yes",
  "probability": 0.89
}
```

## Customer Segmentation API

**POST** `/cluster`

Example input:

```json
{
  "age": 35,
  "job": "technician",
  "marital": "married",
  "education": "secondary",
  "balance": 2500,
  "housing": "no",
  "loan": "no",
  "campaign": 2
}
```

Example response:

```json
{
  "cluster": 0,
  "description": "Typical-balance customers, often blue-collar or secondary-educated, with many holding housing loans."
}
```

The clustering model returns only `Cluster 0` or `Cluster 1`.

## Models Used

### Classification

- Logistic Regression
- Random Forest
- XGBoost

**Selected model:** Random Forest

### Clustering

- K-Means
- Agglomerative Clustering
- DBSCAN

**Selected model:** K-Means with `K = 2`

## Technologies

- Python
- pandas
- scikit-learn
- XGBoost
- FastAPI
- React
- Vite
- Axios
- Joblib
- Pytest

## Repository

https://github.com/Abdikani94/Bank-Customer-Intelligence-System