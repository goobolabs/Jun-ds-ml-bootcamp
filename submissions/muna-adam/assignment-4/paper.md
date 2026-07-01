# Introduction to Regration

## What is Regression in Machine Learning?

Regression is a type of Machine Learning used to predict continuous numerical values, not categories. It is commonly used to estimate values such as house prices, weather temperature, age, or sales.

## Difference Between Regression and Classification

| Regression | Classification |
|------------|----------------|
| Predicts a numerical value | Predicts a category or class |
| Output is continuous | Output is discrete |
| Example: House Price = $200,000 | Example: Email = Spam or Not Spam |

## Real-Life Example of Regression

### House Price Prediction
Suppose we know the following information about a house:

•	House size = 1,800 square feet
•	Number of bedrooms = 3
•	Location = City center

The machine learning model predicts:

House Price = $250,000

Since the output is a numerical value, this is an example of Regression.

## Real-Life Example of Classification
Bitcoin (BTC) Price Direction Prediction

A machine learning model predicts whether the price of Bitcoin will:
•	Go Up (UP)
•	Go Down (DOWN)

The output is a category rather than a number, so this is an example of Classification.

# Types of Regression

## Linear Regression

Linear Regression makes predictions using one input feature and one output variable. Because it uses only one feature, the model may not always produce the most accurate predictions, especially when many factors affect the result.

## Multiple Linear Regression

Multiple Linear Regression uses two or more input features to predict one output variable. Since it considers multiple factors, it usually provides more accurate predictions than Linear Regression when the target depends on several features.

## Polynomial Regression 

is used when the relationship between the input and the output is not a straight line. It fits a curved line to the data, making it useful for predicting values when the data follows a curve instead of a linear pattern.


1.  MAE calculates the average difference between the predicted values and the actual values.
2.	MSE: For example, if the errors are 2, 2, and 8, it squares each value.
3.	RMSE takes the square root of the MSE.
4.	R² shows the percentage of the dataset that the model has learned. If the R² value is 0.3, it means the model is not good. If the R² value is 0.9, it means the model has learned the dataset well.

| Metric | Unit | Sensitivity to Large Errors | Meaning |
|--------|------|-----------------------------|---------|
| MAE | Same as the target variable | Low | Measures the average difference between predicted and actual values. |
| MSE | Squared unit of the target variable | High | Measures the average of the squared errors. Large errors have a bigger impact. |
| RMSE | Same as the target variable | High | Measures the average prediction error by taking the square root of MSE. |
| R² | No unit (0 to 1) | Not based on error size | Shows how well the model fits the data. A value closer to **1** means a better mode
# Underfitting and Overfitting

## Underfitting 
happens when the model is not trained well on the dataset, so its accuray is low.

## Overfiting 

is different because the model memorizes everything in the dataset, even unnecessary information or noise. However, when new data is given, it cannot make accurate predictions.

What causes overfitting, especially in Polynomial Regression?
Polynomial Regression uses a curved line.

If you use a very high polynomial degree (for example, degree 10 or 15), the curve tries to fit all the data points.
This causes:
•	The model to learn the noise.
•	The model to become too complex.
•	The model to perform poorly on new data.

## Methods to prevent overfitting

1. Use a lower polynomial degree
Do not use a very high polynomial degree.

3. Use more training data
When the dataset is larger, the model learns the correct pattern instead of the noise.

4. Remove unnecessary features
Do not include unnecessary featres.

Too many unimportant features can increase overfitting.

## Real-World Case Study

House Price Prediction Using Multiple Linear Regresion

### Goal

The goal of the study was to predict house prices accurately based on different house features. This helps buyers, sellers, and real estate companies make better decisions.

## DataUsed

The researchers used a dataset from Kaggle containing 3,553 houses with 11 features, including:
•	House size
•	Number of bedrooms
•	Number of bathrooms
•	Location
•	Other house characteristics

## Type of Regression Applied

The study used Multiple Linear Regression because it used several input features to predict one output value (house price).
Key Results and Insights.

The model achieved about 85% accuracy. The study found that house features such as size, location, and the number of rooms had a strong effect on house prices. The results showed that Multiple Linear Regression can be used to predict house prices with good accuracy.
https://jurnal.kaputama.ac.id/index.php/JIK/article/view/135?utm_source=chatgpt.com
