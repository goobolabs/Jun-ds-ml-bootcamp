# Project Proposal – Student Academic Performance Prediction Using AI Tools

**Date:** July 2026

---

# 1. Certificate Name

**Mohamed Abdirahman Hassan**



# 2. Project Title and Description

## Title

**Student Academic Performance Prediction Using AI Tools**

### Description

Artificial Intelligence (AI) tools have become an important part of modern education. Many students use AI-powered applications such as ChatGPT and search assistants to complete assignments, study for exams, and improve their understanding of different subjects. However, educational institutions still need to understand how AI usage affects students' academic performance.

This project aims to build a Machine Learning regression model that predicts a student's academic performance after using AI tools. The prediction will be based on features such as age, education level, study hours, AI usage, previous grades, and daily screen time.

The final product will be a REST API developed with FastAPI. Users will submit student information as JSON, and the API will return the predicted academic grade after AI usage. This project can support educators, researchers, and institutions in understanding the relationship between AI-assisted learning and academic performance.

---

# 3. Problem Type

**Regression**

The target variable is **grades_after_ai**, which represents a continuous numeric value.

This is a supervised learning problem because the model learns from historical student records where the final grades are already known.

---

# 4. Dataset

**Dataset Name**

Student AI Tools vs Exam Scores Dataset

**Source**

Kaggle

https://www.kaggle.com/datasets/muneebmuhammadali/student-ai-tools-vs-exam-scores/data

**Dataset Author**

Muneeb Muhammad Ali

**Dataset Size**

- 1,000 rows
- 9 columns

### Target Variable

- grades_after_ai

### Input Features

- age
- education_level
- study_hours_per_day
- uses_ai
- ai_tools_used
- purpose_of_ai
- grades_before_ai
- daily_screen_time_hours

### Preprocessing Plan

The dataset will be prepared using the following preprocessing pipeline:

- Load and inspect the dataset.
- Check for missing values.
- Handle missing values using median and mode imputation.
- Remove duplicate records.
- Correct inconsistent categorical values.
- Encode categorical variables using One-Hot Encoding.
- Scale numerical features using StandardScaler.
- Split the dataset into 80% training and 20% testing.

---

# 5. Algorithms I Plan to Train

| No. | Algorithm | Reason for Selection |
|-----|-----------|---------------------|
| 1 | Linear Regression | Simple baseline model for predicting continuous values and easy to interpret. |
| 2 | Random Forest Regressor | Captures complex relationships and reduces overfitting through ensemble learning. |
| 3 | Gradient Boosting Regressor | Often achieves high prediction accuracy on structured tabular datasets. |

These three algorithms satisfy the project requirement of training at least three machine learning models. Linear Regression and Random Forest Regressor were introduced during the course, while Gradient Boosting Regressor will be researched using the Scikit-learn documentation.

---

# 6. Evaluation Plan

All models will be evaluated using the same testing dataset.

## Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## Best Model Selection

The best model will be selected based on the following criteria:

1. Highest R² Score.
2. Lowest RMSE if two models achieve similar R² values.

A comparison table will summarize the performance of every trained model before selecting the final model for deployment.

---

# 7. Deployment Sketch

## Framework

FastAPI

## Endpoint

POST /predict

### Example Input

```json
{
  "age": 20,
  "education_level": "College",
  "study_hours_per_day": 5,
  "uses_ai": "Yes",
  "ai_tools_used": "ChatGPT",
  "purpose_of_ai": "Homework",
  "grades_before_ai": 74,
  "daily_screen_time_hours": 6
}
```

### Example Output

```json
{
  "predicted_grade_after_ai": 83.42
}
```

The API will load the trained model from:

```
models/best_model.pkl
```

The API will also load any preprocessing objects such as encoders and scalers before making predictions.

---

# 8. Repository Plan

```text
student-ai-performance-api/

├── dataset/
│   └── student_ai_tools_vs_exam_scores.csv
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
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
│   └── student_performance_prediction.ipynb
│
├── README.md
├── requirements.txt
└── project_paper.md
```

---

# Planned Commands

Train all machine learning models:

```bash
python src/train.py
```

Start the FastAPI application locally:

```bash
uvicorn api.app:app --reload
```

---

# Expected Outcome

The completed project will provide an API capable of predicting students' academic performance after AI tool usage based on their personal information, study habits, previous grades, and AI usage patterns. The project will compare three regression algorithms and deploy the best-performing model as a FastAPI service for real-time predictions.
