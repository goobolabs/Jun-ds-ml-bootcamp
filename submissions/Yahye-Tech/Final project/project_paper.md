# Rainfall Prediction API

**Final Machine Learning Project**

**Author:** Yahye-Tech  
**Date:** 14 July 2026  
**GitHub Repository:** [https://github.com/Yahye-Tech/Final-Project-Rainfall-prediction-Data-science-and-ML](https://github.com/Yahye-Tech/Final-Project-Rainfall-prediction-Data-science-and-ML)

---

## 1. Introduction

Weather forecasting plays an important role in agriculture, transportation, disaster management,
and everyday life. One of the most important weather events to predict is rainfall because it
helps farmers plan their farming activities, allows governments to prepare for floods, and
assists people in making daily decisions.

The aim of this project is to develop a machine learning model that predicts whether it will
rain based on weather measurements such as temperature, humidity, wind speed, atmospheric
pressure, and rainfall recorded on previous days. The final product is deployed as a REST API
using FastAPI. Users submit weather information in JSON format, and the API returns a prediction
indicating whether rainfall is expected together with a confidence probability.

---

## 2. Problem Statement

**Problem type:** Binary classification (supervised learning)

This project is a supervised machine learning classification problem because the model is
trained using historical weather records where the rainfall outcome is already known.

**Target column:** `RainTomorrow`

- `1` = Rain is expected tomorrow
- `0` = No rain is expected tomorrow

The objective is to accurately classify future weather conditions based on historical weather
observations.

---

## 3. Dataset

**Source:** Kaggle – Weather Dataset (Rain Prediction)  
**Link:** [WeatherAUS](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)  
**Size:** Approximately 145,000 weather records with more than 20 weather-related features  
**Target:** `RainTomorrow`

**Main features used in this project:**

| Feature | Description |
|---|---|
| MinTemp | Minimum temperature |
| MaxTemp | Maximum temperature |
| Rainfall | Amount of rainfall recorded |
| Evaporation | Daily evaporation |
| Sunshine | Hours of sunshine |
| WindGustSpeed | Maximum wind gust speed |
| Humidity9am | Humidity at 9 AM |
| Humidity3pm | Humidity at 3 PM |
| Pressure9am | Atmospheric pressure at 9 AM |
| Pressure3pm | Atmospheric pressure at 3 PM |
| Temp9am | Temperature at 9 AM |
| Temp3pm | Temperature at 3 PM |
| RainToday | Whether it rained today |

---

## 4. Preprocessing

Before training the machine learning models, the dataset was prepared by:

1. Removing duplicate records
2. Dropping rows with missing target (`RainTomorrow`) or `RainToday`
3. Handling missing values using median imputation (numerical) and most-frequent imputation (categorical)
4. Encoding categorical variables (`RainToday`) with one-hot encoding
5. Scaling numerical features with standard scaling
6. Splitting the dataset into 80% training and 20% testing sets (stratified split)

All preprocessing statistics (imputer values, scaler parameters) are fit on the training set
only to prevent data leakage. The fitted preprocessing pipeline is saved to `models/scaler.pkl`
for use during inference.

---

## 5. Algorithms

Three classification algorithms were trained as specified in the project proposal:

| # | Algorithm | Why it fits |
|---|---|---|
| 1 | Logistic Regression | A simple and effective baseline algorithm for binary classification |
| 2 | Random Forest | Handles complex relationships between weather variables and generally provides high prediction accuracy |
| 3 | Gradient Boosting (scikit-learn) | A powerful ensemble algorithm that performs well on structured datasets and can improve prediction performance |

These three algorithms satisfy the project requirement of training at least three machine
learning models. After evaluating all models, the best-performing model was selected for
deployment.

---

## 6. Evaluation

All models were evaluated on the same 20% held-out test set using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Model Comparison Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.7871 | 0.5132 | 0.7604 | 0.6128 |
| **Random Forest** | **0.8047** | **0.5421** | **0.7638** | **0.6341** |
| Gradient Boosting | 0.8538 | 0.7416 | 0.5224 | 0.6130 |

### Confusion Matrices

**Logistic Regression:**

|  | Predicted No Rain | Predicted Rain |
|---|---|---|
| Actual No Rain | 17,417 | 4,501 |
| Actual Rain | 1,495 | 4,745 |

**Random Forest:**

|  | Predicted No Rain | Predicted Rain |
|---|---|---|
| Actual No Rain | 17,892 | 4,026 |
| Actual Rain | 1,474 | 4,766 |

**Gradient Boosting:**

|  | Predicted No Rain | Predicted Rain |
|---|---|---|
| Actual No Rain | 20,782 | 1,136 |
| Actual Rain | 2,980 | 3,260 |

### Best Model Selection

The final model was selected based on the **highest F1-Score**, since it provides a good
balance between Precision and Recall. If two models achieved similar F1-Scores, the model
with the higher Recall was selected, because correctly predicting rainfall is important for
reducing missed rainfall events.

**Selected model: Random Forest** (F1-Score = 0.6341, Recall = 0.7638)

Random Forest achieved the highest F1-Score among all three models. It also achieved the
highest Recall, meaning it correctly identified more actual rainfall events compared to the
other models. While Gradient Boosting had the highest overall accuracy (0.8538), its lower
Recall (0.5224) means it missed nearly half of all actual rainfall events, making it less
suitable for this use case.

Full comparison results are saved in `models/metrics_report.json`.

---

## 7. Deployment

**Framework:** FastAPI  
**Endpoint:** `POST /predict`

The API loads the best trained model from `models/best_model.pkl` together with the
preprocessing pipeline from `models/scaler.pkl`. Users can send weather information to the
API and receive predictions in real time.

**Input JSON example:**

```json
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
                      ```

                      **Output JSON example:**

                      ```json
                      {
                        "prediction": "No Rain",
                          "probability": 0.94
                          }
                          ```

                          ### Additional API Endpoints

                          | Method | Endpoint | Description |
                          |---|---|---|
                          | GET | `/` | Service information |
                          | GET | `/health` | Health check (model and preprocessor status) |
                          | GET | `/docs` | Interactive Swagger documentation |
                          | POST | `/predict` | Submit weather data and receive rainfall prediction |

                          ---

                          ## 8. Repository Structure

                          ```
                          ├── dataset/
                          │   └── weatherAUS.csv
                          ├── src/
                          │   ├── preprocess.py
                          │   └── train.py
                          ├── api/
                          │   └── app.py
                          ├── models/
                          │   ├── best_model.pkl
                          │   ├── scaler.pkl
                          │   └── metrics_report.json
                          ├── notebooks/
                          │   └── exploration.ipynb
                          ├── README.md
                          ├── requirements.txt
                          └── project_paper.md
                          ```

                          ### Planned Commands

                          ```bash
                          python src/train.py
                          ```

                          The first command trains all machine learning models, compares their performance, and saves
                          the best-performing model.

                          ```bash
                          uvicorn api.app:app --reload
                          ```

                          The second command starts the FastAPI application locally, allowing users to test the
                          prediction endpoint through a browser or API testing tools.

                          ---

                          ## 9. Technologies

                          | Category | Technology |
                          |---|---|
                          | Language | Python 3.11+ |
                          | Data | pandas, numpy |
                          | ML | scikit-learn |
                          | API | FastAPI, Uvicorn |
                          | Validation | Pydantic |

                          ---

                          ## 10. Conclusion

                          This project successfully implements an end-to-end rainfall prediction pipeline: data
                          preprocessing, training and comparison of three machine learning models, selection of the
                          best model by F1-Score, and deployment as a REST API. The Random Forest model was selected
                          as the best performer with an F1-Score of 0.6341 and a Recall of 0.7638. The system allows
                          users to submit weather data and receive real-time rainfall predictions with confidence scores.
                          