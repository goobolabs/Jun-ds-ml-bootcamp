# Project Proposal: Credit Card Fraud Detection API 

**Date:** July 2026

## Certificate Name
Abdirahman Khadar Muxumed

---

## Project Title and Description
**Title:** Real-Time Credit Card Fraud Detection API  
A financial institution processes thousands of card transactions daily and requires an instant mechanism to flag fraudulent activity. This project builds a machine learning model that predicts whether an incoming credit card transaction is legitimate or fraudulent based on transaction attributes (time, amount, and structural behavioral features). The final deliverable is a production ready REST API that accepts transaction data as JSON and instantly returns a fraud prediction accompanied by a risk probability score serving as a critical automated line of defense for banking security systems.

---

## Problem Type
Classification binary output: Approved (0 for Legitimate) or Rejected (1 for Fraudulent).  
The target column is `Class`. This is a supervised learning task using historical transaction logs where fraud instances have already been confirmed and labeled.

---

## Dataset
* **Source:** Credit Card Fraud Detection Dataset (Kaggle mirror of anonymized European cardholder transactions). [Dataset Link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
* **Size:** 284,807 rows, 31 columns.
* **Target:** `Class` — whether the transaction is legitimate (0) or a fraud attempt (1).
* **Main Features:**
  * `Time` — seconds elapsed between this transaction and the first transaction in the dataset (numeric).
  * `Amount` — transaction monetary volume (numeric).
  * `V1` to `V28` — anonymized features obtained via Principal Component Analysis (PCA) representing latent behavioral patterns (numeric).
* **Preprocessing plan:** Standardize numerical features (`Time` and `Amount`) using a RobustScaler, handle extreme class imbalance using internal algorithm parameters (like `scale_pos_weight` in XGBoost), and perform a stratified train/test split (80/20) to preserve the minor class distribution.

---

## Algorithms I Plan to Train

| # | Algorithm | Why it fits |
|---|---|---|
| **1** | Logistic Regression |Baseline for binary classification; fast, highly interpretable, and establishes a solid benchmark when utilizing balanced class weights. |
| **2** | Random Forest |Ensemble; robust against overfitting, aggregates multiple decision trees, and handles skewed feature distributions well. |
| **3** | XGBoost Classifier | Researched gradient boosting framework; highly optimized for structured/tabular data and specifically designed to handle extreme class imbalances efficiently. |

---

## Evaluation Plan
Metrics for all models (computed on the same held-out stratified test set):
* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1-Score

**Best-model rule:** Rank all trained models by their **F1-Score** on the test set. Accuracy is an unreliable metric here because over 99% of the transactions are legitimate. F1-Score directly balances *Precision* (minimizing false alarms that freeze legitimate customer cards) and *Recall* (catching the actual thieves). If two models tie on F1-Score, the tiebreaker will be the highest **Recall** to prioritize capturing maximum financial risk.

---

## Deployment Sketch
* **Framework:** FastAPI (High performance, modern syntax, and auto-generates interactive API documentation at `/docs`).
* **Endpoint:** `POST /predict`

### Input JSON Example:
```json
{
  "Time": 85000.0,
  "Amount": 15500.00,
  "V1": 1.15, "V2": -0.25, "V3": 0.65, "V4": 0.45, "V5": -0.35,
  "V6": 0.15, "V7": -0.10, "V8": 0.05, "V9": 0.55, "V10": -0.05,
  "V11": -0.20, "V12": 0.35, "V13": 0.10, "V14": 0.15, "V15": 0.95,
  "V16": 0.25, "V17": -0.15, "V18": -0.05, "V19": 0.10, "V20": -0.05,
  "V21": -0.05, "V22": 0.12, "V23": -0.08, "V24": 0.05, "V25": 0.32,
  "V26": -0.15, "V27": 0.02, "V28": 0.01
}

JSON OUTPUT
{
  "prediction": 0,
  "fraud_probability": 0.0142,
  "status": "Legitimate"
}
```
---

## Repository Plan
```project hierarchy 
Traveling-accident-prediction/
├── dataset/
│   ├── raw_creditcard.csv             # Raw dataset
│   └── cleaned_creditcard.csv       # Preprocessed dataset
├── utility/
│   ├── preprocess.py              # Data loading, scaling, and splitting logic
│   └── train.py                   # Model training, comparison loops, and serialization
├── api/
│   └── app.py                     # FastAPI application script with routing endpoints
├── models/
│   └── best_model.pkl             # Single dictionary containing winning model, scaler, and feature list
├── README.md                      # Setup and execution instructions
└── project_paper.md               # Detailed final reporting document
```