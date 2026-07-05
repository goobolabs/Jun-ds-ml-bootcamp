# Machine Learning Regression Report

---

# 1. Introduction to Regression in Machine Learning

## What is Regression?
Regression is a supervised machine learning technique used to predict **continuous numerical values**. It finds relationships between input variables (features) and a continuous output variable (target).

Example: predicting house prices based on size and location.

---

## Difference Between Regression and Classification

- **Regression:** predicts continuous values (e.g., 250,000 USD)
- **Classification:** predicts categories (e.g., spam or not spam)

---

## Real-Life Examples

- **Regression example:** Predicting house prices
- **Classification example:** Predicting disease (Yes/No)

---

# 2. Types of Regression

---

## 2.1 Linear Regression

### Definition
Linear regression models the relationship between one input and output using a straight line:

y = mx + b

### How it works
It finds the best-fitting line that minimizes prediction errors.

### Use Case
Predicting salary based on years of experience.

### Advantages
- Simple and fast
- Easy to interpret
- Works well for linear relationships

### Limitations
- Cannot model complex relationships
- Sensitive to outliers

---

## 2.2 Multiple Linear Regression

### Definition
Uses multiple input variables to predict one output:

y = b0 + b1x1 + b2x2 + ... + bnxn

### How it works
Each feature contributes with a weight to the final prediction.

### Use Case
Predicting house price using size, rooms, and location.

### Advantages
- More accurate than simple linear regression
- Handles multiple features

### Limitations
- Multicollinearity problem
- Still assumes linear relationships

---

## 2.3 Polynomial Regression

### Definition
Models non-linear relationships using powers of variables:

y = b0 + b1x + b2x² + b3x³ + ...

### How it works
Transforms input into polynomial features to fit curved patterns.

### Use Case
Predicting population growth or sales trends.

### Advantages
- Captures non-linear patterns
- Flexible model

### Limitations
- High risk of overfitting
- Complex with high degrees

---

# 3. Regression Metrics

---

## 3.1 MAE (Mean Absolute Error)
Measures the average absolute difference between actual and predicted values.

- Simple interpretation
- Ignores direction of error

---

## 3.2 MSE (Mean Squared Error)
Measures squared differences between actual and predicted values.

- Penalizes large errors heavily
- Sensitive to outliers

---

## 3.3 RMSE (Root Mean Squared Error)
Square root of MSE.

- Same unit as target variable
- Easier to interpret than MSE

---

## 3.4 R² (Coefficient of Determination)
Measures how well the model explains variance in data.

- Range: 0 to 1 (sometimes negative)
- Higher = better model fit

---

## Comparison Table

| Metric | Unit | Large Error Sensitivity | Meaning |
|--------|------|------------------------|---------|
| MAE | Same as data | Low | Average absolute error |
| MSE | Squared units | High | Penalizes big errors |
| RMSE | Same as data | High | Standard error size |
| R² | None | N/A | Model explanation power |

---

# 4. Underfitting and Overfitting

---

## Underfitting
Occurs when the model is too simple and fails to capture patterns.

- High error on training and test data
- Example: straight line for curved data

---

## Overfitting
Occurs when the model learns noise instead of real patterns.

- Very good training performance
- Poor generalization on new data

### Why it happens (especially polynomial regression)
- Very high polynomial degree
- Too much model flexibility
- Noise is learned as pattern

---

## How to Prevent Overfitting

- Reduce model complexity
- Use regularization (L1, L2)
- Apply cross-validation
- Increase training data

---

# 5. Real-World Case Study: House Price Prediction

---

## Goal
Predict house prices based on property features.

---

## Data Used
- House size
- Number of rooms
- Location
- Age of property
- Historical prices

---

## Model Used
Multiple Linear Regression

---

## Results and Insights
- House size strongly affects price
- Location is a key factor
- Data cleaning improves accuracy
- Outliers reduce performance if not handled

---

# Conclusion
Regression is a powerful method for predicting continuous values. Different regression models are used depending on data complexity. Evaluation metrics like MAE, MSE, RMSE, and R² help measure performance. Understanding overfitting and underfitting is important for building reliable machine learning models.