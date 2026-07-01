Assignment Four: Regression — Theory and Practice (Part A)

1. Introduction to Regression

What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values based on one or more input variables. The model learns the relationship between the input features (independent variables) and the target variable (dependent variable) using historical data. Once trained, the model can estimate the value of the target for new, unseen data.

Regression is widely used in many industries because it helps organizations make predictions, identify trends, and support decision-making. Examples include predicting house prices, sales revenue, fuel consumption, and stock prices.

Difference Between Regression and Classification

Although both regression and classification are supervised learning techniques, they solve different types of problems.

Regression predicts continuous numerical values, while classification predicts discrete categories or class labels. For example, regression may predict the selling price of a car, whereas classification may determine whether an email is spam or not spam.

Another important difference is the evaluation metrics. Regression models are commonly evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the Coefficient of Determination (R²). Classification models are evaluated using metrics such as Accuracy, Precision, Recall, and F1-score.

Real-Life Examples

Regression Example: Predicting the market price of a used car based on mileage, age, number of accidents, and location.

Classification Example: Determining whether a bank customer will default on a loan (Yes or No).

---

2. Types of Regression

Linear Regression

Linear Regression is the simplest regression algorithm. It assumes a straight-line relationship between one independent variable and one dependent variable. The model finds the best-fitting line that minimizes prediction errors.

Real-World Use Case

A company can use Linear Regression to predict monthly electricity consumption based on average temperature.

Advantages

- Simple to understand and implement.
- Fast to train.
- Easy to interpret.

Limitations

- Assumes a linear relationship.
- Sensitive to outliers.
- Cannot model complex patterns.

---

Multiple Linear Regression

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict a single target variable.

Instead of using only one feature, the model combines several features to improve prediction accuracy.

Real-World Use Case

Predicting car prices using mileage, manufacturing year, number of doors, accident history, and location.

Advantages

- Uses multiple sources of information.
- Usually more accurate than simple linear regression.
- Easy to interpret feature importance.

Limitations

- Sensitive to multicollinearity.
- Assumes linear relationships.
- Performance decreases if assumptions are violated.

---

Polynomial Regression

Polynomial Regression models nonlinear relationships by adding polynomial terms to the regression equation. Instead of fitting a straight line, it fits a curve that better represents complex data patterns.

Real-World Use Case

Predicting crop yield based on fertilizer usage, where the relationship is nonlinear.

Advantages

- Captures curved relationships.
- More flexible than linear regression.
- Can improve prediction accuracy when relationships are nonlinear.

Limitations

- Can easily overfit the training data.
- More computationally expensive.
- Choosing the correct polynomial degree can be difficult.

---

3. Regression Metrics

Mean Absolute Error (MAE)

Mean Absolute Error measures the average absolute difference between actual values and predicted values. Every error contributes equally to the final score, making MAE easy to understand.

Lower MAE values indicate better model performance.

---

Mean Squared Error (MSE)

Mean Squared Error calculates the average squared difference between predicted and actual values. Squaring the errors gives greater weight to large prediction errors.

This makes MSE useful when large mistakes should be penalized more heavily.

---

Root Mean Squared Error (RMSE)

Root Mean Squared Error is the square root of MSE. Because RMSE is expressed in the same unit as the target variable, it is easier to interpret than MSE.

Lower RMSE values indicate better predictions.

---

Coefficient of Determination (R²)

The R² score measures how well the regression model explains the variation in the target variable.

An R² value of:

- 1.0 means perfect prediction.
- 0 means the model performs no better than predicting the average.
- Negative values indicate poor model performance.

Higher R² values are better.

---

Comparison of Regression Metrics

Metric| Unit| Sensitive to Large Errors| Interpretation
MAE| Same as target| No| Average prediction error
MSE| Squared unit| Yes| Penalizes large errors heavily
RMSE| Same as target| Yes| Average error with greater penalty for large mistakes
R²| No unit| No| Percentage of variance explained by the model

---

4. Underfitting and Overfitting

Underfitting

Underfitting occurs when a model is too simple to learn the underlying patterns in the data. As a result, the model performs poorly on both training and testing datasets.

Common causes include using too few features or selecting an overly simple model.

---

Overfitting

Overfitting occurs when a model learns not only the true patterns in the training data but also the noise. Such a model performs very well on the training data but poorly on unseen test data.

Polynomial Regression is particularly vulnerable to overfitting when a very high polynomial degree is used because the model begins fitting random fluctuations instead of meaningful trends.

Methods to Prevent Overfitting

- Use cross-validation.
- Reduce model complexity.
- Apply regularization techniques.
- Increase the amount of training data.
- Perform feature selection.
- Prune decision trees or limit tree depth.

---

5. Real-World Case Study

House Price Prediction Using Multiple Linear Regression

A common real-world application of regression is predicting house prices. Real estate companies collect information such as house size, number of bedrooms, location, age of the building, and nearby facilities.

Researchers train a Multiple Linear Regression model using historical housing sales data. The model learns how each feature contributes to the final selling price.

The results help buyers estimate fair market values, assist sellers in pricing properties competitively, and support banks in property valuation for mortgage approvals.

Although more advanced algorithms such as Random Forest and Gradient Boosting often achieve higher accuracy, Multiple Linear Regression remains valuable because it is easy to interpret and explains how different variables influence the final prediction.

---

References

Géron, A. (2023). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (3rd ed.). O'Reilly Media.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning (2nd ed.). Springer.

Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830.