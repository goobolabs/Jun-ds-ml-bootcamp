# Reflection Paper – Car Price Prediction

## 1. What Did I Implement?

In this assignment, I built two machine learning models to predict car prices using the cleaned dataset from Assignment Three. First, I loaded the cleaned dataset and selected **Price** as the target variable while using the remaining features as input variables. I split the dataset into training and testing sets using an 80:20 ratio with a random state of 42 to ensure reproducible results.

I trained a **Linear Regression** model and a **Random Forest Regressor** model. After training both models, I evaluated their performance using R², MAE, MSE, and RMSE. Finally, I compared the predicted price of one car from the test set with its actual price to perform a sanity check.

---

## 2. Comparison of Models

During the sanity check, both models produced predictions that were close to the actual car price. However, the Random Forest model generally produced predictions that were closer to the true value than the Linear Regression model.

The Random Forest model gave more realistic predictions because it can learn complex and nonlinear relationships between the car features and price. Linear Regression assumes a straight-line relationship, which may not capture all the patterns present in real-world car pricing data.

---

## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Each tree is trained using a random sample of the training data and a random subset of features. When predicting a numerical value, every tree produces its own prediction, and the final result is the average of all predictions.

This approach reduces overfitting and usually provides better accuracy than relying on a single decision tree.

---

## 4. Metrics Discussion

Based on the evaluation metrics, the Random Forest model achieved a higher R² score and lower MAE and RMSE values than the Linear Regression model.

A higher R² indicates that Random Forest explained more of the variation in car prices. Lower MAE and RMSE values mean that its predictions were closer to the actual prices and had smaller prediction errors.

Although Linear Regression is simple, fast, and easy to interpret, Random Forest is generally better at handling complex datasets with nonlinear relationships.

---

## 5. My Findings

After comparing both models, I prefer the Random Forest Regressor for car price prediction. It consistently produced more accurate predictions and achieved better evaluation metrics. Since car prices are influenced by many interacting factors, Random Forest is better suited to capture these complex relationships.

Linear Regression remains useful because it is simple, efficient, and easy to explain. However, for practical applications where prediction accuracy is the main goal, Random Forest is the better choice. This assignment helped me understand the importance of comparing multiple models instead of relying on a single algorithm and selecting the model that best fits the data.
