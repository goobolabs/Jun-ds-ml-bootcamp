# Final Project Proposal

Date: july 2026

## 1. Certificate Name

**Hayat Mohamud Hassan** 

---

# 2. Project Title and Description

## Project Title

**JobShield AI: Fake Job Posting Detector Using Machine Learning**

## Project Description

Online job platforms have made it easier for people to find employment opportunities, but they have also become a target for scammers who publish fake job advertisements. These fraudulent postings often ask applicants for personal information or payments and waste valuable time. The goal of this project is to develop a machine learning model that can automatically classify a job posting as **Real** or **Fake** based on its content and metadata. This system can help job seekers avoid scams and assist recruitment platforms in identifying suspicious job advertisements before they reach users.

---

# 3. Problem Type

**Classification (Supervised Learning)**

This project is a binary classification problem because the model predicts one of two categories:

* **Real Job Posting**
* **Fake Job Posting**


---

# 4. Dataset

### Dataset Source

Kaggle – Fake Job Posting Prediction Dataset

https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction

### Expected Size

Approximately **18,000 job postings**, which satisfies the minimum requirement of at least 1,000 rows.

### Target Column

**fraudulent**

* **0** = Real Job Posting
* **1** = Fake Job Posting

### Main Features

| Feature             | Description                              |
| ------------------- | ---------------------------------------- |
| title               | Job title                                |
| location            | Job location                             |
| department          | Hiring department                        |
| salary_range        | Salary information                       |
| company_profile     | Company description                      |
| description         | Full job description                     |
| requirements        | Required skills and qualifications       |
| benefits            | Benefits offered                         |
| employment_type     | Full-time, Part-time, Contract, etc.     |
| required_experience | Experience level                         |
| required_education  | Required education                       |
| industry            | Company industry                         |
| function            | Job function                             |
| telecommuting       | Remote work availability                 |
| has_company_logo    | Whether the company has a logo           |
| has_questions       | Whether screening questions are included |

---

# 5. Algorithms I Plan to Train

## 1. Logistic Regression

Logistic Regression will be used as the baseline model because it performs well on binary classification problems and provides an easy-to-understand benchmark.

## 2. Random Forest

Random Forest combines multiple decision trees to improve prediction accuracy and reduce overfitting, making it suitable for structured datasets.

## 3. Gradient Boosting

Gradient Boosting builds models sequentially by correcting previous errors and often achieves high performance on classification tasks.

---

# 6. Evaluation Plan

The models will be evaluated using the following metrics:

* Accuracy
* Precision
* Recall
* F1 Score

### Best Model Selection

The final model will be selected based on **F1 Score** because the dataset is expected to be imbalanced, with significantly more real job postings than fake ones. F1 Score provides a balanced measure of Precision and Recall, making it more reliable than Accuracy for this problem.

---

# 7. Deployment Sketch

The trained model will be deployed using **FastAPI**.

## API Endpoint

```text
POST /predict
```

### Input (JSON)

```json
{
  "title": "Senior Python Developer",
  "location": "Remote",
  "department": "Engineering",
  "salary_range": "70000-90000",
  "company_profile": "Software company",
  "description": "We are looking for an experienced Python developer...",
  "requirements": "Python, Django, REST APIs",
  "benefits": "Health insurance",
  "employment_type": "Full-time",
  "required_experience": "Mid-Senior",
  "required_education": "Bachelor's Degree",
  "industry": "Information Technology",
  "function": "Engineering",
  "telecommuting": 1,
  "has_company_logo": 1,
  "has_questions": 1
}
```

### Output (JSON)

```json
{
  "prediction": "Real",
  "probability": 0.96
}
```

or

```json
{
  "prediction": "Fake",
  "probability": 0.89
}
```

---

# 8. Repository Plan

```text
jobshield-ai/
│
├── dataset/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── api/
│   └── app.py
│
├── models/
│
├── reports/
│   ├── project-proposal.md
│   └── project_paper.md
│
├── requirements.txt
│
└── README.md
```

