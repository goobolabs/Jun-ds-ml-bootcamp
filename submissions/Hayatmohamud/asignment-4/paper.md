# Part A – Theory

## Introduction to Regression

### What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values. It learns the relationship between input features (independent variables) and a target variable (dependent variable). After learning from historical data, the model can estimate future values for new observations. Regression is widely used in finance, healthcare, business, engineering, and many other fields where numerical prediction is required.

### Difference Between Regression and Classification

Regression and classification are both supervised learning methods, but they solve different types of problems.

Regression predicts continuous numerical values such as house prices, salaries, or temperatures. Classification predicts discrete categories or labels such as spam or not spam, pass or fail, or healthy or diseased.

### Examples

**Regression Example**

Predicting the selling price of a house using its size, number of bedrooms, location, and year built.

**Classification Example**

Predicting whether an email is spam or not spam.

---

# Types of Regression

## 1. Linear Regression

Linear Regression is the simplest regression algorithm. It assumes a straight-line relationship between the input variable and the output variable. The model finds the line that minimizes the prediction errors.

### Real-World Use

Predicting house prices based only on house size.

### Advantages

- Easy to understand.
- Fast to train.
- Easy to interpret.

### Limitations

- Assumes a linear relationship.
- Sensitive to outliers.
- Cannot model complex patterns.

---

## 2. Multiple Linear Regression

Multiple Linear Regression extends Linear Regression by using multiple independent variables to predict one target variable.

Instead of relying on only one feature, it combines several variables to improve prediction accuracy.

### Real-World Use

Predicting employee salaries using education level, years of experience, age, and job position.

### Advantages

- Uses multiple factors.
- More accurate than simple linear regression.
- Easy to interpret.

### Limitations

- Sensitive to multicollinearity.
- Requires careful feature selection.
- Assumes linear relationships.

---

## 3. Polynomial Regression

Polynomial Regression models nonlinear relationships by adding polynomial terms to Linear Regression. Instead of fitting a straight line, it fits a curve that better represents complex data patterns.

### Real-World Use

Predicting fuel consumption based on vehicle speed.

### Advantages

- Models nonlinear relationships.
- More flexible than linear regression.
- Often provides better accuracy.

### Limitations

- Easily overfits the training data.
- Choosing the correct polynomial degree is difficult.
- More computationally expensive.

---

# Comparison of Regression Types

| Type | Relationship | Features | Example |
|------|-------------|----------|---------|
| Linear Regression | Linear | One | House price using size |
| Multiple Linear Regression | Linear | Multiple | Salary prediction |
| Polynomial Regression | Nonlinear | One or More | Fuel consumption |

---

# Regression Metrics

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted values and actual values. Lower MAE indicates better model performance.

---

## Mean Squared Error (MSE)

MSE measures the average squared prediction errors. Squaring makes large errors receive higher penalties.

---

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. Because it uses the same unit as the target variable, it is easier to interpret.

---

## R² (Coefficient of Determination)

R² measures how well the regression model explains the variation in the target variable.

- R² = 1 means perfect prediction.
- R² = 0 means the model explains none of the variation.

Higher values indicate better performance.

---

# Comparison of Regression Metrics

| Metric | Unit | Sensitive to Large Errors | Meaning |
|---------|------|--------------------------|---------|
| MAE | Same as target | Low | Average prediction error |
| MSE | Squared unit | Very High | Average squared error |
| RMSE | Same as target | High | Standard prediction error |
| R² | No unit | No | Percentage of variance explained |

---

# Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to learn the patterns in the training data. As a result, it performs poorly on both the training data and unseen test data.

## Overfitting

Overfitting occurs when a model learns not only the true patterns but also the noise in the training data. It performs very well on training data but poorly on new data.

Polynomial Regression is especially prone to overfitting when a high polynomial degree is used.

### Causes of Overfitting

- Small datasets
- Very complex models
- High-degree polynomial features
- Too many irrelevant features

### Methods to Prevent Overfitting

- Collect more training data.
- Use cross-validation.
- Reduce model complexity.
- Apply regularization techniques such as Ridge or Lasso Regression.

---

# Real-World Case Study

## Predicting Student Academic Performance

Regression is widely used in education to predict student academic performance. Universities and schools analyze student information to identify learners who may need additional academic support.

The dataset typically includes attendance percentage, assignment scores, previous examination marks, study hours, and classroom participation. These variables are used as input features, while the target variable is the student's final examination score.

Multiple Linear Regression is commonly used because student performance depends on several factors rather than a single variable. The model learns the relationship between these features and predicts the expected final score.

The results help teachers identify students who are at risk of poor academic performance before final examinations. Schools can then provide additional tutoring, counseling, or academic support to improve learning outcomes. This demonstrates how regression can support data-driven decision-making in education.

---

# References

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.

2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.

3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

4. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.