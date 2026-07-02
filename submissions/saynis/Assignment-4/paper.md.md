# Part A — Theory: Regression in Machine Learning

## Introduction to Regression

Regression is a type of supervised machine learning used to predict a number. In supervised learning, the model learns from past examples where the correct answer is already known. The data usually has input features and one target value. The features are the information we use to make a prediction, and the target is the value we want the model to predict.

For example if we want to predict the price of a car, the features may include the year of the car, mileage, engine size, fuel type, and transmission type. The target value is the actual price of the car. The model studies old car records and tries to learn how these features are related to the price. After training, it can estimate the price of a new car.

Regression is different from classification. Regression predicts a continuous numerical value, while classification predicts a category or class. If a model predicts the final mark of a student, that is regression because the answer is a number. If a model predicts whether the student will pass or fail, that is classification because the answer is a category.

A real-life example of regression is predicting house prices using house size, location, number of rooms, and age of the house. A real-life example of classification is predicting whether an email is spam or not spam.

## Types of Regression

## Linear Regression

Linear Regression is the simplest form of regression. It is used when we want to predict a number using one main feature. The basic idea is to draw the best straight line through the data points. This line shows the general relationship between the input and the output.

For example, we may use the mileage of a car to predict its price. In many cases, when mileage increases, the price decreases. Linear Regression tries to learn this relationship and use it to make predictions.

A real-world use case of Linear Regression is predicting a student’s final mark using attendance percentage. If attendance is higher, the final mark may also be higher. This is not always perfect, but it can show a simple pattern.

The main advantage of Linear Regression is that it is easy to understand and fast to train. It also helps us see how one feature affects the target. The main limitation is that real-world problems are often more complex than one straight line. If the data has many factors or a curved pattern, simple Linear Regression may not perform well.

## Multiple Linear Regression

Multiple Linear Regression is similar to Linear Regression, but it uses more than one feature to predict the target value. This is more realistic because most real-world outcomes depend on many factors, not only one.

For example, the price of a car may depend on mileage, year, engine size, fuel type, and transmission. In this case, the model does not look at only one factor. It looks at all selected features together and learns how they are connected to the price.

A real-world use case of Multiple Linear Regression is predicting car prices using several features. It can also be used in education to predict a student’s final mark using attendance, quiz average, assignment average, and previous performance.

The main advantage of Multiple Linear Regression is that it can use more information than simple Linear Regression. This can improve predictions when the target depends on several features. Another advantage is that it is still easier to understand than many advanced models. Its limitation is that it still expects the relationship to be mostly linear. If the relationship is very complex, the model may not capture it well.

## Polynomial Regression

Polynomial Regression is used when the relationship between the feature and the target is not a straight line. Some data follows a curved pattern. In this case, a straight line may be too simple, so Polynomial Regression tries to fit a curve.

For example, study hours and exam score may not increase in a perfect straight line. At first, studying more hours may improve the score quickly. But after some time, the improvement may slow down. A curved model may describe this kind of relationship better.

A real-world use case of Polynomial Regression is predicting sales growth. A new product may grow quickly at the beginning, but later the growth may slow down. A curved regression model may fit this pattern better than a straight-line model.

The main advantage of Polynomial Regression is that it can model curved relationships. Its limitation is that it can easily overfit if the curve is too complex. Overfitting means the model learns the training data too closely and performs poorly on new data.

## Regression Metrics

Regression metrics are used to check how good or bad a regression model is. After the model makes predictions, we compare the predicted values with the actual values. The difference between the actual value and the predicted value is called the error.

Mean Absolute Error, or MAE, measures the average size of the prediction errors. It tells us how far the predictions are from the actual values on average. For example, if a car price model has an MAE of 1,200, it means the model is wrong by about 1,200 price units on average. MAE is easy to understand because it uses the same unit as the target value.

Mean Squared Error, or MSE, also measures prediction error, but it squares each error before taking the average. This means large errors become much bigger. MSE is useful when large mistakes are serious, but it is harder to understand because the unit is squared.

Root Mean Squared Error, or RMSE, is the square root of MSE. It brings the error back to the original unit of the target. RMSE is easier to understand than MSE and still gives more attention to large errors. If RMSE is much higher than MAE, it may mean the model has some large mistakes.

R², also called the Coefficient of Determination, measures how much of the pattern in the target value is explained by the model. A value close to 1 means the model explains the data well. A value close to 0 means the model is not better than simply guessing the average. A negative R² means the model is performing worse than a simple average prediction.

In simple terms, MAE tells us the average error, MSE strongly punishes big errors, RMSE shows error in the original unit while still caring about big errors, and R² tells us how well the model explains the pattern in the data.

## Underfitting and Overfitting

Underfitting happens when a model is too simple to learn the real pattern in the data. In regression, this may happen when we use a straight-line model for data that clearly follows a curved pattern. An underfitted model usually performs badly on both training data and testing data.

Overfitting happens when a model learns the training data too closely. It may memorize small details or noise instead of learning the general pattern. An overfitted model may perform very well on training data, but poorly on new testing data.

Polynomial Regression can overfit when the degree is too high. A high-degree polynomial can create a very flexible curve that passes close to many training points. This may look good on the training data, but it may not work well for new data.

There are several ways to reduce overfitting. One method is to use a train-test split, so the model is tested on data it has not seen before. Another method is to reduce model complexity, such as using a lower polynomial degree. A third method is to use cross-validation, where the model is tested on different parts of the data. Collecting more data can also help because the model gets more examples and is less likely to memorize only a few cases.

## Real-World Case Study

One real-world use of regression is in healthcare, where researchers used Multiple Linear Regression to predict hospital length of stay for patients who had laparoscopic appendectomy. The goal of the study was to estimate how long patients would stay in the hospital. This kind of prediction can help hospitals plan beds, staff, and resources.

The data came from hospital patient records. It included information such as patient age, gender, health conditions, diagnosis, complications, surgery information, and the length of stay in the hospital. The target value was the total number of days the patient stayed in the hospital.

The researchers used Multiple Linear Regression because the target was a number and because many factors could affect the result. The model looked at several features together, such as age, complications, and diagnosis type, to estimate the length of stay.

The study found that some factors had more influence than others. Age, pre-operative length of stay, complications, and complicated diagnosis were important factors. The model was not perfect, but it gave useful information that could support hospital planning.

This case study shows that regression is useful in real life because it can help organizations make better decisions. In a school management system, a similar idea could be used to predict student final marks, student risk scores, or fee payment delays using historical school data.

## Conclusion

Regression is an important machine learning method used to predict numerical values. It is different from classification because regression predicts numbers, while classification predicts categories. Linear Regression is simple and useful when there is one main factor. Multiple Linear Regression uses several features and is better for many real-world problems. Polynomial Regression can model curved patterns, but it must be used carefully to avoid overfitting.

Regression metrics such as MAE, MSE, RMSE, and R² help us evaluate how well a model performs. MAE and RMSE are easy to understand because they relate to prediction error, while R² helps us understand how much of the target pattern the model explains. A good regression model should not only perform well on training data, but also on new unseen data.

## References

Scikit-learn Documentation. LinearRegression.

Scikit-learn Documentation. Regression metrics and model evaluation.

Scikit-learn Documentation. PolynomialFeatures.

Trunfio, T. A., and others. Multiple regression model to analyze the total length of stay for patients undergoing laparoscopic appendectomy. BMC Medical Informatics and Decision Making, 2022.
