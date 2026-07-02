# Car Price Prediction Using Linear Regression and Random Forest

I trained two machine learning models, **Linear Regression** and **Random Forest**, to predict car prices. I used my cleaned Assignment Three dataset. First, I split the data into training and testing sets. Then, I trained both models and made predictions on the test data.

## Comparison of Models

## Single-Row Sanity Check

| Item | Value |
|------|------:|
| Actual Price | $3,892 |
| Linear Regression Prediction | $3,225 |
| Random Forest Prediction | $4,766 |

The actual car price was **$3,892**.

- Linear Regression predicted **$3,225**, so the error was **$667**.
- Random Forest predicted **$4,766**, so the error was **$874**.

The predictions are different because the two models use different methods. Linear Regression learns a straight-line relationship, while Random Forest uses many decision trees to learn more complex patterns.

From this single example, **Linear Regression** was closer to the actual price. However, one prediction is not enough to decide which model is better. We should compare the models using **R², MAE, MSE, and RMSE**. The better model has **higher R²** and **lower MAE, MSE, and RMSE**.

## Understanding Random Forest

Random Forest is a machine learning algorithm that uses many decision trees. Each tree makes its own prediction. The final prediction is the average of all the trees. This makes the model more accurate and reduces mistakes.

## Metrics Discussion

### Linear Regression

- **R²:** 0.407
- **MAE:** 1,829
- **MSE:** 5,543,710
- **RMSE:** 2,355

### Random Forest

- **R²:** 0.597
- **MAE:** 1,364
- **MSE:** 3,761,761
- **RMSE:** 1,940

This shows that Random Forest performed better.

## Performance Analysis of Linear Regression and Random Forest

The R² scores are relatively low because the dataset has limited variability in the target variable (many cars have the same price of 1500), important predictive features such as car brand and model are missing, and the dataset size is small. Additionally, both Year and Car_Age provide overlapping information, which can reduce the effectiveness of Linear Regression. Random Forest performs better (R² = 0.597) because it can model non-linear relationships, but the overall performance is still constrained by the quality and size of the dataset.

## My Findings

I prefer the **Random Forest** model for predicting car prices because it gives more accurate and realistic predictions. It also has better evaluation metrics than Linear Regression.

Linear Regression is still useful because it is simple, fast, and easy to understand. However, for this dataset, Random Forest is the better choice because it predicts car prices more accurately.