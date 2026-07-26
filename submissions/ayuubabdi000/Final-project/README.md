# Ayuub

# 🎓 Student Success AI — Course Completion Prediction API

**AI-powered student completion prediction & learning behavior analysis · Built by Ayuub**


<p align="center">
  <img src="images/myphoto.jpeg" width="150", alt="Description">
</p>


![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-61DAFB?logo=react)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange?logo=scikitlearn)


---
### 🚀 [View Live Demo](https://student-success-ai-71cy.vercel.app/)
---



---

# 🌟 Overview

**Student Success AI** is a full-stack machine learning application that predicts whether a student is likely to complete an online course based on learning behavior and engagement data.

The system combines:

- 🎓 Machine Learning classification for course completion prediction
- 📊 K-Means clustering for student learning behavior analysis
- ⚡ FastAPI backend for real-time predictions
- 🎨 React dashboard for user interaction

The goal is to help educators identify students who may need additional support and understand different learning patterns.

```
Student Learning Data
          ↓
Data Preprocessing
          ↓
Machine Learning Models
          ↓
Completion Prediction + Student Learning Profile
```

---

# ✨ Features

| Feature | Description |
|---|---|
| 🎓 Completion Prediction | Predicts whether a student will complete a course |
| 📈 Prediction Probability | Returns model prediction probability |
| 📊 Student Clustering | Groups students into learning behavior categories |
| 🤖 ML Model Comparison | Trains and compares multiple algorithms |
| ⚡ FastAPI API | Real-time machine learning API |
| 🎨 React Dashboard | Interactive user interface |
| 🔒 Privacy Friendly | No student data stored permanently |

---

# 🖼️ Screenshots
![alt text](images/11aa.png)
![alt text](images/1aaa.png)

# 📊 Dataset

## Source

Course Completion Prediction Dataset from Kaggle:

```
https://www.kaggle.com/datasets/nisargpatel344/student-course-completion-prediction-dataset/data```

## Dataset Size

Original dataset:

- 100,000 student records
- 40 features

Final processed dataset:

- 100,000 rows
- 17 columns
- 16 input features
- 1 target variable

Target:

| Value | Meaning |
|-|-|
| 0 | Not Completed |
| 1 | Completed |

---

# 🧹 Data Preprocessing

The following preprocessing steps were applied:

### Feature Removal

Removed:

- Student identifiers
- Personal information
- Course metadata
- Payment information
- Unavailable prediction features

Examples:

```
Student_ID
Name
Course_ID
CourseName
Payment_Amount
Enrollment_Date
Progress_Percentage
```

`Progress_Percentage` was removed because it could cause target leakage by directly revealing course completion progress.

---

### Feature Scaling

Numerical features were standardized using:

```
StandardScaler
```

The scaler was saved and reused during API prediction.

---

### Train/Test Split

The dataset was divided:

```
Training: 80,000 samples
Testing : 20,000 samples
```

The same split was used for all models.

---

# 🤖 Machine Learning Models

Three classification algorithms were trained and compared:

## 1. Logistic Regression

A statistical classification algorithm that predicts class probability using the sigmoid function.

Chosen because:

- Fast training
- Easy interpretation
- Strong baseline for binary classification


## 2. Random Forest

An ensemble algorithm that combines multiple decision trees.

Chosen because:

- Handles complex patterns
- Reduces overfitting
- Provides feature importance


## 3. Gradient Boosting

Builds decision trees sequentially where each model improves previous errors.

Chosen because:

- Strong performance on structured datasets
- Learns complex relationships


---

# 📈 Model Results

| Algorithm | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|-|-|-|-|-|-|
| 🥇 Logistic Regression | **0.602** | **0.597** | 0.581 | **0.589** | **0.638** |
| Gradient Boosting | 0.598 | 0.591 | **0.582** | 0.587 | 0.636 |
| Random Forest | 0.587 | 0.583 | 0.554 | 0.568 | 0.619 |

---

# 🏆 Best Model

The deployed model is:

```
Logistic Regression
```

Selection criteria:

```
Highest F1 Score
```

Why F1 Score?

F1 balances Precision and Recall, which is important because the system should:

- Correctly identify students who may struggle
- Avoid unnecessary intervention for successful students

Final performance:

```
Accuracy : 60.2%
Precision: 59.7%
Recall   : 58.1%
F1 Score : 58.9%
ROC-AUC  : 63.8%
```

---

# 🔍 Important Features

Top features influencing predictions:

| Feature | Importance |
|-|-|
| Video Completion Rate | 0.122 |
| Quiz Score Average | 0.096 |
| Project Grade | 0.093 |
| Peer Interaction Score | 0.083 |
| App Usage Percentage | 0.081 |

---

# 📊 Student Behavior Clustering

K-Means clustering was used to discover student learning groups.

The system identifies:

| Cluster | Student Type |
|-|-|
| 0 | Excellent Student |
| 1 | At Risk Student |
| 2 | Average Student |
| 3 | Active Student |
| 4 | Low Engagement Student |

These groups help educators understand student behavior patterns.

---

# 🚀 Running The Project

## Requirements

```
Python 3.10+
Node.js 18+
```

---

# Backend Setup

Clone repository:

```bash
git clone https://github.com/yourusername/student-success-ai.git

cd student-success-ai
```

Create environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train models:

```bash
python src/train_classifier.py

python src/train_cluster.py
```

Run API:

```bash
uvicorn api.app:app --reload
```

API:

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 🔌 API Documentation

## Prediction Endpoint

```
POST /api/predict
```

Example:

```json
{
 "Login_Frequency":4,
 "Average_Session_Duration_Min":35,
 "Video_Completion_Rate":57.3,
 "Discussion_Participation":3,
 "Time_Spent_Hours":3.6,
 "Days_Since_Last_Login":2,
 "Notifications_Checked":5,
 "Peer_Interaction_Score":6.3,
 "Assignments_Submitted":6,
 "Assignments_Missed":4,
 "Quiz_Attempts":4,
 "Quiz_Score_Avg":67.9,
 "Project_Grade":67.8,
 "Rewatch_Count":9,
 "App_Usage_Percentage":81,
 "Reminder_Emails_Clicked":4
}
```

Response:

```json
{
 "prediction":1,
 "label":"Completed",
 "confidence":0.525
}
```

---

# 📂 Project Structure

```
student-success-ai/

├── api/
│   └── app.py
│    
│    ├── models/
│   ├── student_success_model.joblib
│   ├── cluster_features.pkl
│   ├── student_cluster_model.pkl
│   ├── student_scaler.pkl
│
│
├── dataset/
│
├── frontend/
│

│
├── src/
│   ├── train_classifier.py
│   └── train_cluster.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 Lessons Learned

During this project I learned:

- Data preprocessing has a major impact on ML performance.
- Simple models can outperform complex algorithms depending on the dataset.
- Model comparison is necessary before deployment.
- ML deployment requires matching preprocessing during training and inference.
- Building a complete ML system requires combining data science, backend engineering, and frontend development.



# 👤 Author

## Ayuub


