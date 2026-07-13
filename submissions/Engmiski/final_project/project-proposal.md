# Final Project Proposal

## 1. Certificate Name

**Your Full Name:** ___Miski mohamed Nur___________________

---

## 2. Project Title and Description

### **Title**

**Laptop Price Prediction Using Machine Learning**

### **Description**

This project aims to develop a machine learning regression model that predicts the price of a laptop based on its hardware specifications and brand information. The model will use features such as the laptop company, type, screen size, processor, RAM, storage, graphics card, and weight to estimate the selling price. The system is designed to help buyers estimate fair laptop prices and assist sellers in making competitive pricing decisions. The final application will be deployed using **Flask**, allowing users to obtain laptop price predictions through a simple web interface and REST API.

---

## 3. Problem Type

**Regression**

Since the target variable (**Price**) is a continuous numerical value, this project is a supervised machine learning regression problem.

---

## 4. Dataset

**Source:** Kaggle – Laptop Price Prediction Dataset 
https://www.kaggle.com/datasets/eslamelsolya/laptop-price-prediction

**Dataset Size:** Approximately **1,300** laptop records

**Target Variable:**

* Price

**Input Features:**

* Company
* TypeName
*screen size
* Cpu
* Ram
* Memory
* Gpu
* Weight

---

## 5. Algorithms

The following machine learning regression algorithms will be trained and compared:

* Random Forest Regressor
* XGBoost Regressor
* CatBoost Regressor
* Linear regration


The best-performing model will be selected based on evaluation metrics.

---

## 6. Evaluation Plan

The models will be evaluated using the following metrics:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Root Mean Squared Error (RMSE)**

The final model will be selected based on the **highest R² Score** and the **lowest MAE and RMSE**.

---

## 7. Deployment Sketch

The trained model will be deployed using **Flask**.

A Flask application will provide a **`/predict`** endpoint that accepts the following JSON input:

* Company
* TypeName
* screen size
* Cpu
* Ram
* Memory
* Gpu
* Weight

The API will return the predicted laptop price in JSON format.

---

## 8. Repository Plan

```text
Laptop-Price-Prediction/
│
├── dataset/
├── notebooks/
├── src/
├── api/
│   └── app.py
├── models/
├── templates/
│   └── index.html
├── static/
├── README.md
└── project_paper.md
```
