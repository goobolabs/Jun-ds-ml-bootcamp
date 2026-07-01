# Part C — Reflection Paper

## What I Implemented

In this assignment, I implemented two regression models to predict car prices using my cleaned dataset from Assignment Three. The dataset was already cleaned before modeling, so I mainly focused on preparing the features and target, splitting the data, training the models, making predictions and evaluating their performance.

The target variable was the car price, because the goal was to predict a continuous numerical value. The remaining columns in the dataset were used as input features. These features were given to the models so they could learn the relationship between car information and the final price.

I trained a Linear Regression model and a Random Forest Regressor model. The Linear Regression model tried to learn a straight-line relationship between the features and the price. Since I used many features, this worked as Multiple Linear Regression. The Random Forest Regressor was trained with 100 decision trees and a fixed random state of 42. I used the same training and testing data for both models so the comparison would be fair.

## Comparison of Models

For the sanity check, I selected one row from the test set and compared the actual price with the predictions from both models. The actual price was 1500.0. The Linear Regression model predicted about 385.66, which was far from the actual value. The Random Forest Regressor predicted 1500.0, which matched the actual price exactly for that selected example.

For this single sanity check, Random Forest gave a more realistic result because its prediction was much closer to the actual price. However, I also learned that one example is not enough to judge the whole model. A sanity check is useful for manually checking one prediction, but the final decision should be based on the full test set metrics.

## Understanding Random Forest

Random Forest is a machine learning model made of many decision trees. A decision tree works by asking a series of questions about the data. For example, in a car price problem, a tree may check the year of the car, mileage, engine size, or other features, then use those conditions to estimate the price.

Random Forest does not depend on only one tree. Instead, it builds many trees and combines their predictions. In regression, each tree gives a predicted number, and Random Forest takes the average of those predictions. This makes the model stronger than a single decision tree because it reduces the risk of depending too much on one tree’s decision.

In simple words, Random Forest is like asking many decision trees for their opinion and then taking the average answer. This helps the model handle more complex patterns in the data.

## Metrics Discussion

The model results were mixed. Linear Regression had a better R² score and a lower RMSE. The Linear Regression R² was about 0.443, while the Random Forest R² was about 0.263. This means Linear Regression explained more of the variation in car prices compared to Random Forest.

Linear Regression also had a lower RMSE, about 1925.89, while Random Forest had an RMSE of about 2214.55. Since RMSE gives more importance to large errors, this suggests that Random Forest may have made some bigger mistakes on the test set.

However, Random Forest had a better MAE. Its MAE was about 1198.92, while Linear Regression had an MAE of about 1453.32. This means that, on average, Random Forest had a smaller absolute error. In other words, Random Forest was better when looking at the average size of the mistakes, but Linear Regression was better when considering large errors and overall pattern explanation.

These results show that Linear Regression was more stable overall, while Random Forest performed well in some cases and had a smaller average absolute error. The sanity check also showed that Random Forest could give a very accurate prediction for one selected row, but the full metrics showed that it was not always better across all test examples.

## My Findings

Based on the results, I would prefer Linear Regression as the more stable model for this dataset. Even though Random Forest had a better MAE and performed very well in the sanity check, Linear Regression had a better R² score and lower RMSE. This means it explained the price pattern better and made fewer large errors overall.

However, I would not completely reject Random Forest. It may become better if the dataset is larger, if more useful features are added, or if the model parameters are tuned. Random Forest can capture complex patterns that Linear Regression may miss. But for my current dataset and results, Linear Regression seems to be the better choice for general car price prediction because it gave more consistent performance across the full test set.

This assignment helped me understand that model comparison should not depend on only one prediction. A single sanity check can be interesting, but the full evaluation metrics are more important. I also learned that different metrics can tell different stories about a model, so it is better to look at MAE, RMSE, and R² together before choosing the best model.
