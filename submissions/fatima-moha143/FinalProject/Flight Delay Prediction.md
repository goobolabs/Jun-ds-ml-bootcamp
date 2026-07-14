# 1. Certificate Name

[Fadumo Mohamed Omar]

---

# 2. Project Title and Description

## Title: Flight Delay Prediction System
Airlines operate thousands of flights every day, and delays can disrupt schedules, increase operational costs, and reduce passenger satisfaction. This project develops a machine learning classification model that predicts whether a flight will be on time or delayed using historical flight information such as departure time, flight duration, airline, departure airport, destination airport, and day of the week.

The final deliverable is a machine learning prediction system that classifies each flight as On-Time or Delayed, helping airlines improve operational planning and decision-making.

---

# 3. Problem Type

3. Problem Type

Classification — binary output: On-Time or Delayed.

The target column is Class. This is a supervised learning problem because the model is trained using historical flight records where the flight status is already known.

Target Variable:

0 = On-Time
1 = Delayed

The goal of this project is to predict whether a flight will arrive on time or be delayed based on flight-related information.
---

# 4. Dataset

# Source: Kaggle – Airlines Delay Dataset

* Dataset Link:
* https://www.kaggle.com/datasets/ulrikthygepedersen/airlines-delay

# Size:
* 539,382 rows
* 8 columns
* 1 CSV file

# Target:

* Class — Indicates whether the flight was delayed or on time.
* 0 = On-Time
* 1 = Delayed
### Main Features:

* Flight — Flight identification number
* Time — Scheduled departure time
* Length — Flight duration (minutes)
* Airline — Airline code
* AirportFrom — Departure airport
* AirportTo — Destination airport
* DayOfWeek — Day of the week (1–7)
### Preprocessing Plan:

* Handle missing values (if any)
* Remove duplicate records
* Drop unnecessary columns (if appropriate, e.g., Flight)
* Encode categorical variables (Airline, AirportFrom, AirportTo)
* Scale numerical features (Time, Length)
* Perform a stratified train/test split (80/20)
---

# 5. Algorithms I Plan to Train

| # | Algorithm                    | Why it fits                                                                             |
| - | ---------------------------- | --------------------------------------------------------------------------------------- |
| 1 | Logistic Regression          | Strong baseline model for binary classification and easy interpretation.                |
| 2 | Random Forest Classifier     | Handles complex relationships, reduces overfitting, and works well with mixed features. |
| 3 | Gradient Boosting Classifier | Powerful ensemble algorithm that often performs well on structured datasets.            |

This meets the requirement of training at least three machine learning algorithms.

The first two models are based on classification methods learned during the bootcamp, while Gradient Boosting will be researched using scikit-learn documentation and tutorials.

---

# 6. Evaluation Plan

All models will be evaluated using the same test dataset.

Metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC Score

### Best Model Selection:

The final model will be selected based on the highest **F1-Score** because flight delay prediction requires balancing:

* Correctly identifying delayed flights (Recall)
* Avoiding unnecessary delay predictions (Precision)

If two models have similar F1-Scores, ROC-AUC and Recall will be considered.

The best model will be saved and used for deployment.

---

# 7. Deployment Sketch

**Framework:** FastAPI

FastAPI will be used to create a REST API that allows users to send flight information and receive delay predictions.

## Endpoint:

```
POST /predict
```

### Input JSON Example:

```json
{
  "Airline": "Delta",
  "Origin": "JFK",
  "Destination": "LAX",
  "Distance": 2475,
  "Departure_Hour": 14,
  "Day_of_Week": 5,
  "Month": 7
}
```

### Output JSON Example:

```json
{
  "prediction": "Delayed",
  "probability": 0.82
}
```

The API will load the saved best model from:

```
models/best_model.pkl
```

along with preprocessing files such as encoders and scalers.

---

# 8. Repository Plan

```
flight-delay-prediction/
│
├── dataset/
│   ├── raw_flights.csv
│   └── cleaned_flights.csv
│
├── src/
│   ├── preprocess.py
│   └── train.py
│
├── api/
│   └── app.py
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── notebooks/
│   └── exploration.ipynb
│
├── images/
│   ├── delay_distribution.png
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── README.md
├── requirements.txt
└── project_paper.md
```

---

# 9. Expected Outcome

The project will produce a machine learning model capable of predicting flight delays from historical flight information.

The system will help demonstrate how machine learning can solve real-world aviation problems by improving decision-making, reducing operational problems, and providing better passenger services.

---
