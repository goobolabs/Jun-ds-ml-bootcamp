# Assignment Four – Regression Theory

## Part A – Theory

### 1. Introduction to Regression

#### What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values. The model learns the relationship between input features (independent variables) and a target variable (dependent variable). After training, it can estimate the value of the target for new data.

For example, regression can predict house prices, car prices, monthly sales, temperature, or student exam scores.

#### How is Regression Different from Classification?

Although both regression and classification are supervised learning methods, they solve different types of problems.

* **Regression** predicts a continuous numerical value.
* **Classification** predicts a category or class label.

For example, predicting that a car costs **$18,500** is a regression task, while predicting whether an email is **Spam** or **Not Spam** is a classification task.

#### Real-Life Examples

**Regression Example:**
A car dealership predicts the selling price of a used car using features such as manufacturing year, mileage, engine size, and number of previous owners.

**Classification Example:**
A bank predicts whether a customer will repay a loan or default based on their financial history.

---

## 2. Types of Regression

### Linear Regression

#### How It Works

Linear Regression assumes a straight-line relationship between the input feature and the target value. It finds the line that minimizes the prediction error.

#### Real-World Use Case

Predicting employee salary based on years of experience.

#### Advantages

* Simple and easy to understand.
* Fast to train.
* Easy to interpret.

#### Limitations

* Only works well when the relationship is approximately linear.
* Sensitive to outliers.
* May perform poorly with complex data.

---

### Multiple Linear Regression

#### How It Works

Multiple Linear Regression extends Linear Regression by using two or more input features to predict a single target variable.

#### Real-World Use Case

Predicting house prices using location, number of bedrooms, house size, and age.

#### Advantages

* Uses multiple factors for prediction.
* Often produces better results than simple linear regression.
* Easy to interpret feature importance.

#### Limitations

* Assumes a linear relationship.
* Sensitive to multicollinearity between features.
* Can overfit if unnecessary features are included.

---

### Polynomial Regression

#### How It Works

Polynomial Regression models curved relationships by adding polynomial terms such as x², x³, and higher powers.

#### Real-World Use Case

Modeling population growth, fuel consumption, or production costs where relationships are nonlinear.

#### Advantages

* Can model nonlinear patterns.
* More flexible than linear regression.
* Often improves prediction when the data follows a curve.

#### Limitations

* Can easily overfit the training data.
* Higher-degree polynomials reduce interpretability.
* Performance may decrease on unseen data if the model is too complex.

---

## 3. Regression Metrics

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted values and actual values. Every error contributes equally to the final score.

A lower MAE indicates better prediction accuracy.

---

### Mean Squared Error (MSE)

MSE measures the average squared difference between predictions and actual values. Squaring gives larger errors much greater importance.

A lower MSE indicates better model performance.

---

### Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. Because it uses the same unit as the target variable, it is easier to interpret than MSE.

A lower RMSE means the predictions are closer to the actual values.

---

### R² (Coefficient of Determination)

R² measures how well the model explains the variation in the target variable.

* R² = 1 means perfect prediction.
* R² = 0 means the model performs no better than predicting the average.
* Negative R² means the model performs worse than predicting the average.

Higher R² values indicate better performance.

---

### Comparison of Regression Metrics

| Metric | What It Measures       | Units          | Sensitive to Large Errors | Better Value |
| ------ | ---------------------- | -------------- | ------------------------- | ------------ |
| MAE    | Average absolute error | Same as target | Low                       | Lower        |
| MSE    | Average squared error  | Squared units  | Very High                 | Lower        |
| RMSE   | Square root of MSE     | Same as target | High                      | Lower        |
| R²     | Explained variance     | No units       | No                        | Higher       |

---

## 4. Underfitting and Overfitting

### Underfitting

Underfitting occurs when a model is too simple to learn the patterns in the data. As a result, it performs poorly on both the training and testing datasets.

### Overfitting

Overfitting occurs when a model learns not only the true patterns but also the noise in the training data. It performs very well on training data but poorly on unseen data.

### Causes of Overfitting (Especially in Polynomial Regression)

* Using a polynomial degree that is too high.
* Training on a small dataset.
* Including too many unnecessary features.
* Noise and outliers in the data.

### Methods to Prevent Overfitting

1. Use cross-validation.
2. Reduce model complexity (choose a lower polynomial degree).
3. Collect more training data.
4. Apply regularization techniques such as Ridge or Lasso Regression.
5. Remove irrelevant features through feature selection.

---

## 5. Real-World Case Study

### Predicting House Prices Using Multiple Linear Regression

One common application of regression is predicting residential property prices.

**Goal:**
Estimate the selling price of houses using information such as size, number of bedrooms, location, and age of the property.

**Data Used:**
A housing dataset containing property characteristics and historical selling prices.

**Regression Technique:**
Multiple Linear Regression.

**Results and Insights:**
The model showed that house size and location were the strongest factors affecting price. Larger houses in desirable neighborhoods generally sold for higher prices. The model helped buyers, sellers, and real estate companies estimate fair market values and make informed decisions.
