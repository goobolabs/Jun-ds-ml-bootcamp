# SuuqPulse AI

## Hidden Market Regime Discovery and Staple Food Price Shock Prediction using Machine Learning

**Repository:** https://github.com/saynis/SuuqPulse_AI  
**API:** https://suuqpulseai-production.up.railway.app  
**Frontend Dashboard:** https://suuq-pulse-ai.vercel.app  

---

## Overview

SuuqPulse AI is an end-to-end machine learning early-warning system for Somali food markets.

The system uses World Food Programme (WFP) food price data to discover hidden market behavior patterns and predict possible future food price shocks.

The project combines:

- Unsupervised Learning (K-Means)
- Supervised Learning (Classification)
- FastAPI deployment
- Next.js dashboard

---

## Problem

Food price instability can create serious challenges for households and humanitarian organizations.

Instead of only forecasting prices, SuuqPulse AI first learns how markets behave and then predicts possible price shocks.

---

## Dataset

Source:

World Food Programme (WFP) Somalia Food Prices Dataset

Raw data:

- 42,616 rows
- 16 columns

After preprocessing:

- 42,304 rows
- 14 columns

Coverage:

- 1995–2026
- 46 markets
- 18 regions
- 22 commodities

Modelled foods:

- Maize
- Rice
- Sorghum
- Wheat flour
- Sugar
- Vegetable oil
- Cowpeas

---

# Machine Learning Pipeline

## Phase 1: Market Regime Discovery

Algorithm:

K-Means Clustering

Purpose:

Discover hidden market behavior groups.

Features:

- Price change
- Volatility
- Spike count
- Relative trend
- Seasonality


Results:

| Regime | Profiles |
|---|---:|
| Growing |233|
| Stable |98|
| High Risk |10|


---

## Phase 2: Price Shock Prediction

The system predicts whether prices will increase more than 15% in the next month.

Models compared:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting


Performance:

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Logistic Regression |64.4%|15.4%|51.9%|23.7%|
| Random Forest |86.8%|26.6%|13.7%|18.1%|
| Gradient Boosting |89.5%|61.3%|3.8%|7.1%|


Final model:

**Logistic Regression**

Selected because it achieved the best F1 score and recall.

---

# Architecture

```
WFP Dataset
      |
      ↓
Preprocessing
      |
      ↓
Feature Engineering
      |
      ↓
K-Means Regimes
      |
      ↓
Shock Classifier
      |
      ↓
FastAPI Backend
      |
      ↓
Next.js Dashboard
```

---

# Project Structure

```
backend/
├── dataset/
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── clustering.py
│   ├── train_classifier.py
│   └── run_pipeline.py
├── models/
│   ├── scaler.pkl
│   ├── kmeans.pkl
│   ├── classifier.pkl
│   └── metadata.joblib
├── utils/
│   └── feature_builder.py
└── api/
    └── app.py

frontend/
└── Next.js Dashboard
```

---

# API

## Health

```
GET /health
```

## Prediction

```
POST /predict
```

Example:

```json
{
 "market":"Bakaara",
 "commodity":"Rice",
 "prices":[1200,1300,1400,1700,1900]
}
```

Response:

```json
{
 "market_regime":"Growing",
 "shock_probability":0.49,
 "prediction":0
}
```

---

# Running Locally

Backend:

```bash
cd backend
pip install -r requirements.txt
python src/run_pipeline.py
uvicorn api.app:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

---

# Deployment

Backend:

https://suuqpulseai-production.up.railway.app

Frontend:

https://suuq-pulse-ai.vercel.app

---

# Future Improvements

- Add rainfall and climate data
- Add conflict indicators
- Add exchange rate information
- Improve time-series validation
- Add more real-time data sources

---

# Lessons Learned

This project covered the complete machine learning lifecycle:

- Data preprocessing
- Feature engineering
- Model comparison
- Evaluation
- Model deployment
- Building a production ML application
