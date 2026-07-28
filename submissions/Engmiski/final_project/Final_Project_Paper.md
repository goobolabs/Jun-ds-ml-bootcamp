# Laptop Price Prediction Using Machine Learning

## Final Project Report

**Student Name: Miski Mohamed Nur  

---

# Abstract

Laptop prices are affected by many hardware specifications such as processor type, RAM capacity, storage capacity, graphics card, screen size, weight, and brand. Because the laptop market contains thousands of models with different configurations, predicting the correct price manually can be challenging.

This project develops a machine learning regression system that predicts laptop prices based on hardware specifications. Four regression algorithms were implemented and compared: Linear Regression, Random Forest Regressor, CatBoost Regressor, and XGBoost Regressor.

The models were evaluated using R² Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE). The experimental results showed that XGBoost Regressor achieved the best performance with an R² Score of 0.834, MAE of 96.84, and RMSE of 165.48.

The selected model was deployed using Flask framework to create a web-based prediction system. The application allows users to enter laptop specifications and receive estimated prices instantly through a user-friendly interface and REST API.

---

# 1. Introduction

## 1.1 Background

The laptop industry provides a wide range of devices with different specifications, brands, and price categories. Laptop prices depend on several important factors including processor performance, RAM size, storage technology, graphics capability, display size, and manufacturer.

For customers, choosing a laptop with a reasonable price can be difficult because comparing different specifications requires technical knowledge and time.

Machine learning provides an effective approach by learning patterns from historical laptop data and using these patterns to predict future prices.

---

## 1.2 Problem Statement

Determining the correct price of a laptop based only on specifications is a complex problem because multiple hardware features affect the final market price.

This project aims to develop a machine learning model capable of automatically predicting laptop prices using hardware specifications as input.

---

## 1.3 Project Objectives

The main objectives of this project are:

- Collect and prepare laptop price data.
- Perform data cleaning and preprocessing.
- Apply feature engineering techniques.
- Train different machine learning regression models.
- Compare model performance.
- Select the best-performing model.
- Deploy the final model using Flask.
- Create a user-friendly prediction application.

---

# 2. Dataset Description

## 2.1 Dataset Source

The dataset used in this project is the Laptop Price Prediction Dataset obtained from Kaggle.

Dataset Source:

 https://www.kaggle.com/datasets/eslamelsolya/laptop-price-prediction


## 2.2 Dataset Information

The dataset contains:

- Approximately 1,300 laptop records.
- 8 input features.
- 1 target variable.

---

## 2.3 Features Description

| Feature | Description |
|---|---|
| Company | Laptop manufacturer |
| TypeName | Laptop category |
| Screen Size | Display size in inches |
| CPU | Processor specification |
| RAM | Installed memory |
| Memory | Storage configuration |
| GPU | Graphics card |
| Weight | Laptop weight |

---

## 2.4 Target Variable

The target variable is:

**Price**

Since the price value is numerical and continuous, this project is considered a supervised regression problem.

---

# 3. Data Preprocessing

Before training the machine learning models, several preprocessing steps were performed.

## 3.1 Data Cleaning

The following operations were applied:

- Removed unnecessary columns.
- Checked missing values.
- Removed duplicate records.
- Converted data into suitable formats.

---

## 3.2 Feature Engineering

Machine learning algorithms require numerical data, therefore categorical variables were transformed.

Categorical features:

- Company
- TypeName
- CPU
- Memory
- GPU

Numerical features:

- Screen Size
- Weight

---

## 3.3 Train-Test Split

The dataset was divided into two parts:

| Dataset | Percentage |
|---|---:|
| Training Data | 80% |
| Testing Data | 20% |

The same split was used for all models to ensure a fair comparison.

---

# 4. Machine Learning Algorithms

Four regression algorithms were implemented.

---


## 4.1 Random Forest Regressor

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy.

### Advantages:

- Handles nonlinear relationships.
- Reduces overfitting.
- Provides reliable predictions.

---

## 4.2 CatBoost Regressor

CatBoost is a gradient boosting algorithm designed to handle categorical features effectively.

### Advantages:

- Works well with categorical data.
- Provides high prediction accuracy.
- Requires less preprocessing.

---

## 4.3 XGBoost Regressor

XGBoost is an advanced gradient boosting algorithm widely used for machine learning regression tasks.

### Advantages:

- High predictive performance.
- Handles complex patterns.
- Includes regularization techniques.
- Efficient training.

---

# 5. Model Evaluation

The models were evaluated using three evaluation metrics.

---

## 5.1 R² Score

R² Score measures how well the model explains the variation in laptop prices.

Higher values indicate better performance.

---

## 5.2 Mean Absolute Error (MAE)

MAE measures the average difference between predicted and actual prices.

Lower values indicate better accuracy.

---

## 5.3 Root Mean Squared Error (RMSE)

RMSE measures the size of prediction errors.

Lower values indicate better model performance.

---

# 6. Model Comparison Results

| Model | R² Score | MAE | RMSE |
|---|---:|---:|---:|
| Random Forest Regressor | 0.828 | 98.46 | 168.16 |
| CatBoost Regressor | 0.832 | 102.34 | 166.24 |
| XGBoost Regressor | **0.834** | **96.84** | **165.48** |

---

# 7. Best Model Selection

Based on the evaluation results, XGBoost Regressor achieved the best performance.

Performance:

- R² Score: 0.834
- MAE: 96.84
- RMSE: 165.48


XGBoost was selected as the final model because it provided:

- Highest prediction accuracy.
- Lowest prediction error.
- Better ability to learn complex relationships between laptop specifications and prices.

---

# 8. Model Testing

Additional tests were performed to verify that the model produces realistic predictions.

---

## Test Case 1

Laptop Configuration:

- Company: Apple
- Type: Ultrabook
- Screen Size: 13.3 inches
- CPU: Intel Core i5
- RAM: 8GB
- Memory: 256GB SSD
- GPU: Intel Iris Graphics
- Weight: 1.37kg


Result:

The model generated a reasonable price prediction compared with similar laptops.

---

## Test Case 2

Laptop Configuration:

- Company: Dell
- Type: Notebook
- Screen Size: 15.6 inches
- CPU: Intel Core i7
- RAM: 16GB
- Memory: 512GB SSD
- GPU: NVIDIA GTX 1650
- Weight: 2.10kg


Result:

The prediction was consistent with laptops having similar specifications.

---

## Test Case 3

Laptop Configuration:

- Company: ASUS
- Type: Gaming
- Screen Size: 17.3 inches
- CPU: AMD Ryzen 7
- RAM: 16GB
- Memory: 1TB HDD + 256GB SSD
- GPU: AMD Radeon RX 580
- Weight: 3.20kg


Result:

The model predicted a higher price because of the powerful gaming hardware.

---

# 9. Deployment Using Flask

The final XGBoost model was deployed using Flask framework.

The application consists of:

- Frontend web interface.
- Flask backend.
- Trained machine learning model.
- Prediction API.

Users can enter laptop specifications through the web interface and receive an estimated price instantly.

---

# 9.1 REST API

The system provides a REST API endpoint:

The API receives laptop specifications as input and returns the predicted laptop price.

Example Input:

```json
{
"Company":"Dell",
"TypeName":"Notebook",
"ScreenSize":15.6,
"CPU":"Intel Core i7",
"RAM":"16GB",
"Memory":"512GB SSD",
"GPU":"NVIDIA GTX 1650",
"Weight":"2.10kg"
}
{
"Predicted Price":881
}
10. Conclusion

This project successfully developed a machine learning system for predicting laptop prices based on hardware specifications.

Four regression algorithms were trained and evaluated. The results showed that XGBoost Regressor achieved the best performance compared with other models.

The final model was deployed using Flask, providing a simple web application and REST API that allow users to estimate laptop prices easily.

This project demonstrates that machine learning can be effectively used for price prediction and decision support systems.

# 10 Reference
github linkg https://github.com/Engmiski/Laptop-Price-Prediction-ML

local link http://127.0.0.1:5000
