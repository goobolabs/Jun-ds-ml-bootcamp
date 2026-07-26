# Student Mental Health Prediction Using Machine Learning

## 1. Introduction

Mental health is an important factor that affects students' academic performance, lifestyle, and overall well-being. Social media usage, daily activities, sleeping habits, and study patterns can influence students' stress levels and mental health conditions.

This project applies Machine Learning techniques to analyze student lifestyle and social media behavior in order to predict mental health outcomes. The system performs two main Machine Learning tasks:

* **Classification:** Predicting student Stress Level
* **Regression:** Predicting Mental Health Score

The goal of this project is to develop predictive models that can support understanding of factors affecting student mental health.

---

# 2. Dataset Description

The dataset used in this project is the **Student Social Media and Mental Health Impact** dataset obtained from Kaggle.

**Dataset Source:**
https://www.kaggle.com/datasets/shivasingh4945/student-social-media-and-mental-health-impact

The dataset contains **4,998 student records** with demographic information, academic activities, lifestyle habits, and social media usage patterns. It includes both categorical and numerical features that were used to build machine learning models for classification and regression tasks.

The main features include:

- Age
- Gender
- Country
- Academic Level
- Most Used Social Media Platform
- Purpose of Social Media Usage
- Daily Social Media Usage Hours
- Daily Phone Unlocks
- Study Hours
- Physical Activity Hours
- Sleep Hours

The project predicts two target variables:

- **Stress_Level** (Classification)
- **Mental_Health_Score** (Regression)

---

# 5. Classification Model Comparison

Three machine learning classification algorithms were trained and evaluated using the same training and testing datasets.

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 0.746 | 0.747 | 0.746 | 0.746 |
| Random Forest Classifier | **0.919** | **0.920** | **0.919** | **0.919** |
| Support Vector Machine | 0.776 | 0.779 | 0.776 | 0.776 |

## Best Classification Model

The **Random Forest Classifier** achieved the highest overall performance with an **F1 Score of 0.919**. Since the project focuses on predicting multiple stress level categories, the F1 Score was selected as the primary evaluation metric because it balances both precision and recall.

The Random Forest model captured complex relationships among student lifestyle, academic activities, and social media usage better than the other classification algorithms.

---

---

# 6. Confusion Matrix Evaluation

After selecting the Random Forest Classifier as the best classification model, a confusion matrix was generated to analyze the prediction performance for each stress level category.

The confusion matrix shows the comparison between the actual stress levels and the predicted stress levels produced by the model.


The results show that the Random Forest model correctly classified most student stress levels:

| Actual Class | High | Low | Medium | Very High |
|-------------|------|-----|--------|-----------|
| High | 262 | 1 | 8 | 17 |
| Low | 0 | 120 | 9 | 0 |
| Medium | 20 | 6 | 233 | 0 |
| Very High | 18 | 0 | 2 | 304 |

The diagonal values represent correct predictions, while the remaining values represent classification errors.

The model achieved strong performance across all stress categories, especially for **Very High Stress** and **High Stress** classes. The small number of misclassifications indicates that Random Forest successfully learned the relationship between student lifestyle factors, academic behavior, and stress levels.

The confusion matrix confirms the reliability of the Random Forest model for multi-class stress level prediction.

# 7. Regression Model Comparison

Two regression algorithms were trained and evaluated.

| Model | MAE | RMSE | R² Score |
|-------|------|------|-----------|
| Linear Regression | 0.480 | 0.622 | 0.783 |
| Random Forest Regressor | **0.279** | **0.389** | **0.915** |

## Best Regression Model

The **Random Forest Regressor** produced the lowest prediction error and the highest R² Score, indicating that it successfully learned the complex non-linear relationships between student behavior and mental health score.

---

# 8. Model Evaluation and Sanity Checks

After selecting the best-performing models, several prediction tests were performed to verify that the models produced reasonable outputs.

## Sanity Check 1 (Classification)

**Actual Stress Level**

```
Medium
```

**Predicted Stress Level**

```
High
```

Although this prediction was not correct, the predicted class was close to the actual class, showing that the model captured similar stress patterns.

---

## Sanity Check 2 (Regression)

**Actual Mental Health Score**

```
5.60
```

**Predicted Mental Health Score**

```
5.57
```

The prediction error was very small (0.03), demonstrating excellent regression performance.

---

## Sanity Check 3 (API Prediction)

The deployed Flask API was tested using sample student information. The API successfully processed the JSON request and returned both the predicted stress level and the mental health score.

Example response:

```json
{
    "Stress_Level": "High",
    "Mental_Health_Score": 6.84,
    "confidence": 0.91
}
```

These tests confirm that the trained models were correctly integrated into the prediction API.

---

# 9. Deployment

The best-performing machine learning models were saved using the Joblib library.

Saved files:

- best_classifier.pkl
- best_regressor.pkl
- preprocessor_cls.pkl
- preprocessor_reg.pkl

A Flask API was developed to load these trained models and provide real-time predictions through a `/predict` endpoint.

The prediction workflow is as follows:

1. The user submits student information through the API.
2. The preprocessing pipeline transforms the input data.
3. The classification model predicts the student's stress level.
4. The regression model predicts the mental health score.
5. The API returns both predictions in JSON format.

The API was successfully tested using both Postman and sample JSON requests.

---

# 10. Lessons Learned

This project provided practical experience in developing an end-to-end machine learning system.

The major lessons learned include:

- Proper data preprocessing significantly improves model performance.
- Comparing multiple machine learning algorithms helps identify the most suitable model for the problem.
- Random Forest consistently performed better than the other algorithms for both classification and regression tasks.
- Deploying trained models through a Flask API enables machine learning models to be integrated into real-world applications.
- Machine learning projects require not only model development but also proper documentation, testing, and deployment.

---

# 11. Conclusion

This project demonstrates the successful application of machine learning techniques to analyze student lifestyle and social media behavior for predicting mental health outcomes.

Two predictive systems were developed:

- Stress Level Classification
- Mental Health Score Regression

Among all evaluated models, the **Random Forest Classifier** achieved the best classification performance with an **F1 Score of 0.919**, while the **Random Forest Regressor** achieved the highest regression performance with an **R² Score of 0.915**.

The trained models were successfully deployed using a Flask API, allowing real-time predictions from user-provided data. This project demonstrates how machine learning can support data-driven decision-making in understanding student mental health and lifestyle patterns.

---

# 12. Project Repository

The complete source code, trained models, Flask API, and project documentation are available on GitHub:

GitHub Repository:

https://github.com/Eng-saacid/ds-ml-bootcamp-final-project-Student-Mental-Health-Prediction

The repository contains:

- Machine Learning training notebooks
- Data preprocessing pipeline
- Classification and regression models
- Saved ML models
- Flask API implementation
- Project documentation
- README file