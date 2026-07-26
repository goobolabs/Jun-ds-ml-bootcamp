# Goobo Classifier Deployment

Loan approval demo branded as **Goobo Classifier**. Same simple layout as the house demo: process → train/save → Flask API → client UI.

```
deployment/
├── processing.py   # reuse Lesson 5 loan cleaning (+ save scaler/columns)
├── model.py        # reuse Lesson 5 LR + RF (+ joblib save + optional custom test)
├── utils.py        # raw form → model features
├── app.py          # Flask /predict?model=lr|rf
├── models/         # artifacts
└── client/         # Goobo-branded Next.js UI
```

## Setup

```bash
pip install -r requirements.txt
```

## Run (from this folder)

```bash
# 1) Clean data + save scaler
python processing.py

# 2) Train + save models (+ optional custom input test)
python model.py

# 3) Start API (port 8000)
python app.py
```

In another terminal:

```bash
cd client
npm install
npm run dev
```

Open http://localhost:3000

## Quick API test

```bash
curl -X POST "http://127.0.0.1:8000/predict?model=rf" \
  -H "Content-Type: application/json" \
  -d '{
    "Income": 65000,
    "CreditScore": 720,
    "EmploymentYears": 5,
    "LoanAmount": 15000,
    "HasCollateral": "Yes",
    "PreviousDefaults": "No"
  }'
```
