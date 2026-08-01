# Student Name: Miski Mohamed Nur  

# Laptop Price Prediction Using Machine Learning Regression Algorithms and Flask Deployment

## Abstract

The increasing demand for laptops has created a challenge for customers when selecting devices with suitable specifications and reasonable prices. Laptop prices depend on various factors such as brand, processor, RAM, storage, graphics card, display, and operating system. This project presents a machine learning-based laptop price prediction system that estimates laptop prices using regression algorithms.

In this research, three machine learning regression models were implemented: Linear Regression, Random Forest Regression, and XGBoost Regression. The dataset was processed through data cleaning, feature transformation, and encoding of categorical attributes. The trained models were evaluated using regression performance metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.

The best-performing model was integrated into a Flask web application to provide real-time laptop price predictions. Users can enter laptop specifications through a web interface and receive an estimated price instantly. The developed system demonstrates how machine learning can be applied to improve price estimation and support purchasing decisions in the electronics market.

**Keywords:** Machine Learning, Laptop Price Prediction, Regression Algorithms, Random Forest, XGBoost, Flask Deployment.

---

# 1. Introduction

The laptop market contains a wide range of products with different specifications and prices. The price of a laptop is influenced by many technical features, making it difficult for customers to determine the actual value of a device. Traditional methods require manual comparison of specifications, which can be time-consuming and sometimes inaccurate.

Machine learning provides an efficient solution by analyzing historical data and identifying relationships between laptop specifications and prices. Regression algorithms are particularly suitable for predicting continuous values such as product prices.

This project develops a laptop price prediction system using multiple regression algorithms and deploys the final model as a Flask-based web application. The system provides users with an automated method for estimating laptop prices based on their selected specifications.

---

# 2. Objectives

The main objectives of this project are:

* To collect and analyze laptop specification data.
* To preprocess and prepare data for machine learning.
* To train regression models for laptop price prediction.
* To compare different regression algorithms.
* To evaluate model accuracy and performance.
* To deploy the prediction model using Flask.
* To create an interactive interface for users.

---

# 3. Dataset Description

The dataset used in this project contains information about different laptop models and their specifications. The main features include:

| Feature          | Description               |
| ---------------- | ------------------------- |
| Brand            | Laptop manufacturer       |
| Processor        | CPU information           |
| RAM              | Memory capacity           |
| Storage          | SSD/HDD capacity          |
| GPU              | Graphics processing unit  |


| Price            | Target prediction value   |

The target variable of the system is the laptop price.

---

# 4. Methodology

The project follows a complete machine learning workflow:

1. Data collection
2. Data preprocessing
3. Feature engineering
4. Model training
5. Model evaluation
6. Model deployment

The raw dataset is cleaned by removing unnecessary values, handling missing data, and converting categorical features into numerical formats suitable for machine learning algorithms.

---

# 5. Machine Learning Models

## 5.1 Linear Regression

Linear Regression is a basic supervised learning algorithm that predicts the relationship between input features and laptop price. It provides a simple and interpretable approach for price prediction.

## 5.2 Random Forest Regression

Random Forest Regression is an ensemble learning method that combines multiple decision trees to improve prediction accuracy. It can handle complex relationships between laptop features and prices.

## 5.3 XGBoost Regression

XGBoost is a powerful gradient boosting algorithm that improves prediction performance by combining multiple weak learners. It is widely used for structured data prediction problems because of its accuracy and efficiency.

---

# 6. System Implementation

The project was implemented using Python and Flask.

The system structure includes:

```
FINAL-PROJ-DS-ML/

Dataset/

frontend/
    templates/
        index.html

    static/
        style.css
        js/script.js

models/
    linear_regression_model.pkl
    random_forest_model.pkl
    xgboost_model.pkl

app.py
train.py
predict.py
processing.py
requirements.txt
```

The trained models are saved as `.pkl` files and loaded by the Flask application during prediction.

---

# 7. Flask Web Application

The Flask application provides a simple interface where users enter laptop specifications. The entered information is processed and passed to the trained machine learning model.

The prediction process follows:

```
User Input
     |
     ↓
Flask Application
     |
     ↓
Data Processing
     |
     ↓
Machine Learning Model
     |
     ↓
Predicted Laptop Price
```

---

# 8. Model Evaluation

The performance of the regression models is evaluated using:

### Mean Absolute Error (MAE)

Measures the average difference between actual and predicted prices.

### Root Mean Squared Error (RMSE)

Measures the prediction error while giving more importance to large errors.

### R² Score

Measures how well the model explains variations in laptop prices.

Based on experiments, ensemble models such as Random Forest and XGBoost generally achieve better performance because they can capture complex relationships between laptop specifications.

---

# 9. Results and Discussion

The developed system successfully predicts laptop prices using machine learning regression techniques. Linear Regression provides a basic prediction capability, while Random Forest and XGBoost provide improved accuracy due to their ability to learn complex patterns.

The deployment of the model through Flask makes the system practical and accessible. Users can interact with the prediction system without requiring technical knowledge about machine learning.

---

# 10. Conclusion

This research developed an automated laptop price prediction system using machine learning regression algorithms. The project demonstrated the complete machine learning lifecycle, including data preprocessing, model training, evaluation, and deployment.

The results show that machine learning techniques can effectively estimate laptop prices based on hardware specifications. The Flask web application provides an easy-to-use platform for real-time price prediction.

---

# 11. Future Improvements

Future development of this project can include:

* Real-time laptop price collection from online stores.
* Integration with e-commerce platforms.
* Development of a mobile application.
* Use of deep learning algorithms.
* Automatic model updating with new market data.

---

# References

1. Breiman, L. (2001). Random Forests. Machine Learning Journal.

2. Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System.

3. Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python.

4. Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning.

 githublink   https://github.com/Engmiski/laptop-price-prediction-model