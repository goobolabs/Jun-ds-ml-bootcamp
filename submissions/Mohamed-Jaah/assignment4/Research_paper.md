# Assignment Four, Part A: Regression — Theory

**Course:** Machine Learning
**Date:** June 30, 2026

---

## 1. Introduction to Regression

### 1.1 What is Regression in Machine Learning?

Regression is a category of supervised learning in which a model learns to predict a continuous numerical value from a set of input features. Given a training dataset of input-output pairs, a regression algorithm tries to find the mathematical relationship between the independent variables (features) and the dependent variable (target) so that, when given new, unseen inputs, it can output a reasonable numeric estimate. For example, in the rainfall dataset used for the practical part of this assignment, a regression model learns the relationship between atmospheric features (temperature, humidity, pressure, wind speed, and similar measurements) and the actual amount of rainfall recorded in millimeters, so that it can later estimate rainfall for days it has never seen.

### 1.2 How is Regression Different from Classification?

Both regression and classification are supervised learning tasks, meaning both rely on labeled training data. The key difference lies in the nature of the output variable. Regression predicts a continuous quantity that can take any numerical value within a range, such as 12.4 mm of rain or 87.9 mm of rain. Classification, on the other hand, predicts a discrete category or class label from a finite, predefined set of possibilities, such as "Rainy" or "Drought," or "Spam" versus "Not Spam." Because the output types differ, the two tasks also use different evaluation metrics: regression relies on error-based metrics such as MAE and RMSE, while classification relies on metrics such as accuracy, precision, and recall.

### 1.3 Real-Life Examples

A real-life example of regression is predicting the daily rainfall amount in millimeters for a given location based on weather features such as humidity, temperature, and atmospheric pressure, which is exactly the task performed in the practical part of this assignment. A real-life example of classification is predicting whether a given day will be classified as "Rainy" or "Drought" based on the same kind of weather features; here the output is a category rather than a number.

---

## 2. Types of Regression

### 2.1 Linear Regression

Linear regression models the relationship between a single independent variable and the dependent variable as a straight line. It assumes that the target value can be approximated by multiplying the input feature by a coefficient (weight) and adding a constant (intercept). The model is trained by finding the line that minimizes the overall squared distance between the predicted values and the actual values, a method known as least squares.

- **How it works:** It fits the equation y = b0 + b1x by adjusting b0 and b1 so that the predicted line is as close as possible to all the data points.
- **Real-world use case:** Estimating a person's salary based solely on years of work experience.
- **Advantages:** Simple, fast to train, easy to interpret, and works well when the relationship between variables is approximately linear.
- **Limitations:** Cannot capture more complex or curved relationships, and it is sensitive to outliers since it tries to minimize squared error across all points.

### 2.2 Multiple Linear Regression

Multiple linear regression extends simple linear regression to situations where more than one independent variable influences the target. Instead of a single coefficient, the model learns a separate coefficient for each input feature, allowing it to capture the combined effect of several factors at once. This is the technique used directly in the rainfall prediction script for this assignment, since rainfall amount depends on several weather features simultaneously rather than just one.

- **How it works:** It fits the equation y = b0 + b1x1 + b2x2 + ... + bnxn, where each xi is a different feature and each bi is its learned weight.
- **Real-world use case:** Predicting house prices based on multiple factors such as square footage, number of bedrooms, location, and age of the property.
- **Advantages:** Captures the joint effect of multiple factors, generally more accurate than simple linear regression for real-world problems, and still relatively interpretable since each coefficient shows the effect of one feature.
- **Limitations:** Performance degrades when features are highly correlated with each other (multicollinearity), and it still cannot model non-linear relationships well.

### 2.3 Polynomial Regression

Polynomial regression is an extension of linear regression that models non-linear relationships by raising the input features to higher powers (squares, cubes, and so on) before fitting a linear model to those transformed features. Even though the relationship between the transformed features and the target is still linear in terms of the coefficients, the resulting curve can bend and flex to fit more complex patterns in the data.

- **How it works:** It fits an equation such as y = b0 + b1x + b2x^2 + b3x^3 + ..., adding higher-degree terms of the same feature so the model can represent curves instead of only straight lines.
- **Real-world use case:** Modeling the growth rate of a population or the trajectory of a thrown object, both of which follow curved rather than straight-line patterns.
- **Advantages:** Can model curved, non-linear relationships that simple and multiple linear regression cannot capture.
- **Limitations:** Choosing too high a degree easily leads to overfitting, where the model fits the noise in the training data rather than the underlying trend; it is also more sensitive to outliers at the extremes of the data range.

### 2.4 Comparison Summary

Linear regression is the simplest and works only when there is roughly one dominant linear relationship. Multiple linear regression builds on this by incorporating several predictors at once, which is closer to most real-world problems. Polynomial regression goes a step further by allowing curvature, at the cost of higher complexity and a greater risk of overfitting if not carefully controlled.

---

## 3. Regression Metrics

To judge whether a regression model is performing well, several numerical metrics are used to quantify the difference between the predicted values and the true values.

- **MAE (Mean Absolute Error):** The average of the absolute differences between predicted and actual values. It tells us, on average, how far off the predictions are in the same unit as the target variable, without exaggerating the effect of any single large error.
- **MSE (Mean Squared Error):** The average of the squared differences between predicted and actual values. Because the errors are squared before averaging, larger errors are penalized much more heavily than smaller ones, making MSE more sensitive to outliers than MAE.
- **RMSE (Root Mean Squared Error):** The square root of MSE. Taking the square root brings the metric back into the same unit as the original target variable (for example, millimeters of rainfall), which makes it easier to interpret than MSE while still penalizing large errors more than MAE does.
- **R² (Coefficient of Determination):** A measure of how much of the variance in the target variable is explained by the model, expressed as a value typically between 0 and 1 (it can be negative for a very poor model). An R² of 1 means the model perfectly explains all the variation in the data, while an R² of 0 means the model explains none of it, performing no better than simply predicting the average value every time.

### 3.1 Comparison Table

| Metric | Unit | Sensitivity to Large Errors | What It Measures |
|---|---|---|---|
| MAE | Same as target variable | Low — treats all errors proportionally | Average magnitude of prediction error |
| MSE | Square of target variable's unit | High — squaring amplifies large errors | Average squared prediction error |
| RMSE | Same as target variable | High — inherits MSE's sensitivity, but interpretable in original units | Typical size of prediction error, in original units |
| R² | Unitless (ratio/proportion) | Moderate — large errors reduce explained variance | Proportion of variance in the target explained by the model |

---

## 4. Underfitting and Overfitting

**Underfitting** occurs when a model is too simple to capture the underlying pattern in the data. An underfit model performs poorly on both the training data and new, unseen data, because it has not learned enough about the relationship between the features and the target. For example, trying to fit a straight line to data that clearly follows a curve would result in underfitting.

**Overfitting** occurs when a model is too complex relative to the amount or simplicity of the data, causing it to learn not only the genuine underlying pattern but also the random noise present in the training set. An overfit model performs very well on the training data but poorly on new, unseen data, because it has essentially memorized the training examples rather than learning a generalizable trend.

**Causes of overfitting in polynomial regression:** Polynomial regression is particularly prone to overfitting because increasing the degree of the polynomial gives the model more flexibility to bend and twist the fitted curve. At very high degrees, the curve can pass extremely close to every individual training point, including the noise, instead of representing the smooth underlying trend. This problem becomes worse when the training dataset is small, since there are fewer points to constrain the shape of the curve.

**Methods to prevent overfitting:**

1. **Limit model complexity** — for polynomial regression, choose a lower degree, and for tree-based models such as Random Forest, limit the maximum depth of each tree (as is done in the practical script with `max_depth=12`).
2. **Use regularization** — techniques such as Ridge (L2) or Lasso (L1) regression add a penalty term that discourages the model from assigning excessively large weights to any single feature.
3. **Use cross-validation and a held-out test set** — splitting the data into training and testing sets, as done in the practical part of this assignment, allows the model's performance to be checked on data it has not seen, which reveals overfitting that would otherwise be hidden if only training accuracy were examined.

---

## 5. Real-World Case Study

A relevant real-world case study is research on rainfall and daily average temperature prediction conducted using machine learning techniques applied to a Bangladesh weather dataset. The goal of the study was to predict both the occurrence of rainfall and the amount of rainfall, since accurate rainfall forecasting is critical in agriculture-dependent economies such as Bangladesh, where unpredictable rainfall can directly affect food security and disaster preparedness.

The researchers used a weather dataset containing historical meteorological observations and applied several regression algorithms, including Linear Regression, Random Forest, and Support Vector Regression, alongside an ensemble regression approach that combined multiple models together. The study found that an ensemble regression approach outperformed individual Linear Regression, Random Forest, and Support Vector Regression models for predicting rainfall amounts, achieving the lowest mean absolute error and root mean squared error among the methods tested.

This case study is directly relevant to the practical part of this assignment, since it follows the same overall approach: using regression algorithms, including Linear Regression and Random Forest, to predict a continuous weather-related quantity (rainfall amount) and comparing the models using MAE and RMSE. The key insight from this research is that combining multiple regression models (an ensemble approach) tends to produce more accurate and reliable rainfall predictions than relying on any single algorithm alone, since different models tend to make different kinds of errors that can partially cancel out when combined.

---

## References

- Preprints.org. (2024). *Rainfall and Daily Average Temperature Prediction using Machine Learning: A Case Study of Bangladesh.* Retrieved from https://www.preprints.org/manuscript/202402.1566/v1
- Course materials and lecture notes, Machine Learning module, Regression unit.
- Scikit-learn documentation, regression and metrics modules.
