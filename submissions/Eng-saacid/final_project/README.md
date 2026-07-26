# Student Mental Health Prediction API

## Overview

This project uses Machine Learning to predict students' **Stress Level** and **Mental Health Score** based on social media usage and lifestyle factors.

The system includes both:
- **Classification** → Predicts Stress Level (Low, Medium, High)
- **Regression** → Predicts Mental Health Score

## Dataset

Dataset: `student_social_media.csv`

Features include:
- Age
- Gender
- Country
- Academic Level
- Most Used Platform
- Purpose of Use
- Average Daily Usage Hours

## Machine Learning Models

### Classification Models
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

### Regression Models
- Linear Regression
- Random Forest Regressor

## Project Structure
```
student-mental-health-api/
│
├── dataset/
│   └── student_social_media.csv
│
├── src/
│   ├── preprocess.py        # data cleaning, encoding, scaling, train/test split
│   └── train.py             # train models, compare performance, save best models
│
├── api/
│   └── app.py               # FastAPI app with /predict endpoint
│
├── models/
│   ├── best_classifier.pkl  # best stress level prediction model
│   ├── best_regressor.pkl   # best mental health score prediction model
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── notebooks/
│   └── exploration.ipynb    # optional EDA and data analysis
│
├── README.md
├── requirements.txt
└── project_paper.md
```
