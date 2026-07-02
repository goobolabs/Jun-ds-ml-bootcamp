# Reflection Paper: Car Price Prediction (Linear Regression vs Random Forest)

---

# 1. What I Implemented

In this assignment, I worked on a car price prediction project using a cleaned dataset from Assignment Three. The dataset had already been preprocessed, including handling missing values, encoding categorical variables, and scaling numerical features where necessary.

I implemented two machine learning models:

- Linear Regression
- Random Forest Regressor

Both models were trained to predict car prices based on features such as mileage, engine size, year, brand, and other vehicle attributes. The dataset was split into training and testing sets to evaluate performance fairly.

---

# 2. Comparison of Models

During the sanity check (comparing predicted values with actual car prices), the results from the two models were noticeably different:

- **Linear Regression** produced smoother and more stable predictions. However, it sometimes gave unrealistic values for complex cases, especially when relationships in the data were not strictly linear.
- **Random Forest** produced more flexible and realistic predictions. It handled variations in the dataset better and adapted well to different feature combinations.

Overall, Random Forest gave more realistic results because it could capture non-linear relationships between features and price.

---

# 3. Understanding Random Forest

Random Forest is an ensemble learning method that combines multiple decision trees to make predictions.

It works as follows:
- The dataset is split into many random samples.
- Multiple decision trees are trained independently on these samples.
- Each tree makes a prediction.
- The final prediction is the **average of all tree outputs** (for regression tasks).

This approach reduces overfitting and improves accuracy because it does not rely on a single decision path.

---

# 4. Metrics Discussion

When comparing evaluation metrics:

- **Random Forest** had better R² scores, meaning it explained more variance in the data.
- It also had lower MAE and RMSE, showing smaller prediction errors overall.
- **Linear Regression** had weaker performance because it assumes a straight-line relationship between features and price.

### Interpretation:
- Random Forest is stronger at handling complex and non-linear relationships.
- Linear Regression is simpler but limited when data relationships are complex.

---

# 5. Findings and Model Preference

Based on the results, I prefer Random Forest for car price prediction. The main reason is its ability to handle non-linear relationships and interactions between features, which are very common in real-world car pricing data.

Linear Regression is useful for simplicity and interpretability, but it is not flexible enough for this dataset. In contrast, Random Forest provided more accurate predictions and better generalization on unseen data.

However, Random Forest is more computationally expensive and less interpretable than Linear Regression. Despite this limitation, its higher accuracy makes it more suitable for this task.

---

# Conclusion

This project demonstrated that model selection depends on the complexity of the dataset. While Linear Regression provides a simple baseline, Random Forest delivers better performance for real-world structured data like car prices.