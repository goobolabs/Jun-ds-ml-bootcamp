# 1.Certificate Name:

## Abdihamid Hussein Abdikarin

# 2.project Title and Description.

## Title: AI Impact on Jobs and Layoff Risk.

As artificial intelligence and automation rapidly integrate into the modern economy, human resource departments face massive workforce transformations. HR managers and enterprise leaders need a fast, objective, and data-driven screening tool to understand workforce vulnerabilities.

This project builds a machine learning model that predicts an employee's organizational layoff risk (Low, Medium, or High) based on their demographic profile, job role, and exposure to automation metrics. The final deliverable is a REST API that accepts employee data as JSON and returns a risk prediction with a probability confidence score useful for corporate workforce planning dashboards or internal talent optimization and upskilling triage tools.

# \* 3.problem Type

**Classification** output: High medium or Low.

The target column is Layoff_Risk. This is supervised learning:

## 4. Dataset

**Source:** [AI Impact on Jobs and Layoff Risk Dataset](https://www.kaggle.com/datasets/shivasingh4945/ai-impact-on-jobs-and-layoff-risk-dataset) (A realistic workforce analytics dataset focusing on digital transformation and employment metrics).

**Size:** 20,000 rows, 16 columns.

**Target:** `Layoff_Risk` — whether the employee's layoff risk is categorized as **Low**, **Medium**, or **High** (multi-class text values to encode).

### Main Features:

- `Age` — employee age in years (numeric)
- `Years_of_Experience` — total professional work experience (numeric)
- `Routine_Task_Percentage` — percentage of repetitive and predictable tasks in the role (numeric)
- `Creativity_Requirement` — creativity and problem-solving requirement score from 0–100 (numeric)
- `Human_Interaction_Level` — degree of communication and collaboration required from 0–100 (numeric)
- `AI_Usage_Hours_Per_Week` — weekly hours spent using AI tools (numeric)
- `Tasks_Automated_Percentage` — percentage of tasks automated through AI technologies (numeric)
- `AI_Training_Hours` — total AI-related training hours completed (numeric)
- `Education_Level`, `Industry`, `Job_Role`, `Company_Size`, `Job_Level`, `AI_Adoption_Level` — categorical columns to encode

**Preprocessing Plan:** Impute missing values (if any), encode ordinal categoricals using Ordinal Encoding (`Education_Level`, `Job_Level`), apply One-Hot Encoding to nominal categoricals (`Industry`, `Job_Role`), map the target variable to numerical labels (`0`, `1`, `2`), scale numerical features to support baseline convergence, and execute a stratified train/test split (80/20) to preserve class balance across the multi-class target.

# 5.Algorithms I Plan to Train

| **#** | **Algorithm**                    | **Why it fits**                                                                                                                                                                                                                         |
| ----- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Logistic Regression**          | Baseline for multi-class classification; fast, handles multinomial target distributions natively (One-Vs-Rest), and offers interpretable coefficients to understand early risk baselines.                                               |
| **2** | **Random Forest**                | Advanced tree ensemble; handles the dataset's mixture of categorical text fields (e.g.,`Industry`,`Job_Role`) and numerical features well while inherently reducing the risk of overfitting.                                            |
| **3** | **Support Vector Machine (SVM)** | Effective in high-dimensional spaces resulting from One-Hot Encoding nominal variables; utilizing a non-linear kernel (like RBF) allows the model to find complex decision boundaries between risk categories.                          |
| **4** | **XGBoost**                      | High-performance gradient boosting framework; highly optimized for tabular datasets, natively regularized to prevent overfitting, and capable of capturing subtle non-linear interactions between automation levels and training hours. |

# 6. Evaluation Plan

### Metrics for All Models (on the same held-out test set):

- **Accuracy**
- **Macro Precision**
- **Macro Recall**
- **Macro F1-Score**
- **Multi-class Confusion Matrix**

**Best-Model Rule:** Rank all trained models by **Macro F1-Score** on the test set. Macro F1 balances precision and recall evenly across all three risk categories—which is crucial here because misclassifying a "High Risk" employee (leading to unexpected displacement) and misclassifying a "Low Risk" employee (causing unnecessary internal panic or false triage) are both highly costly operational errors. If two models tie on Macro F1-Score, the tie will be broken by selecting the model with the higher **Recall for the High-Risk class** to ensure the system is optimized to catch as many vulnerable positions as possible.

I will print a comparison table with one row per algorithm and save/deploy only the winner inside the final inference pipeline.

# 7. Deployment Sketch

### Framework:

**FastAPI** (Selected for its high performance, production readiness, asynchronous capabilities, and automatic interactive OpenAPI documentation generation at `/docs`).

### Endpoint:

`POST /predict`

### Input JSON Example:

```json
{
  "Age": 38,
  "Education_Level": "Master's",
  "Years_of_Experience": 11,
  "Industry": "Finance",
  "Job_Role": "Accountant",
  "Company_Size": "Medium",
  "Job_Level": "Entry",
  "Routine_Task_Percentage": 84,
  "Creativity_Requirement": 21,
  "Human_Interaction_Level": 94,
  "AI_Adoption_Level": "Medium",
  "Number_of_AI_Tools_Used": 4,
  "AI_Usage_Hours_Per_Week": 15,
  "Tasks_Automated_Percentage": 68,
  "AI_Training_Hours": 22
}
```

### Output JSON Example:

```json
{
  "prediction": "High",
  "probability": 0.87
}
```

**Deployment Logic:** The API initializes by loading the top-performing serialized model from `models/best_model.pkl` alongside all required preprocessing artifacts (such as the standard scaler, categorical encoders, and feature engineering configuration files). When a payload is received, it handles feature validation via Pydantic, applies the transformations, and delivers the multi-class risk category prediction coupled with its operational confidence score.
