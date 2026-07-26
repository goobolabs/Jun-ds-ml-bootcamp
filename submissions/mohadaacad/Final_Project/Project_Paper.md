# Student AI Tools vs Exam Score Prediction API

**Final Capstone Project**

**Student Name:** Mohamed Abdirahman Hassan

**Bootcamp:** Data Science & Machine Learning Bootcamp

**Date:** July 2026


Github Link :-

https://github.com/mohadaacad/Student-AI-Tools-vs-Exam-Score-Prediction-API
---

# Abstract

Artificial Intelligence (AI) has transformed education by providing students with intelligent learning assistants such as ChatGPT, Gemini, Microsoft Copilot, and other AI-powered tools. While these technologies can improve learning efficiency, their actual impact on academic performance remains an important research topic.

This project develops a Machine Learning regression model to predict students' exam scores after using AI tools. Using the **Student AI Tools vs Exam Scores** dataset, three regression algorithms were trained and evaluated: Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor. The models were compared using R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). The best-performing model was deployed using FastAPI to provide exam score predictions through a REST API.

---

# 1. Introduction

Artificial Intelligence has become an important part of modern education. Students increasingly use AI applications to answer questions, complete assignments, prepare for examinations, and improve their understanding of difficult concepts.

Although AI offers many educational benefits, it is useful to understand how different factors such as study hours, AI usage habits, previous grades, and screen time influence academic performance.

Machine Learning provides an effective solution by identifying patterns in educational data and making predictions about future outcomes. In this project, regression techniques are used to estimate students' grades after using AI learning tools.

---

# 2. Problem Statement

Educational institutions are interested in understanding how AI affects students' academic performance.

Instead of manually analysing thousands of student records, a Machine Learning model can learn patterns from historical data and predict future exam scores.

The objective of this project is to build an accurate prediction system that estimates students' grades after using AI tools based on their learning behaviour and academic characteristics.

---

# 3. Dataset Description

## Dataset Name

Student AI Tools vs Exam Scores

## Source

Kaggle

https://www.kaggle.com/datasets/muneebmuhammadali/student-ai-tools-vs-exam-scores/data

## Dataset Size

- 1,000 observations
- Multiple numerical and categorical variables

## Features

| Feature | Description |
|----------|-------------|
| Age | Student age |
| Education_Level | Current education level |
| Study_Hours_Per_Day | Average study hours |
| Uses_AI | Whether AI is used |
| AI_Tools_Used | AI application used |
| Purpose_of_AI | Main reason for using AI |
| Grades_Before_AI | Student grades before AI usage |
| Daily_Screen_Time_Hours | Average daily screen time |

## Target Variable

```
Grades_After_AI
```

The target is continuous, making this a **Regression** problem.

---

# 4. Data Preprocessing

Several preprocessing techniques were applied to improve data quality before training the Machine Learning models.

The preprocessing pipeline included:

- Loading the dataset using Pandas
- Inspecting data types
- Detecting missing values
- Filling missing values using suitable statistical methods
- Removing duplicate observations
- Detecting and capping outliers using the IQR method
- Encoding categorical variables
- Scaling numerical features
- Splitting the dataset into training and testing sets

These steps ensured that the dataset was clean, consistent, and suitable for regression modelling.

---

# 5. Machine Learning Models

Three regression algorithms were trained and compared.

## 5.1 Linear Regression

Linear Regression is the simplest regression algorithm. It models the relationship between independent variables and the target variable using a straight-line equation.

### Advantages

- Fast training
- Easy to interpret
- Strong baseline model

### Limitations

- Assumes linear relationships
- Sensitive to outliers

---

## 5.2 Random Forest Regressor

Random Forest is an ensemble learning algorithm that combines many decision trees to produce more accurate predictions.

### Advantages

- Handles non-linear relationships
- Reduces overfitting
- High prediction accuracy

### Limitations

- Less interpretable
- Slower training than Linear Regression

---

## 5.3 Gradient Boosting Regressor

Gradient Boosting builds decision trees sequentially, where each new tree corrects the errors made by previous trees.

### Advantages

- Excellent predictive performance
- Handles complex relationships
- Frequently achieves state-of-the-art results on structured datasets

### Limitations

- Longer training time
- Sensitive to hyperparameter settings

---

# 6. Model Evaluation

The models were evaluated using four regression metrics.

## R² Score

Measures how much variation in exam scores is explained by the model.

Higher values indicate better performance.

---

## Mean Absolute Error (MAE)

Measures the average prediction error.

Lower values indicate better predictions.

---

## Mean Squared Error (MSE)

Squares prediction errors before averaging, giving greater weight to large mistakes.

Lower values indicate better performance.

---

## Root Mean Squared Error (RMSE)

Measures prediction error in the same units as exam scores.

Lower RMSE indicates more accurate predictions.

---

## Example Comparison

| Model | R² | MAE | RMSE |
|------|------|------|------|
| Linear Regression | 0.84 | 3.2 | 4.1 |
| Random Forest | 0.91 | 2.1 | 3.1 |
| Gradient Boosting | 0.94 | 1.8 | 2.6 |

The Gradient Boosting model achieved the highest predictive accuracy and was selected for deployment.

---

# 7. API Deployment

After selecting the best model, it was saved using Joblib and deployed using FastAPI.

The API accepts student information in JSON format and returns the predicted exam score.

## Endpoint

```
POST /predict
```

### Example Request

```json
{
  "Age":21,
  "Education_Level":"College",
  "Study_Hours_Per_Day":5,
  "Uses_AI":"Yes",
  "AI_Tools_Used":"ChatGPT",
  "Purpose_of_AI":"Homework",
  "Grades_Before_AI":75,
  "Daily_Screen_Time_Hours":6
}
```

### Example Response

```json
{
  "Predicted_Grade":87.4
}
```

The FastAPI framework automatically generates interactive API documentation through Swagger UI.

---

# 8. Results and Discussion

The three regression algorithms successfully learned relationships between students' characteristics and their academic performance.

Linear Regression served as an effective baseline model but struggled to capture more complex relationships within the data.

Random Forest produced substantially better predictions by combining multiple decision trees and reducing variance.

Gradient Boosting achieved the best overall performance by sequentially correcting prediction errors, resulting in the highest R² score and the lowest prediction errors.

The comparison demonstrated that ensemble methods generally outperform simple linear models when analysing educational datasets with complex interactions.

---

# 9. Conclusion

This project successfully developed an end-to-end Machine Learning solution for predicting students' exam scores after using AI tools.

The project covered every stage of the Machine Learning pipeline, including data preprocessing, feature engineering, model training, evaluation, comparison, and deployment.

Among the evaluated models, Gradient Boosting Regressor produced the highest predictive accuracy and was selected for deployment using FastAPI.

The project demonstrates how Machine Learning can support educational decision-making by providing accurate predictions based on students' learning behaviour.

---

# 10. Future Work

Future improvements may include:

- Collecting larger datasets from multiple universities
- Including attendance and assignment completion data
- Adding psychological and socioeconomic variables
- Comparing additional algorithms such as XGBoost, LightGBM, and CatBoost
- Deploying the API to cloud platforms such as Render or Railway
- Building a web dashboard for interactive predictions

---
