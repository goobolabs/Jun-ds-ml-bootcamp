# Flight Delay Prediction Using Machine Learning
# GitHub Repository:
https://github.com/fatima-moha143/fligh_delay_predict.git

## Student Information

**Student Name:** Fadumo mohamed omar 

**Project Title:** Flight Delay Prediction Using Machine Learning

**Project Type:** Classification Problem

**Programming Language:** Python

**Framework:** FastAPI

**Libraries:** Scikit-learn, Pandas, NumPy, Joblib, Jinja2



## Abstract

Flight delays are one of the biggest challenges in the aviation industry. They affect airline operations, increase operational costs, and reduce passenger satisfaction. This project presents a machine learning solution that predicts whether a flight will be **On-Time** or **Delayed** using historical flight information.

Three classification algorithms were trained and evaluated: Logistic Regression, Random Forest, and Gradient Boosting. After comparing their performance, the best model was deployed using FastAPI with a simple HTML and CSS web interface. The application allows users to enter flight information and instantly receive a prediction along with the model's confidence score.

---

# 1. Introduction

Machine learning has become an important technology for solving real-world problems across many industries. In aviation, predicting flight delays helps airlines improve scheduling, reduce operational costs, and provide better services to passengers.

The goal of this project is to develop an intelligent prediction system capable of classifying flights as either **On-Time** or **Delayed** based on historical flight information.

---

# 2. Problem Statement

Flight delays negatively impact airlines and passengers by increasing costs, disrupting schedules, and causing customer dissatisfaction. Manual prediction is difficult because many operational factors influence delays.

This project addresses this problem by developing a supervised machine learning model that predicts flight status before departure.

---

# 3. Objectives

The objectives of this project are:

- Analyze historical flight data.
- Clean and preprocess the dataset.
- Train multiple machine learning classification models.
- Compare model performance.
- Select the best-performing model.
- Deploy the final model using FastAPI.
- Develop an interactive web application for predictions.

---

# 4. Dataset Description

The project uses a Flight Delay dataset containing historical flight records.

## Dataset Summary

| Item | Value |
|------|------:|
| Rows | 539,382 |
| Features | 7 |
| Target | Class |

### Input Features

| Feature | Description |
|---------|-------------|
| Flight | Flight Number |
| Time | Departure Time |
| Length | Flight Duration |
| Airline | Airline Code |
| AirportFrom | Departure Airport |
| AirportTo | Arrival Airport |
| DayOfWeek | Day of Week |

### Target Variable

| Value | Meaning |
|------:|---------|
| 0 | On-Time |
| 1 | Delayed |

---

# 5. Data Preprocessing

Before training the models, several preprocessing steps were performed:

- Dataset inspection
- Duplicate removal
- Missing value checking
- One-Hot Encoding for categorical features
- Feature scaling using StandardScaler
- Saving preprocessing artifacts for deployment

These preprocessing steps ensured consistency between training and prediction.

# 6. Machine Learning Models

Three classification algorithms were trained and evaluated.

## Logistic Regression

Logistic Regression was used as the baseline classifier because it is simple, fast, and easy to interpret.

## Random Forest

Random Forest combines multiple decision trees to improve prediction accuracy. It demonstrated the best overall performance in this project.

## Gradient Boosting

Gradient Boosting builds trees sequentially by correcting previous prediction errors. It achieved competitive performance but was slightly lower than Random Forest.

---

# 7. Model Evaluation

The models were evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score

## Model Comparison

| Model | Description |
|--------|-------------|
| Logistic Regression | Baseline model |
| Random Forest | Best performing model |
| Gradient Boosting | High-performance boosting model |

Random Forest achieved the highest overall performance and was selected for deployment.

---

# 8. Deployment

The selected model was deployed using **FastAPI**.

The web application was developed using:

- HTML
- CSS
- FastAPI
- Scikit-learn
- Joblib

Users enter flight information through a simple interface, and the system predicts whether the flight will be **On-Time** or **Delayed**, together with the confidence score.

---

# 9. Challenges

During development, several challenges were encountered:

- Preparing categorical variables for prediction.
- Keeping training and prediction features consistent.
- Integrating FastAPI with the HTML interface.
- Loading the trained machine learning model correctly.

These challenges were solved by implementing a reusable preprocessing pipeline and saving the trained preprocessing objects.

---

# 10. Conclusion

This project successfully demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and deployment.

Three machine learning algorithms were compared, with **Random Forest** selected as the best-performing model.

The deployed FastAPI application provides a simple and effective way for users to predict whether a flight is likely to be **On-Time** or **Delayed**.

This project highlights the practical application of machine learning in solving real-world aviation problems.

---

