# Assignment Four: Regression

## Part C.

## Car Price Prediction.

### What I Implemented
I built two machine learning models, Linear Regression and Random Forest, to predict car prices using a cleaned dataset of 140 records. The data was split into 80% training and 20% testing. I used multiple features such as Year, Odometer_km, CarAge, and others to train the models.

### Comparison of Models
In the sanity check, both models made predictions, but Linear Regression performed better overall. It had a higher R² score (0.406) compared to Random Forest (0.315). This means Linear Regression explained more of the variation in car prices.
Random Forest had a lower MAE but a higher RMSE, meaning it made some large errors in certain predictions. Overall, Linear Regression gave more stable and realistic results.

### Uderstanding Random Forest
Random Forest is an ensemble model that uses many decision trees. Each tree makes a prediction, and the final result is the average of all trees. This helps reduce overfitting and improves stability.

### Metrics Discussion
* Linear Regression: R² = 0.406, RMSE = 1987
* Random Forest: R² = 0.315, RMSE = 2134

Linear Regression performed better in R² and RMSE, meaning it was more accurate overall. Random Forest was slightly better in MAE but less consistent.

### Findings
I prefer Linear Regression for this dataset because it gives more stable and accurate predictions. Since the dataset is small (140 rows), Random Forest does not perform as well. In future, more data and better features like car brand or fuel type could improve both models.


### Why did the Linear Regression model outperform the Random Forest model on this dataset?

Even though Random Forest is generally a more powerful machine learning algorithm, Linear Regression performed better in this specific case due to two main reasons:
 1. Overfitting on Small Data: 
 Random Forest is a complex model that requires a large amount of data to properly build its decision trees. With only 140 records, it easily overfits—meaning it memorizes the training data perfectly but fails to generalize, leading to a much worse R^2 score on testing data. Linear Regression is simpler and highly resistant to overfitting on small datasets.
 2. Model Complexity and Data Size: 
 Random Forest thrives on massive datasets with complex, non-linear relationships. When data is extremely limited, a simple linear model is much more stable and effective because it doesn't try to find complex patterns that aren't reliably there.