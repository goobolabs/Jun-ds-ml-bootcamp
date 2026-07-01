# Regression — Theory

**Course:** Machine Learning
**Date:** July 1, 2026

---

## 1. Introduction to Regression

### 1.1 What is Regression in Machine Learning?

Regression is a category of supervised learning in which a model learns to predict a continuous numerical value from a set of input features. Given a training dataset of input-output pairs, a regression algorithm tries to find the mathematical relationship between the independent variables (features) and the dependent variable (target) so that, when given new, unseen inputs, it can output a reasonable numeric estimate. For example, in the car dataset used for the practical part of this assignment, a regression model learns the relationship between vehicle features (odometer reading, number of doors, accident history, year, location, and similar attributes) and the actual selling price of the car, so that it can later estimate the price for cars it has never seen.

### 1.2 How is Regression Different from Classification?

Both regression and classification are supervised learning tasks, meaning both rely on labeled training data. The key difference lies in the nature of the output variable. Regression predicts a continuous quantity that can take any numerical value within a range, such as $4,171 or $8,699 for a car's price. Classification, on the other hand, predicts a discrete category or class label from a finite, predefined set of possibilities, such as "Affordable" versus "Expensive," or "Accident-Free" versus "Has Accident History." Because the output types differ, the two tasks also use different evaluation metrics: regression relies on error-based metrics such as MAE and RMSE, while classification relies on metrics such as accuracy, precision, and recall.

### 1.3 Real-Life Examples

A real-life example of regression is predicting the selling price of a used car in dollars based on features such as mileage, age, number of doors, accident history, and location, which is exactly the task performed in the practical part of this assignment. A real-life example of classification is predicting whether a given car should be labeled "Good Deal" or "Overpriced" based on the same kind of vehicle features; here the output is a category rather than a number.

---

## 2. Types of Regression

### 2.1 Linear Regression

Linear regression models the relationship between a single independent variable and the dependent variable as a straight line. It assumes that the target value can be approximated by multiplying the input feature by a coefficient (weight) and adding a constant (intercept). The model is trained by finding the line that minimizes the overall squared distance between the predicted values and the actual values, a method known as least squares.

- **How it works:** It fits the equation y = b0 + b1x by adjusting b0 and b1 so that the predicted line is as close as possible to all the data points.
- **Real-world use case:** Estimating a car's resale price based solely on its odometer reading.
- **Advantages:** Simple, fast to train, easy to interpret, and works well when the relationship between variables is approximately linear.
- **Limitations:** Cannot capture more complex or curved relationships, and it is sensitive to outliers since it tries to minimize squared error across all points.

### 2.2 Multiple Linear Regression

Multiple linear regression extends simple linear regression to situations where more than one independent variable influences the target. Instead of a single coefficient, the model learns a separate coefficient for each input feature, allowing it to capture the combined effect of several factors at once. This is the technique used directly in the car price prediction script for this assignment, since a car's price depends on several features simultaneously — odometer reading, age, accident history, number of doors, and location — rather than just one.

- **How it works:** It fits the equation y = b0 + b1x1 + b2x2 + ... + bnxn, where each xi is a different feature and each bi is its learned weight.
- **Real-world use case:** Predicting a car's price based on multiple factors such as mileage, age, accident history, and whether it is located in a city, suburb, or rural area.
- **Advantages:** Captures the joint effect of multiple factors, generally more accurate than simple linear regression for real-world problems, and still relatively interpretable since each coefficient shows the effect of one feature.
- **Limitations:** Performance degrades when features are highly correlated with each other (multicollinearity) — for example, CarAge and Year in the dataset used for this assignment carry overlapping information — and it still cannot model non-linear relationships well.

### 2.3 Polynomial Regression

Polynomial regression is an extension of linear regression that models non-linear relationships by raising the input features to higher powers (squares, cubes, and so on) before fitting a linear model to those transformed features. Even though the relationship between the transformed features and the target is still linear in terms of the coefficients, the resulting curve can bend and flex to fit more complex patterns in the data.

- **How it works:** It fits an equation such as y = b0 + b1x + b2x^2 + b3x^3 + ..., adding higher-degree terms of the same feature so the model can represent curves instead of only straight lines.
- **Real-world use case:** Modeling how a car's value depreciates over time, since depreciation is typically steep in the first few years and then levels off — a curved rather than a straight-line pattern.
- **Advantages:** Can model curved, non-linear relationships that simple and multiple linear regression cannot capture.
- **Limitations:** Choosing too high a degree easily leads to overfitting, where the model fits the noise in the training data rather than the underlying trend; it is also more sensitive to outliers at the extremes of the data range, such as very old or very high-mileage cars.

### 2.4 Comparison Summary

Linear regression is the simplest and works only when there is roughly one dominant linear relationship. Multiple linear regression builds on this by incorporating several predictors at once, which is closer to most real-world problems such as car pricing. Polynomial regression goes a step further by allowing curvature, at the cost of higher complexity and a greater risk of overfitting if not carefully controlled.

---

## 3. Regression Metrics

To judge whether a regression model is performing well, several numerical metrics are used to quantify the difference between the predicted values and the true values.

- **MAE (Mean Absolute Error):** The average of the absolute differences between predicted and actual values. It tells us, on average, how far off the price predictions are in dollars, without exaggerating the effect of any single large error.
- **MSE (Mean Squared Error):** The average of the squared differences between predicted and actual values. Because the errors are squared before averaging, larger errors are penalized much more heavily than smaller ones, making MSE more sensitive to outliers than MAE.
- **RMSE (Root Mean Squared Error):** The square root of MSE. Taking the square root brings the metric back into the same unit as the original target variable (dollars, in the case of car price), which makes it easier to interpret than MSE while still penalizing large errors more than MAE does.
- **R² (Coefficient of Determination):** A measure of how much of the variance in the target variable is explained by the model, expressed as a value typically between 0 and 1 (it can be negative for a very poor model). An R² of 1 means the model perfectly explains all the variation in the data, while an R² of 0 means the model explains none of it, performing no better than simply predicting the average car price every time.

### 3.1 Comparison Table

| Metric | Unit | Sensitivity to Large Errors | What It Measures |
|---|---|---|---|
| MAE | Same as target variable (dollars) | Low — treats all errors proportionally | Average magnitude of price prediction error |
| MSE | Square of target variable's unit (dollars²) | High — squaring amplifies large errors | Average squared price prediction error |
| RMSE | Same as target variable (dollars) | High — inherits MSE's sensitivity, but interpretable in original units | Typical size of price prediction error, in dollars |
| R² | Unitless (ratio/proportion) | Moderate — large errors reduce explained variance | Proportion of variance in car price explained by the model |

### 3.2 Applying These Metrics to the Practical Task

In the practical part of this assignment, both a Linear Regression model and a Random Forest Regressor were trained on the cleaned car dataset (`clean_car_dataset.csv`) to predict `Price`, using engineered features such as `Odometer_km`, `Doors`, `Accidents`, `CarAge`, `Km_per_Year`, `Price_per_Door`, and location indicators, while `LogPrice` was excluded from the feature set to avoid leaking target information. On the held-out 20% test split, Linear Regression achieved an R² of 0.908, an MAE of $592, and an RMSE of $783, while Random Forest achieved a higher R² of 0.926, a lower MAE of $341, and a lower RMSE of $702. This shows that Random Forest explained more of the variance in car prices and, on average, produced predictions closer to the true price than Linear Regression did. A single-row sanity check further illustrated this: for a car with an actual price of $7,009, Linear Regression predicted $7,457 while Random Forest predicted $8,699, showing that even the better-performing model can still miss on an individual case despite strong overall performance.

---

## 4. Underfitting and Overfitting

**Underfitting** occurs when a model is too simple to capture the underlying pattern in the data. An underfit model performs poorly on both the training data and new, unseen data, because it has not learned enough about the relationship between the features and the target. For example, trying to predict car price using only the number of doors, while ignoring odometer reading, age, and accident history, would likely result in underfitting, since doors alone carry very little information about price.

**Overfitting** occurs when a model is too complex relative to the amount or simplicity of the data, causing it to learn not only the genuine underlying pattern but also the random noise present in the training set. An overfit model performs very well on the training data but poorly on new, unseen data, because it has essentially memorized the training examples — for instance, the exact price of each of the 140 cars in the dataset — rather than learning a generalizable trend.

**Causes of overfitting in polynomial regression:** Polynomial regression is particularly prone to overfitting because increasing the degree of the polynomial gives the model more flexibility to bend and twist the fitted curve. At very high degrees, the curve can pass extremely close to every individual training point, including the noise, instead of representing the smooth underlying relationship between, say, odometer reading and price. This problem becomes worse when the training dataset is small — as with the 140-row car dataset used here — since there are fewer points to constrain the shape of the curve.

**Methods to prevent overfitting:**

1. **Limit model complexity** — for polynomial regression, choose a lower degree, and for tree-based models such as Random Forest, limit the maximum depth of each tree or the number of estimators (for example, `n_estimators=100` as used in the practical script).
2. **Use regularization** — techniques such as Ridge (L2) or Lasso (L1) regression add a penalty term that discourages the model from assigning excessively large weights to any single feature, such as `Km_per_Year` or `Price_per_Door`.
3. **Use cross-validation and a held-out test set** — splitting the data into training and testing sets, as done in the practical part of this assignment (`test_size=0.2, random_state=42`), allows the model's performance to be checked on cars it has not seen, which reveals overfitting that would otherwise be hidden if only training accuracy were examined.

---

## 5. Real-World Case Study

A relevant real-world case study is research on used car price prediction conducted using machine learning techniques applied to a dataset of used car listings. The goal of the study was to estimate used car prices from attributes highly correlated with price, since accurate price estimation is important for dealerships, buyers, and sellers who need to make informed decisions in a market where the volume of used car sales has grown substantially, particularly as used cars have become a more affordable way for individuals to own a vehicle.

The researchers used a used car dataset containing information such as make and model, mileage, age, and other price-relevant attributes, and applied two widely used regression algorithms: Linear Regression and Random Forest. Model performance was evaluated using the same core metrics used in the practical part of this assignment — Mean Absolute Error, Mean Squared Error, and R-Squared. The results showed that both Random Forest and Linear Regression models could accurately predict used car prices, with Random Forest performing slightly better. The study concluded that these insights could assist car dealerships, buyers, and sellers in making informed pricing decisions, and proposed integrating the trained model into a web interface for public use.

This case study is directly relevant to the practical part of this assignment, since it follows the same overall approach: using regression algorithms, specifically Linear Regression and Random Forest, to predict a continuous target (car price) and comparing the models using MAE, MSE, and R². The key insight from this research — that Random Forest tends to slightly outperform Linear Regression for used car price prediction — matches exactly what was observed in the practical results for this assignment, where Random Forest achieved a higher R² (0.926 vs. 0.908) and lower error (MAE of $341 vs. $592) than Linear Regression on the same car dataset.

---

## References

- Used Car Price Prediction Using Machine Learning. Retrieved from https://www.researchgate.net/publication/371171222_Used_Car_Price_Prediction_Using_Machine_Learning
- Course materials and lecture notes, Machine Learning module, Regression unit.
- Scikit-learn documentation, regression and metrics modules.
