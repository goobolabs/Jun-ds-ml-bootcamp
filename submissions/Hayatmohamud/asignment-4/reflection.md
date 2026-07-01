# Reflection Paper

## What Did I Implement?

In this assignment, I implemented a machine learning project to predict car prices using a cleaned dataset from Assignment Three. The dataset had already been preprocessed by removing missing values, encoding categorical variables, creating new features, and scaling numerical data.

I first loaded the cleaned dataset into a Jupyter Notebook. Then, I selected **Price** as the target variable and used all remaining columns except **Price** and **LogPrice** as the input features. After preparing the data, I split it into training and testing sets using an 80/20 ratio with `random_state=42` to ensure reproducible results.

Next, I trained two regression models: **Linear Regression** and **Random Forest Regressor**. After training, I evaluated both models using four regression metrics: **R² Score**, **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **Root Mean Squared Error (RMSE)**. Finally, I performed a sanity check by selecting one sample from the test dataset and comparing the predicted prices from both models with the actual car price.

---

# Comparison of Models

The sanity check showed that both models produced predictions that were close to the actual car price, but the Random Forest model generally produced predictions that were closer to the true value. Linear Regression sometimes underpredicted or overpredicted because it assumes a linear relationship between the features and the target variable.

Random Forest produced more realistic predictions because it can capture complex and nonlinear relationships within the data. Since car prices depend on many interacting factors such as vehicle age, mileage, accidents, and location, Random Forest was better able to model these relationships.

---

# Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Instead of relying on a single tree, it builds multiple trees using different random samples of the training data. Each tree makes its own prediction, and the final prediction is calculated by averaging the predictions from all trees.

Because many trees work together, Random Forest usually produces more stable and accurate predictions than a single decision tree. It also reduces the risk of overfitting while handling complex relationships between variables.

---

# Metrics Discussion

After evaluating both models, I compared their R² Score, MAE, MSE, and RMSE.

The Random Forest model achieved a higher R² Score and lower error values than the Linear Regression model. A higher R² Score means that the model explained more of the variation in car prices, while lower MAE and RMSE values indicate that the prediction errors were smaller.

Linear Regression performed reasonably well and was easy to interpret, but it was limited because it assumes a linear relationship between the input features and the target variable. Random Forest, on the other hand, was able to capture nonlinear patterns in the dataset and therefore achieved better prediction accuracy.

---

# My Findings

Based on the evaluation results, I prefer the Random Forest model for predicting car prices. It consistently produced more accurate predictions and achieved better evaluation metrics than Linear Regression. Its ability to model complex relationships makes it more suitable for real-world datasets where many factors influence the final price.

However, Linear Regression still has important advantages. It is simple, fast to train, and easy to explain, making it useful as a baseline model. If model interpretability is the main objective, Linear Regression is a good choice. If prediction accuracy is more important, Random Forest is the better option.

Overall, this assignment helped me understand the complete machine learning workflow, including data preparation, model training, performance evaluation, and comparing different regression algorithms. It also demonstrated how different models can produce different prediction quality depending on the complexity of the data.