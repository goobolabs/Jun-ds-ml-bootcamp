# Assignment Four: Regression

## Part A Theory

## Introduction to Regression

### What is Regression in Machine Learning?
In machine learning, regression is a type of supervised learning.
The key objective of regression based tasks is to predict output labels or responses, which are continuous numeric values, for the given input data. The output will be based on what the model has learned in the training phase.

### How is it different from classification?
 Is about predicting a class or discrete values.

1. Example of Classification : Male or Female, True or False

2. Example of Regression: Price, Age, Salary

## Types of Regression
1. Linear Regression: is a statistical technique that estimates the linear relationship between a dependent and one or more independent variables.
2. Multiple linear Regression is basically the extension of simple linear regression that predicts a response using two or more features.
3. Polynomial Regression: Is a form of regression analysis in which relationship between the independent variable and dependent variable is modeled as a 3D.

|Linear regression|Multiple regression|Polynomial regression|Feature|
|------|------|------|------|
|Linear|Two or more|one or more polynomial|Number of dependent variable|
|Straight-line|linear|curved|Relationship|

## Underfitting and Overfitting
1. OverFitting: very well training data but poor testing.

2. UnderFitting: Both poorly Training data and Testing.

## What causes overfitting, especially in polynomial regression?
- In polynomial regression, overfitting is especially common because the model becomes more flexible as the polynomial degree increases.

- To prevent overfitting are:
1. Use lower degree polynomial.
2. Use cross validation.
3. Use Lasso or Ridge regression.

## Real-World Case Study
### Real-World Regression Project: House Price Prediction
One of the most common real-world applications of regression is house price prediction.

### Goal
The goal was to predict the selling price of houses based on different property features. This helps buyers, sellers, and real estate companies estimate fair market prices.

### Data Used
The dataset included features such as:
- House size (square feet)
- Number of bedrooms
- Number of bathrooms
- House age
- Location
- Garage size
The target variable was the house selling price.

### Type of Regression Applied
Multiple Linear Regression was used because the house price depends on multiple independent variables.

### Key Results / Insights
- Larger houses generally had higher prices.
- Location was one of the strongest factors affecting price.
- Houses with more bedrooms and bathrooms were usually more expensive.
- The model helped estimate house prices with good accuracy and supported better decision-making for buyers and sellers.

### REFERENCES
1. Xu, X. (2023). The Real Estate Price Prediction of US Based on Multi-Factorial Linear Regression Models. BCP Business & Management.
2. Abdulhafedh, A. (2022). Incorporating Multiple Linear Regression in Predicting the House Prices Using a Big Real Estate Dataset with 80 Independent Variables. Open Access Library Journal, 9, 1–21. https://doi.org/10.4236/oalib.1108346