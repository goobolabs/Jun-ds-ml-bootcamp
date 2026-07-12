# Final Project Proposal

## Certificate Name

**Abdidahir Bashir Ali**

---

# Project Title

## Water Potability Prediction System Using Machine Learning

---

# Project Overview

Access to safe drinking water is essential for public health. However, traditional laboratory testing is often time-consuming, expensive, and requires specialized equipment. This project aims to develop a machine learning-based system that predicts whether water is safe for drinking using physicochemical measurements. In addition to predicting water potability, the system will estimate the associated risk level and provide practical recommendations to help users make informed decisions.

---

# Project Objectives

- Predict whether water is safe for drinking.
- Compare multiple machine learning classification algorithms.
- Build an end-to-end machine learning pipeline.
- Deploy the best-performing model using a Flask REST API.
- Provide users with a simple risk assessment and recommendation based on the prediction.

---

# Problem Type

**Supervised Machine Learning**

**Task:** Binary Classification

### Target Variable

- **Potability = 1** → Safe for drinking
- **Potability = 0** → Unsafe for drinking

---

# Dataset Information

## Dataset Name

Water Potability Dataset

## Dataset Source

https://www.kaggle.com/datasets/adityakadiwal/water-potability

## Dataset Size

- Total Records: **3,276**
- Total Features: **9**
- Target Column: **Potability**

## Input Features

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

---

# Data Preprocessing Plan

The dataset will undergo the following preprocessing steps:

- Handle missing values
- Remove duplicate records
- Detect and treat outliers
- Scale numerical features using StandardScaler
- Split the dataset into training and testing sets

### Feature Engineering

The project will also include:

- Feature importance analysis
- Feature selection (if necessary)

---

# Exploratory Data Analysis (EDA)

The exploratory analysis will include:

- Dataset summary
- Missing value analysis
- Class distribution
- Feature distributions
- Histograms
- Boxplots
- Correlation heatmap
- Feature relationship analysis

---

# Machine Learning Models

The following machine learning models will be trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

The model with the best performance will be selected for deployment.

---

# Evaluation Plan

The models will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

Since correctly identifying unsafe drinking water is especially important, **F1-Score** will be used as the **primary evaluation metric** for selecting the best-performing model.

---

# Repository Plan

```text
water-potability-prediction/
│
├── dataset/
│   └── water_potability.csv
│
├── notebooks/
│   ├── eda.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   └── water_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Deployment Plan

The selected machine learning model will be saved using **Joblib** and deployed through a **Flask REST API**.

The API will receive water quality measurements as a JSON request and return the predicted water status, risk level, and recommendation.

## Example Request

```json
{
  "ph": 7.2,
  "hardness": 204,
  "solids": 18000,
  "chloramines": 7.5,
  "sulfate": 320,
  "conductivity": 410,
  "organic_carbon": 12,
  "trihalomethanes": 70,
  "turbidity": 3.5
}
```

## Example Response

```json
{
  "prediction": "Not Potable",
  "risk_level": "High",
  "recommendation": "This water is not recommended for drinking. Boil or treat the water before use and consider laboratory testing."
}
```

### Risk Level Strategy

The risk level will be determined using the model's prediction probability:

- **Low Risk** → High confidence that the water is potable.
- **Medium Risk** → Moderate prediction confidence; further testing is recommended.
- **High Risk** → High confidence that the water is unsafe for drinking.

### Recommendation Strategy

Recommendations will be generated using simple rule-based logic based on the predicted class and risk level rather than a separate machine learning model.

---

# Expected Outcome

The project will deliver an end-to-end machine learning application capable of predicting water potability using physicochemical measurements. The final solution will include data preprocessing, exploratory data analysis, feature engineering, model comparison, model evaluation, and deployment through a Flask REST API with a simple user interface. In addition to predicting whether water is safe for drinking, the application will provide a risk assessment and practical recommendations to support decision-making.