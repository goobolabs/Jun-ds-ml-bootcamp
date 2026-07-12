Project Proposal — Heart Disease Prediction API

Date: 12 July 2026

---

1. Certificate Name

Yahye Ahmed Mohamud

---

2. Project Title and Description

Title: Heart Disease Prediction API

Heart disease is one of the most common health problems around the world, and early detection can help doctors provide better treatment and reduce health risks. Hospitals and healthcare centers collect a large amount of patient information, but it can be difficult to analyze all of it manually. Machine learning provides a way to assist medical professionals by identifying patterns in patient data.

The goal of this project is to develop a machine learning model that predicts whether a patient is likely to have heart disease based on medical information such as age, blood pressure, cholesterol level, heart rate, and other health indicators. The final system will be deployed as a REST API using FastAPI. Users will send patient information in JSON format, and the API will return a prediction together with the confidence score of the model.

---

3. Problem Type

Classification — Binary Classification

This project is a supervised machine learning classification problem because the model will be trained using historical patient records where the diagnosis is already known.

The target column is HeartDisease, where:

- 1 = Patient has heart disease
- 0 = Patient does not have heart disease

The objective is to correctly classify new patient records based on their medical information.

---

4. Dataset

- Source: Kaggle – Heart Disease Prediction Dataset
- Size: Approximately 918 patient records with 11 input features and 1 target column.
- Target: "HeartDisease"

Main Features

- "Age" – Patient's age
- "Sex" – Male or Female
- "ChestPainType" – Type of chest pain
- "RestingBP" – Resting blood pressure
- "Cholesterol" – Cholesterol level
- "FastingBS" – Fasting blood sugar
- "RestingECG" – Resting electrocardiogram results
- "MaxHR" – Maximum heart rate achieved
- "ExerciseAngina" – Exercise-induced angina
- "Oldpeak" – ST depression value
- "ST_Slope" – Slope of the ST segment

Preprocessing Plan

Before training the models, the dataset will be prepared by:

- Checking and handling missing values if necessary.
- Encoding categorical features into numerical values.
- Scaling numerical features using StandardScaler.
- Splitting the dataset into 80% training data and 20% testing data.
- Verifying the data to ensure it is suitable for machine learning.

---

5. Algorithms I Plan to Train

#| Algorithm| Why it fits
1| Logistic Regression| A simple and effective baseline algorithm for binary classification problems.
2| Random Forest| Handles complex relationships between features and usually provides high accuracy while reducing overfitting.
3| Gradient Boosting (Scikit-learn)| A powerful ensemble algorithm that often performs well on structured medical datasets and may provide the best prediction accuracy.

These three algorithms satisfy the project requirement of training at least three machine learning models. After comparing their performance, the best model will be selected for deployment.

---

6. Evaluation Plan

All models will be evaluated using the same testing dataset to ensure a fair comparison.

The following evaluation metrics will be used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Best Model Selection

The model with the highest F1-Score will be selected as the final model because it balances both Precision and Recall. If two models achieve similar F1-Scores, the model with the higher Recall will be chosen since detecting patients who actually have heart disease is especially important.

A comparison table showing the performance of each algorithm will also be included.

---

7. Deployment Sketch

- Framework: FastAPI
- Endpoint: "POST /predict"

Input JSON Example

{
  "Age": 54,
    "Sex": "M",
      "ChestPainType": "ATA",
        "RestingBP": 140,
          "Cholesterol": 239,
            "FastingBS": 0,
              "RestingECG": "Normal",
                "MaxHR": 160,
                  "ExerciseAngina": "N",
                    "Oldpeak": 1.0,
                      "ST_Slope": "Up"
                      }

                      Output JSON Example

                      {
                        "prediction": "Heart Disease",
                          "probability": 0.92
                          }

                          The API will load the best trained model from "models/best_model.pkl" together with the preprocessing files needed to make predictions. This will allow users to send patient information and receive predictions quickly through a simple REST API.

                          ---

                          8. Repository Plan

                          heart-disease-prediction-api/
                          ├── dataset/
                          │   └── heart.csv
                          ├── src/
                          │   ├── preprocess.py      # Data cleaning and preprocessing
                          │   └── train.py           # Train, compare and save models
                          ├── api/
                          │   └── app.py             # FastAPI application
                          ├── models/
                          │   ├── best_model.pkl
                          │   └── scaler.pkl
                          ├── notebooks/
                          │   └── exploration.ipynb  # Exploratory Data Analysis
                          ├── README.md
                          ├── requirements.txt
                          └── project_paper.md

                          Planned Commands

                          python src/train.py
                          uvicorn api.app:app --reload

                          The first command trains the machine learning models, compares their performance, and saves the best-performing model. The second command starts the FastAPI application locally, allowing users to test the prediction endpoint through the browser or API tools.