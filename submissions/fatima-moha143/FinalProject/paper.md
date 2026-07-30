# Flight Delay Prediction Using Machine Learning

## 1. Problem Statement and Motivation

Flight delays are a significant challenge in the aviation industry. Delayed flights increase operational costs, disrupt airline schedules, and reduce passenger satisfaction. Predicting flight delays before departure enables airlines to improve planning, optimize resources, and provide timely information to passengers.

The objective of this project is to build a machine learning classification model that predicts whether a flight will be **On-Time** or **Delayed** using historical flight information.

---

## 2. Dataset and Preprocessing

### Dataset Source

Flight Delay Prediction Dataset

### Dataset Size

- 539,382 rows
- 7 input features

### Target Variable

Class

- 0 = On-Time
- 1 = Delayed

### Features

The dataset contains the following features:

- Flight
- Time
- Length
- Airline
- AirportFrom
- AirportTo
- DayOfWeek

### Data Preprocessing

Several preprocessing techniques were applied before training the models:

1. Loaded and inspected the dataset.
2. Removed duplicate records.
3. Checked for missing values.
4. Applied One-Hot Encoding to categorical features.
5. Standardized numerical features using StandardScaler.
6. Saved preprocessing artifacts (Scaler and Training Columns).
7. Split the dataset into training and testing sets.

---

## 3. Machine Learning Algorithms

Three supervised machine learning algorithms were trained and compared.

### Logistic Regression

Logistic Regression is a simple and interpretable classification algorithm widely used for binary classification problems. It provides a strong baseline for comparison.

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Gradient Boosting Classifier

Gradient Boosting builds models sequentially by correcting previous errors, making it one of the most powerful classification algorithms for structured datasets.

---

## 4. Model Evaluation

The models were evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score

### Model Comparison

| Model | Purpose |
|--------|----------|
| Logistic Regression | Baseline classifier |
| Random Forest | Ensemble learning |
| Gradient Boosting | Boosting classifier |

### Best Model

Random Forest Classifier achieved the best overall performance and was selected as the final deployment model.

The final model predicts one of two classes:

- On-Time
- Delayed

The prediction confidence is also displayed to the user.

---

## 5. Deployment

The trained Random Forest model was deployed using FastAPI.

### Technologies

- Python
- FastAPI
- HTML
- CSS
- Jinja2
- Joblib
- Scikit-learn
- Pandas

### User Interface

The web application allows users to enter:

- Flight Number
- Departure Time
- Flight Length
- Airline
- Departure Airport
- Arrival Airport
- Day of Week

The application displays:

- Logistic Regression Prediction
- Random Forest Prediction
- Gradient Boosting Prediction
- Best Model
- Final Prediction
- Confidence Score

---

## 6. Project Workflow

```
Raw Flight Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Encoding & Scaling
        │
        ▼
Train/Test Split
        │
        ▼
Model Training
        │
        ▼
Model Comparison
        │
        ▼
Best Model Selection
        │
        ▼
FastAPI Deployment
        │
        ▼
Prediction Website
```

---

## 7. Lessons Learned

This project provided practical experience in building a complete end-to-end machine learning system.

Key lessons include:

- Importance of data preprocessing.
- Handling categorical variables using One-Hot Encoding.
- Scaling numerical features.
- Comparing multiple machine learning models.
- Saving trained models using Joblib.
- Deploying machine learning models with FastAPI.
- Building an interactive web interface using HTML and CSS.

---

## 8. Future Improvements

Possible future enhancements include:

- Hyperparameter tuning.
- Cross-validation.
- Additional feature engineering.
- Integration with real-time flight data.
- Cloud deployment.
- Improved web interface and visualization.

---

## 9. Conclusion

This project successfully developed a complete Flight Delay Prediction System using machine learning techniques. Three classification algorithms were trained and evaluated, with the Random Forest Classifier selected as the best-performing model.

The model was successfully deployed using FastAPI and integrated with an HTML/CSS web application, allowing users to predict whether a flight is likely to be On-Time or Delayed based on flight information.

The project demonstrates the complete machine learning lifecycle, including data preprocessing, model training, evaluation, deployment, and user interaction.

---

## Repository

GitHub Repository:
https://github.com/fatima-moha143/fligh_delay_predict.git
