# Final Project Proposal — Student Mental Health and Stress Prediction API

> This proposal presents a machine learning project that combines both **Classification** and **Regression** using the same dataset. The system predicts a student's **Stress Level** and **Mental Health Score** based on social media usage and lifestyle habits.

**Date:** July 2026

---

# 1. Certificate Name

**Saacid Abdiaziiz Yuusuf**

---

# 2. Project Title and Description

## Title

**Student Mental Health and Stress Prediction Using Social Media Usage and Lifestyle Habits**

### Description

Social media has become an important part of students' daily lives, influencing both their academic performance and mental well-being. Excessive social media use, poor sleep habits, limited physical activity, and reduced study time may contribute to increased stress and lower mental health.

This project aims to develop **two machine learning models** using the same dataset:

- A **Classification Model** to predict a student's **Stress Level**.
- A **Regression Model** to predict a student's **Mental Health Score**.

The final system will be deployed as a REST API using **FastAPI**, allowing users to submit student information and receive predictions for both stress level and mental health score.

---

# 3. Problem Type

This project combines **two supervised machine learning tasks**.

## Task 1: Classification

**Target Column**

`Stress_Level`

Possible classes:

- Low
- Medium
- High
- Very High

---

## Task 2: Regression

**Target Column**

`Mental_Health_Score`

The model predicts a continuous numerical value representing the student's overall mental health.

---

## 4. Dataset

- **Source:** [Student Social Media and Mental Health Impact Dataset (Kaggle).](https://www.kaggle.com/datasets/shivasingh4945/student-social-media-and-mental-health-impact).
- **Size:** Approximately 5,000 rows, 13 columns.
- **Classification Target:** `Stress_Level` — predicts whether a student's stress level is Low, Medium, High, or Very High.
- **Regression Target:** `Mental_Health_Score` — predicts the student's overall mental health score.
- **Main Features:**
  - `Age` — student age (numeric)
  - `Gender` — student gender (categorical)
  - `Country` — country of residence (categorical)
  - `Academic_Level` — education level (categorical)
  - `Most_Used_Platform` — primary social media platform (categorical)
  - `Purpose_Of_Use` — reason for using social media (categorical)
  - `Avg_Daily_Usage_Hours` — average daily social media usage (numeric)
  - `Daily_Unlocks` — phone unlocks per day (numeric)
  - `Study_Hours` — daily study hours (numeric)
  - `Physical_Activity_Hours` — daily exercise hours (numeric)
  - `Sleep_Hours_Per_Night` — average sleep duration (numeric)
- **Preprocessing Plan:** Handle missing values, remove duplicates, encode categorical features (One-Hot or Label Encoding), scale numerical features using StandardScaler, and split the dataset into training and testing sets (80/20).

# 5. Algorithms I Plan to Train

## Classification Models

| Algorithm | Reason |
|-----------|--------|
| Logistic Regression | Logistic Regression will be used as a baseline classification model because it provides a simple and interpretable approach for predicting student stress levels. |
| Random Forest Classifier | Random Forest Classifier will be used because it can handle multiple student lifestyle features and capture complex patterns in tabular data. |
| Support Vector Machine (SVM) | Support Vector Machine will be used because it is effective for classification tasks and can identify decision boundaries between different stress level categories. |

---

## Regression Models

| Algorithm | Reason |
|-----------|--------|
| Linear Regression | Linear Regression will be used as a baseline regression model because it predicts the continuous Mental Health Score based on relationships between input features and the target value. |
| Random Forest Regressor | Random Forest Regressor will be used because it can capture non-linear relationships between social media usage patterns and mental health scores. |

# 6. Evaluation Plan

Metrics for all classification models (on the same held-out test set):

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Best-model rule: Rank all classification models by F1-Score on the test set. F1 balances Precision and Recall, which is important here because both incorrect stress predictions and missed stress cases can affect the reliability of the system. If two models tie on F1-Score, break the tie with higher Recall because it identifies more actual stress cases correctly.

For regression models, performance will be evaluated using:

- MAE
- MSE
- RMSE
- R² Score

I will print a comparison table with one row per algorithm and save/deploy only the best-performing models.
# 7. Deployment Sketch

- **Framework:** FastAPI (simple, modern, auto-generates API docs at `/docs`).
- **Endpoint:** `POST /predict`
- **Input JSON example:**


```json
{
  "Age": 21,
  "Gender": "Male",
  "Country": "Somalia",
  "Academic_Level": "Undergraduate",
  "Most_Used_Platform": "Instagram",
  "Purpose_Of_Use": "Entertainment",
  "Avg_Daily_Usage_Hours": 6.5,
  "Daily_Unlocks": 180,
  "Study_Hours": 3,
  "Physical_Activity_Hours": 1,
  "Sleep_Hours_Per_Night": 6
}
```

---

## Output JSON Example

```json
{
  "Stress_Level": "High",
  "Stress_Probability": 0.91,
  "Mental_Health_Score": 6.84
}
```

---

# 8. Repository Plan
```
student-mental-health-api/
│
├── dataset/
│   └── student_social_media.csv
│
├── src/
│   ├── preprocess.py        # data cleaning, encoding, scaling, train/test split
│   └── train.py             # train models, compare performance, save best models
│
├── api/
│   └── app.py               # FastAPI app with /predict endpoint
│
├── models/
│   ├── best_classifier.pkl  # best stress level prediction model
│   ├── best_regressor.pkl   # best mental health score prediction model
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── notebooks/
│   └── exploration.ipynb    # optional EDA and data analysis
│
├── README.md
├── requirements.txt
└── project_paper.md
```
---

## Planned Commands

```bash
python src/train_classification.py

python src/train_regression.py

uvicorn api.app:app --reload
```

---

# Expected Outcome

The completed system will:

- Predict a student's **Stress Level** using a Classification model.
- Predict a student's **Mental Health Score** using a Regression model.
- Compare multiple machine learning algorithms to identify the best-performing models.
- Provide predictions through a FastAPI REST API.

The project demonstrates both **Classification** and **Regression** techniques using a single real-world dataset, providing a comprehensive analysis of the relationship between social media usage, lifestyle habits, stress, and mental health.