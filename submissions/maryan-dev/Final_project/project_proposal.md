# Final Project Proposal

## 1. Certificate Name

**Maryan Mohamed Adam**

---

## 2. Project Title and Description

### Title:
**AI-Powered Personal Wellness Recommendation System (WellMind AI)**

### Description:

WellMind AI is a machine learning-based personal wellness recommendation system that predicts a user's overall wellness category (Healthy, Average, or Poor) based on their lifestyle behaviors, including sleep patterns, stress levels, and physical activity.

Many people experience problems such as poor sleep, high stress, and low physical activity without understanding how these factors combine to affect their overall wellness. Most existing wellness applications provide general advice instead of personalized recommendations based on an individual's own lifestyle data.

This project aims to solve this problem by using machine learning techniques to analyze lifestyle information and provide personalized recommendations. The system will help users understand their habits, identify possible lifestyle issues, and receive AI-generated suggestions for improving sleep, reducing stress, and maintaining healthier routines.

The project will benefit everyday users, students, and employees who want simple, data-driven wellness guidance instead of one-size-fits-all advice.

---

## 3. Problem Type

This project will use both supervised and unsupervised machine learning approaches.

### Supervised Learning (Classification)

The primary problem type is **Classification**.

The model will predict the user's:

**Lifestyle Category**

Classes:

- Healthy
- Average
- Poor

The classification model will be used by the `/predict` API to provide personalized wellness recommendations.

### Unsupervised Learning (Clustering)

K-Means clustering will be used as a secondary analysis method to discover hidden lifestyle patterns among users.

Examples of discovered groups:

- Healthy Lifestyle Users
- Sleep-Deprived Users
- High Stress Users
- Low Activity Users

These clusters will help improve the understanding of different user behaviors.

---

## 4. Dataset

### Dataset Source

Kaggle:

https://www.kaggle.com/datasets/imaginativecoder/sleep-health-data-sampled

### Dataset Size

The dataset contains approximately **15,000 rows** of sleep and lifestyle-related information.

The exact dataset size will be confirmed during Exploratory Data Analysis (EDA) using `df.shape`.

This dataset size is suitable for machine learning training, testing, model comparison, and clustering analysis.

### Target Column

The target column will be:

**Lifestyle Category**

Classes:

- Healthy
- Average
- Poor

The original dataset does not contain this target column. It will be created through feature engineering using sleep, activity, and stress-related information.

The target will be generated from a calculated Wellness Score representing the user's overall lifestyle condition.

### Main Features

The original dataset features used in this project include:

| Feature | Description |
|---|---|
| Age | User age |
| Gender | User gender |
| Occupation | User job type |
| Sleep Duration | Number of hours slept |
| Quality of Sleep | Sleep quality level |
| Physical Activity Level | Daily activity level |
| Stress Level | Stress intensity |
| BMI Category | Body weight category |
| Daily Steps | Number of daily steps |
| Sleep Disorder | Sleep-related problems |

---

## 5. Feature Engineering

New features will be created from the original dataset features to improve model performance and provide deeper wellness insights.

### Sleep Score

Created using:

- Sleep Duration
- Quality of Sleep

This represents the overall quality of the user's sleep.

### Activity Score

Created using:

- Physical Activity Level
- Daily Steps

This measures the user's physical activity level.

### Stress Index

Created using:

- Stress Level

This converts stress information into a numerical score for machine learning models.

### Fatigue Score

Created using:

- Sleep Score
- Stress Index
- Activity Score

This estimates the user's fatigue level.

### Wellness Score

Created using:

- Sleep Score
- Activity Score
- Stress Index
- Fatigue Score

This represents the user's overall wellness condition.

### Lifestyle Category (Target)

Created from Wellness Score:

- Healthy
- Average
- Poor

This target will be used for supervised classification.

---

## 6. Algorithms You Plan to Train

### 1. Logistic Regression

Used as a baseline classification model because it is simple, interpretable, and suitable for multi-class classification.

### 2. Decision Tree

Used because it can learn non-linear relationships and provide understandable decision rules.

### 3. Random Forest

Used because it combines multiple decision trees, reduces overfitting, and usually performs well on structured datasets.

### 4. K-Means Clustering

Used for unsupervised learning to discover groups of users with similar lifestyle patterns.

### 5. XGBoost

Used as an advanced gradient boosting algorithm because it performs strongly on structured/tabular data.

---

## 7. Evaluation Plan

### Classification Metrics

The classification models will be evaluated using:

- Accuracy
- Precision
- Recall
- Macro F1 Score
- Confusion Matrix

### Best Model Selection

The best classification model will be selected using:

**Macro F1 Score**

because it provides balanced evaluation across all wellness categories, especially when class sizes are different.

### Clustering Metrics

The clustering performance will be evaluated using:

- Silhouette Score
- Davies-Bouldin Index

The best clustering configuration will be selected using the highest Silhouette Score.

---

## 8. Deployment Sketch

### Framework

The backend API will be developed using:

**FastAPI**

### Endpoint

```
POST /predict
```

### Input JSON

```json
{
  "age": 25,
  "gender": "Female",
  "occupation": "Student",
  "sleep_duration": 5,
  "sleep_quality": 4,
  "stress_level": 8,
  "physical_activity_level": "Low",
  "daily_steps": 3000
}
```

### Output JSON

```json
{
  "prediction": "Poor Lifestyle",
  "wellness_score": 45,
  "recommendations": [
    "Improve sleep duration",
    "Reduce stress level",
    "Increase physical activity"
  ],
  "confidence": 0.91,
  "cluster_label": 2
}
```

---

## 9. Repository Plan

```
wellmind-ai/
│
├── dataset/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_clustering.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── evaluate.py
│
├── api/
│   └── app.py
│
├── models/
│   └── best_model.pkl
│
├── frontend/
│
├── README.md
│
└── project_paper.md
```

---

## Expected Outcome

The final system will provide users with personalized wellness recommendations using machine learning techniques.

The system will analyze lifestyle factors such as sleep patterns, stress levels, physical activity, and daily habits to predict the user's wellness category and generate suitable recommendations.

Multiple machine learning models will be trained and compared to identify the best-performing model for wellness prediction. Additionally, clustering techniques will be used to discover hidden lifestyle patterns and group users based on similar behaviors.

The WellMind AI application will present predictions, wellness scores, lifestyle groups, and personalized recommendations through an interactive dashboard. The system aims to help users better understand their daily habits, improve their lifestyle choices, and make informed wellness decisions using artificial intelligence.