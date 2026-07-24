# ✈️ Flight Delay Prediction System
## Githup link of project
https://github.com/fatima-moha143/fligh_delay_predict.git
## 📌 Machine Learning Classification Project

A Machine Learning based web application that predicts whether a flight will be **On-Time** or **Delayed**.

This project uses different classification algorithms and deploys the best-performing model using **FastAPI** with a simple and user-friendly web interface.

---

# 📖 Project Overview

Flight delays create major problems for airlines and passengers, including financial losses, schedule disruption, and customer dissatisfaction.

The goal of this project is to build a predictive system that can estimate flight delays based on flight information and historical patterns.

The system classifies flights into two categories:

- **0 → On-Time**
- **1 → Delayed**

---

# 🎯 Objectives

The main objectives of this project are:

- Analyze flight data and discover important patterns
- Clean and preprocess raw flight data
- Build multiple classification models
- Compare model performance
- Select the best model
- Deploy the model as a web application using FastAPI

---

# 📂 Dataset Description

Dataset:
**Flight Delay Prediction Dataset**

Dataset size:

- Rows: **539,382**
- Features: **7**

### Features

| Feature | Description |
|---|---|
| Flight | Flight number |
| Time | Departure time |
| Length | Flight duration |
| Airline | Airline code |
| AirportFrom | Departure airport |
| AirportTo | Arrival airport |
| DayOfWeek | Day of the week |

### Target Variable

| Class | Meaning |
|---|---|
| 0 | On-Time |
| 1 | Delayed |

---

# 🔧 Data Preprocessing

The following preprocessing steps were applied:

✅ Data inspection  
✅ Duplicate checking and handling  
✅ Categorical feature encoding  
✅ One-Hot Encoding  
✅ Feature scaling  
✅ Train/Test split  
✅ Feature alignment for deployment  

---

# 🤖 Machine Learning Models

Three classification models were trained and compared:

## 1. Logistic Regression

A simple and interpretable classification algorithm used as a baseline model.

Advantages:
- Fast training
- Easy interpretation


---

## 2. Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees.

Advantages:
- Handles complex relationships
- Reduces overfitting
- Good performance on structured data


---

## 3. Gradient Boosting Classifier

A boosting algorithm that improves weak learners sequentially.

Advantages:
- High predictive power
- Captures complex patterns


---

# 📊 Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The best model was selected based on performance evaluation.

---

# 🏆 Model Deployment

The final model was deployed using:

### Backend
- FastAPI

### Frontend
- HTML
- CSS

### Model Saving
- Joblib

---

# 🏗️ System Architecture
