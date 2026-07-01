***====1.Introduction to Regression====***
====What is regression in Machine Learning?====
Regression is a tool in Machine Learning used to predict a continuous number. A continuous number can be any exact value, like money, weight, or distance.
**====How is it different from classification?====**
Although both of them belong supervised Learning but they produced different output:
Regression predicts a specific number (for example: $15,350).
Classification sorts things into categories or groups (for example: "Spam Email" or "Good Email").
=====Give one real-life example of regression and one of classification.====
Regression:predicting the salary of employee based on its knowledge,experience,etc.
Classification:predicting the email if its spam or not based on keywords.
**====2.Types of Regression=====**
***Linear Regression:***
**Basic Idea:** It models a straight-line relationship between a single independent feature and a dependent target by minimizing the distance between the data points and the line.
**Real-World Use Case:** Estimating a student's final exam score based solely on the number of hours they spent studying.
**Advantages:** Mathematically simple, highly interpretable, and computationally fast to train.
**Limitations:** performing poorly if the real-world trend is curved or influenced by multiple factors.
***multiple Linear Regression:***
**Basic Idea:** An extension of linear regression that models the relationship between a single target and two or more independent features.
**Real-World Use Case:** Predicting a cars market price using its mileage, engine size and production year.
**Advantages:** Accommodates complex real-world datasets where outcomes are driven by multiple interacting factors.
**Limitations:** Highly sensitive to multicollinearity (when input features are strongly correlated with each other), which can distort the model's coefficients.

***Polynomial Regression***
**Basic Idea:** It models non-linear relationships by converting linear features into higher-degree polynomial terms, creating a curved regression line while maintaining linear coefficients.
**Real-World Use Case:** Modeling the spread rate of an infectious disease over time during the initial phases of an outbreak.
**Advantages:** Capable of fitting complex, curved patterns that flat linear models completely miss.
**Limitations:** Highly prone to severe overfitting if the polynomial degree is set too high, leading to wild oscillations outside the training boundaries.

***3.Regression Metrics***
Metrics are scores that tell us how many mistakes our model made.
**MAE (Mean Absolute Error):** The average distance between the guess and the real answer. It treats all mistakes normally.
**MSE (Mean Squared Error):** It squares the mistakes before averaging them. This makes big mistakes look much worse.
**RMSE (Root Mean Squared Error):** The square root of MSE. It shows the mistakes in normal units (like dollars).
**R² (R-Squared):** A score from 0 to 1 that tells us how good the model is.
A score of 1 means perfect guesses. 
A score of 0 means the model is just guessing blindly.

***====4.Underfitting and Overfitting===***
**Definitions:**
*Underfitting:* The model is too simple. It cannot find any pattern. It gets bad scores on both old and new data.
*Overfitting:* The model memorizes the training data perfectly, including the mistakes and noise. It gets perfect scores on old data but fails completely on new data.
***Prevention of Methods***
**Cross-Validation:** Splitting data into multiple rotating folds during training to ensure the model performs consistently across different subsets.
**Regularization:** Adding a mathematical penalty to the loss function (such as Ridge or Lasso regression) to shrink large coefficients and keep the model simple.
**Feature Reduction:** Dropping irrelevant or highly redundant features to reduce the data's complexity before it reaches the model.

*Split the Data:* Test the model on different parts of the data to make sure it works everywhere.
*Keep it Simple:* Use mathematical rules to stop the model from using huge numbers or overly complex shapes.
*Drop Bad Information:* Delete features that are useless or confusing before training.

**5.Real-World Case Study**5

*Goal:*A city wanted to predict how many cars would be on the road to fix traffic lights.
*Data Used:* They collected data on the weather, the hour of the day, and holidays.
Regression Type: Multiple Linear Regression.Results: They found that the hour of the day was the most important feature. 
Using this model helped the city reduce traffic delays by 14%.