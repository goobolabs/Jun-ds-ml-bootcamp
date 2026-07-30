# Rainfall Prediction API

**Author:** Yahye-Tech
**Date:** 14 July 2026

Machine learning project that predicts whether rainfall is expected tomorrow using historical
weather data from the Kaggle WeatherAUS dataset, deployed as a REST API with FastAPI.

---

## Project Overview

- **Problem type:** Binary classification (supervised learning)
- **Target:** `RainTomorrow` (1 = Rain expected, 0 = No rain expected)
- **Dataset:** [WeatherAUS](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package) (~145,000 records)
- **Algorithms:** Logistic Regression, Random Forest, Gradient Boosting (scikit-learn)
- **Best model selection:** Highest F1-Score (Recall as tiebreaker)
- **Selected model:** Random Forest (F1 = 0.6341, Recall = 0.7638)

---

## Features Used

| Feature | Description |
|---|---|
| MinTemp | Minimum temperature |
| MaxTemp | Maximum temperature |
| Rainfall | Amount of rainfall recorded |
| Evaporation | Daily evaporation |
| Sunshine | Hours of sunshine |
| WindGustSpeed | Maximum wind gust speed |
| Humidity9am | Humidity at 9 AM |
| Humidity3pm | Humidity at 3 PM |
| Pressure9am | Atmospheric pressure at 9 AM |
| Pressure3pm | Atmospheric pressure at 3 PM |
| Temp9am | Temperature at 9 AM |
| Temp3pm | Temperature at 3 PM |
| RainToday | Whether it rained today |

---

## Folder Structure

```
rainfall-prediction-api/
├── dataset/
│   └── weatherAUS.csv
├── src/
│   ├── preprocess.py
│   └── train.py
├── api/
│   └── app.py
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── metrics_report.json
├── notebooks/
│   └── exploration.ipynb
├── README.md
├── requirements.txt
└── project_paper.md
```

---

## Installation

```bash
cd rainfall-prediction-api
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

---

## Usage

### 1. Train models

```bash
python src/train.py
```

This trains all three models, compares them, and saves the best model to `models/best_model.pkl`.

### 2. Run the API

```bash
uvicorn api.app:app --reload
```

Open `http://localhost:8000/docs` for interactive Swagger documentation.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Service information |
| GET | `/health` | Health check (model and preprocessor status) |
| GET | `/docs` | Interactive Swagger documentation |
| POST | `/predict` | Submit weather data and receive rainfall prediction |

---

## API Example

**POST** `/predict`

Request:

```json
{
  "MinTemp": 18.2,
  "MaxTemp": 29.4,
  "Rainfall": 0.0,
  "Humidity9am": 65,
  "Humidity3pm": 48,
  "Pressure9am": 1018.4,
  "Pressure3pm": 1015.7,
  "Temp9am": 21.0,
  "Temp3pm": 28.1,
  "WindGustSpeed": 35,
  "RainToday": "No"
}
```

Response:

```json
{
  "prediction": "No Rain",
  "probability": 0.94
}
```

---

## Model Comparison Results

All models were evaluated on the same 20% test split using Accuracy, Precision, Recall,
F1-Score, and Confusion Matrix.

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.7871 | 0.5132 | 0.7604 | 0.6128 |
| **Random Forest** | **0.8047** | **0.5421** | **0.7638** | **0.6341** |
| Gradient Boosting | 0.8538 | 0.7416 | 0.5224 | 0.6130 |

The model with the highest F1-Score is selected for deployment. If two models tie, the one
with higher Recall is chosen.

**Selected model: Random Forest** (F1-Score = 0.6341, Recall = 0.7638)

---

## Technologies

| Category | Technology |
|---|---|
| Language | Python 3.11+ |
| Data | pandas, numpy |
| ML | scikit-learn |
| API | FastAPI, Uvicorn |
| Validation | Pydantic |
