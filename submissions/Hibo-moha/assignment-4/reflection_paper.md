# Reflection Paper

## What Did I Implement?

In this assignment, I built two regression models to predict car prices using the cleaned dataset produced in Assignment Three. I used Linear Regression and Random Forest Regressor. The dataset was divided into training and testing sets using an 80/20 split with a random state of 42.

## Comparison of Models

The two models produced different predictions during the sanity check. Linear Regression generated predictions using a linear relationship between the features and the target variable, while Random Forest combined predictions from multiple decision trees.

Based on the evaluation metrics, Linear Regression achieved a higher R² score and lower RMSE. Random Forest had a slightly lower MAE but performed worse overall.

## Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines many decision trees. Each tree makes its own prediction, and the final prediction is the average of all trees. This approach often improves accuracy and reduces overfitting compared to a single decision tree.

## Metrics Discussion

Linear Regression achieved an R² score of 0.4358, while Random Forest achieved 0.2430. The lower RMSE of Linear Regression indicates that it made smaller prediction errors overall.

Although Random Forest had a lower MAE, its larger RMSE suggests that it made some larger mistakes on certain observations.

## Findings

I prefer Linear Regression for this dataset because it achieved a higher R² score and lower RMSE. The results indicate that the relationship between the features and car price is relatively linear.

For this particular dataset, Linear Regression provided more reliable and consistent predictions than Random Forest.