# Final Project Proposal

**Date:** July 2026

---

# 1. Certificate Name

**Abdullahi Hassan Shire**

---

# 2. Project Title and Description

## Title

**Customer Purchase Amount Prediction Using Machine Learning**

## Description

Retail businesses collect customer shopping information to better understand purchasing behavior and improve business decisions. Predicting how much a customer is likely to spend helps companies personalize marketing campaigns, optimize inventory, and improve customer satisfaction.

This project aims to develop a machine learning model that predicts the **Purchase Amount (USD)** based on customer demographic information, shopping preferences, and purchasing history.

The best-performing model will be deployed using **FastAPI**, allowing users to submit customer information and receive a predicted purchase amount through a REST API.

---

# 3. Problem Type

## Regression (Supervised Learning)

The objective of this project is to predict the amount of money a customer is expected to spend.

### Output

* Purchase Amount (USD)

---

# 4. Dataset

## Source

**Customer Shopping Trends Dataset (Kaggle)**

https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset/data

## Dataset Size

* Approximately 3,900 customer records
* Multiple numerical and categorical features

## Target Column

`Purchase Amount (USD)`

## Main Features

* Age
* Gender
* Category
* Item Purchased
* Size
* Color
* Season
* Review Rating
* Subscription Status
* Previous Purchases
* Payment Method
* Shipping Type
* Discount Applied
* Promo Code Used
* Frequency of Purchases

## Preprocessing Plan

* Perform Exploratory Data Analysis (EDA)
* Remove duplicate records
* Handle missing values
* Encode categorical variables
* Scale numerical features
* Detect and handle outliers
* Perform feature selection
* Split the dataset into training and testing sets

---

# 5. Algorithms I Plan to Train

## Linear Regression

A simple baseline regression model for predicting purchase amount.

## Decision Tree Regressor

A non-linear regression algorithm capable of learning complex relationships.

## Random Forest Regressor

An ensemble model expected to provide the highest prediction accuracy.

---

# 6. Evaluation Plan

The following regression metrics will be used:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

The best model will be selected using the **highest R² Score** together with the **lowest MAE and RMSE**.

Three sanity checks will also be performed using sample customer records.

---

# 7. Deployment Sketch

## Backend

* FastAPI
* REST API
* Swagger Documentation (`/docs`)

## API Endpoint

### Purchase Prediction

```http
POST /predict
```

### Example Input

```json
{
  "Age": 29,
  "Gender": "Male",
  "Category": "Clothing",
  "Season": "Winter",
  "Review Rating": 4.5,
  "Previous Purchases": 12,
  "Subscription Status": "Yes"
}
```

### Example Output

```json
{
  "predicted_purchase_amount": 135.60
}
```

---

# 8. Repository Plan

```text
customer-purchase-prediction/
│
├── dataset/
│   ├── shopping_trends.csv
│   └── clean_shopping_data.csv
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
├── api/
│   └── app.py
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── requirements.txt
├── README.md
└── project_paper.md
```

## Planned Commands

```bash
python src/train.py

uvicorn api.app:app --reload
```

---

# 9. Expected Outcome

The project will produce a machine learning application capable of predicting customer purchase amounts with good accuracy. It will compare three regression algorithms, select the best-performing model, and deploy it through a FastAPI REST API. The completed project will demonstrate practical skills in data preprocessing, regression modeling, model evaluation, and API deployment.
