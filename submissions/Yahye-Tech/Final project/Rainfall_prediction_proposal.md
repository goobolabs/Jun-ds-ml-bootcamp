Project Proposal — Rainfall Prediction API

«This proposal outlines the plan for my final machine learning project. The project focuses on predicting the likelihood of rainfall using historical weather data and deploying the trained model as a REST API.»

Date:14 July 2026

---

1. Certificate Name

Yahye Ahmed Mohamud

---

2. Project Title and Description

Title: Rainfall Prediction API

Weather forecasting plays an important role in agriculture, transportation, disaster management, and everyday life. One of the most important weather events to predict is rainfall because it helps farmers plan their farming activities, allows governments to prepare for floods, and assists people in making daily decisions.

The aim of this project is to develop a machine learning model that predicts whether it will rain based on weather measurements such as temperature, humidity, wind speed, atmospheric pressure, and rainfall recorded on previous days. The final product will be deployed as a REST API using FastAPI. Users will submit weather information in JSON format, and the API will return a prediction indicating whether rainfall is expected together with a confidence probability.

---

3. Problem Type

Classification — Binary Classification

This project is a supervised machine learning classification problem because the model will be trained using historical weather records where the rainfall outcome is already known.

The target column is RainTomorrow, where:

- 1 = Rain is expected tomorrow.
- 0 = No rain is expected tomorrow.

The objective is to accurately classify future weather conditions based on historical weather observations.

---

4. Dataset

- Source: Kaggle – Weather Dataset (Rain Prediction)
- Size: Approximately 145,000 weather records with more than 20 weather-related features.
- Target: "RainTomorrow"

Main Features

- "MinTemp" – Minimum temperature
- "MaxTemp" – Maximum temperature
- "Rainfall" – Amount of rainfall recorded
- "Evaporation" – Daily evaporation
- "Sunshine" – Hours of sunshine
- "WindGustSpeed" – Maximum wind gust speed
- "Humidity9am" – Humidity at 9 AM
- "Humidity3pm" – Humidity at 3 PM
- "Pressure9am" – Atmospheric pressure at 9 AM
- "Pressure3pm" – Atmospheric pressure at 3 PM
- "Temp9am" – Temperature at 9 AM
- "Temp3pm" – Temperature at 3 PM
- "RainToday" – Whether it rained today

Preprocessing Plan

Before training the machine learning models, the dataset will be prepared by:

- Removing duplicate records.
- Handling missing values using appropriate techniques.
- Encoding categorical variables into numerical values.
- Scaling numerical features where necessary.
- Splitting the dataset into 80% training and 20% testing sets.
- Verifying the quality of the cleaned data before model training.

---

5. Algorithms I Plan to Train

#| Algorithm| Why it fits
1| Logistic Regression| A simple and effective baseline algorithm for binary classification.
2| Random Forest| Handles complex relationships between weather variables and generally provides high prediction accuracy.
3| Gradient Boosting (Scikit-learn)| A powerful ensemble algorithm that performs well on structured datasets and can improve prediction performance.

These three algorithms satisfy the project requirement of training at least three machine learning models. After evaluating all models, the best-performing model will be selected for deployment.

---

6. Evaluation Plan

All models will be evaluated using the same testing dataset.

The following evaluation metrics will be used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Best Model Selection

The final model will be selected based on the highest F1-Score, since it provides a good balance between Precision and Recall. If two models achieve similar F1-Scores, the model with the higher Recall will be selected because correctly predicting rainfall is important for reducing missed rainfall events.

A comparison table showing the performance of all trained models will be included in the final report.

---

7. Deployment Sketch

- Framework: FastAPI
- Endpoint: "POST /predict"

Input JSON Example

{
  "MinTemp": 18.2,
    "MaxTemp": 29.4,
      "Rainfall": 0.0,
        "Humidity9am": 65,
          "Humidity3pm": 48,
            "Pressure9am": 1018.4,
              "Pressure3pm": 1015.7,
                "Temp9am": 21.0,
                  "Temp3pm": 28.1,
                    "WindGustSpeed": 35,
                      "RainToday": "No"
                      }

                      Output JSON Example

                      {
                        "prediction": "No Rain",
                          "probability": 0.94
                          }

                          The API will load the best trained model from "models/best_model.pkl" together with the preprocessing files required for prediction. Users can send weather information to the API and receive predictions in real time.

                          ---

                          8. Repository Plan

                          rainfall-prediction-api/
                          ├── dataset/
                          │   └── weatherAUS.csv
                          ├── src/
                          │   ├── preprocess.py
                          │   └── train.py
                          ├── api/
                          │   └── app.py
                          ├── models/
                          │   ├── best_model.pkl
                          │   └── scaler.pkl
                          ├── notebooks/
                          │   └── exploration.ipynb
                          ├── README.md
                          ├── requirements.txt
                          └── project_paper.md

                          Planned Commands

                          python src/train.py
                          uvicorn api.app:app --reload

                          The first command trains all machine learning models, compares their performance, and saves the best-performing model. The second command starts the FastAPI application locally, allowing users to test the prediction endpoint through a browser or API testing tools.