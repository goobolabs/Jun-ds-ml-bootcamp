### 📌 Problem Statement & Motivation

#### **The Problem**

The rapid advancement and integration of Artificial Intelligence (AI) into the workplace are fundamental restructuring global job dynamics. While AI tools boost productivity, they simultaneously automate routine tasks and alter skill requirements across industries, leading to growing uncertainty regarding **job security and layoff risks** .

Organizations and professionals often lack data-driven, actionable insights to evaluate how specific workplace factors—such as task routine, automation exposure, and AI tool usage—impact individual employment stability. Without structured models, assessing job risk remains reactive and subjective rather than predictive.

#### **The Motivation & Solution**

To address this challenge, this project delivers an **end-to-end Machine Learning solution** designed to quantitatively assess and predict an employee's layoff risk level ( **Low** , **Medium** , or **High** ).

By analyzing workplace metrics (e.g., years of experience, routine task percentages, creativity requirements, and AI usage hours), the system empowers stakeholders with data-driven predictions:

- **For Employees & Job Seekers:** Provides clear visibility into how automation and AI adoption impact their role, highlighting areas where upskilling (e.g., higher creativity or specialized AI training) can mitigate risk.
- **For HR & Strategic Leaders:** Enables scalable batch risk assessment across departments, allowing organizations to plan proactive workforce development, reskilling programs, and smooth technological transitions.

# The Dataset

**Source:** [AI Impact on Jobs and Layoff Risk Dataset](https://www.kaggle.com/datasets/shivasingh4945/ai-impact-on-jobs-and-layoff-risk-dataset) (A realistic workforce analytics dataset focusing on digital transformation and employment metrics).

**Size:** 20,000 rows,

# Main features are

```python

           "Education_Level": "High School",
            "Years_of_Experience": 2.0,
            "Industry": "Retail",
            "Job_Role": "Store Manager",
            "Company_Size": "Small",
            "Job_Level": "Entry",
            "Routine_Task_Percentage": 80,
            "Creativity_Requirement": 10,
            "Human_Interaction_Level": 20,
            "AI_Adoption_Level": "High",
            "Number_of_AI_Tools_Used": 6.0,
            "AI_Usage_Hours_Per_Week": 25,
            "Tasks_Automated_Percentage": 50,
            "AI_Training_Hours": 2
```

### Data Cleaning and Preprocessing Steps

1. **Loaded the dataset** and assigned it to a DataFrame (`df`).
2. **Inspected the dataset** to check whether the data was messy or contained any issues.
3. **Verified that the data was already clean**, so no additional data cleaning was required.
4. **Removed outliers** using the Interquartile Range (IQR) method with the first quartile (Q1 = 0.25) and the third quartile (Q3 = 0.75).
5. **Performed feature engineering** by creating two new features to improve the model's learning ability.
6. **Encoded the categorical features** using both **Label Encoding** and **One-Hot Encoding**, depending on the type of variable.
7. **Saved the cleaned and preprocessed dataset** for use in model training.

# Models Used for Training

I **trained four machine learning classification algorithms to predict the layoff risk of employees. Using multiple algorithms allowed me to compare their performance and choose the model that produced the most accurate and reliable predictions.**

#### \* Logistic Regression Classifier

**How it works:
Logistic Regression calculates the probability that an employee belongs to a particular class (for example, Low, Medium, or High layoff risk). It learns the relationship between the input features and the target variable and predicts the most likely class.**

**Why I chose it:**

**It is a simple and interpretable baseline classification model.
It trains quickly.
It performs well when the relationship between features and the target is approximately linear.
It provides a benchmark to compare with more advanced models.**

#### 2. Random Forest Classifier

**How it works:
Random Forest builds many decision trees using different subsets of the training data. Each tree makes a prediction, and the final prediction is determined by majority voting.**

**Why I chose it:**

**It captures complex, non-linear relationships.
It is less likely to overfit than a single decision tree.
It works well with mixed feature types.
It is generally one of the strongest traditional machine learning algorithms for classification problems.**

#### 3. Support Vector Machine (SVM)

**How it works:
SVM finds the optimal boundary (called a hyperplane) that best separates different classes. It maximises the distance (margin) between the classes to improve classification accuracy.**

**Why I chose it:**

**It performs well on high-dimensional datasets.
It is effective when the classes are clearly separated.
Different kernel functions allow it to model non-linear relationships.**

#### 4. XGBoost (Extreme Gradient Boosting)

**How it works:
XGBoost builds decision trees sequentially. Each new tree learns from the errors made by the previous trees, gradually improving the model's predictions.**

**Why I chose it:**

**It often achieves state-of-the-art performance on structured (tabular) data.
It handles complex patterns effectively.
It includes regularisation techniques that help reduce overfitting.
It is fast, efficient, and widely used in machine learning competitions and real-world applications.**

After evaluating all four machine learning algorithms, I selected the three best-performing models based on their classification accuracy and overall evaluation metrics. The selected models are **Logistic Regression (LR)** , **Support Vector Machine (SVM)** , and **Extreme Gradient Boosting (XGBoost)** . These models demonstrated the best performance and were therefore deployed in the application to predict employee layoff risk accurately and reliably.

Here are the **Deployment Notes** structured specifically for your project documentation or final submission:

---

## 🚀 Deployment Notes

### 1. How the System & Architecture Work

The application is deployed using a decoupled architecture where the UI handles user interaction and the backend inference module executes model predictions.

```text
[ Streamlit Frontend UI ]
        │
        ▼ (Raw user input / Bulk CSV data)
[ predictor.py (Inference Engine) ]
        │
        ├──> Uses utility.py (Preprocesses & Encoders)
        ├──> Loads models/ Robust_scale.pkl & XGB.joblib
        │
        ▼ (Outputs predicted class & risk probability matrix)
[ App Interface / Results Download ]
```

- **Frontend (User Interface):** Built with **Streamlit** (`app.py`), hosting both an interactive sidebar interface for single-profile testing and a drag-and-drop file uploader for batch CSV evaluations.
- **Backend Inference Engine (`predictor.py`):** Acts as the execution layer. It receives raw input records, calls transformation pipelines in `utility.py` to format categorical features and apply `RobustScaler`, and loads trained models (`XGB.joblib`, `lr_model.joblib`, or `SVM_model.joblib`) to run inferences.

---

### 2. Example Request & Response Structure

While the app processes data directly in Python memory via DataFrame objects, the underlying input dictionary structure and model output follow a clear payload format:

#### **Example Input Request (Raw Features)**

```json
{
  "Job_Title": "Data Analyst",
  "Industry": "Technology",
  "Years_of_Experience": 5.0,
  "Routine_Task_Percentage": 65.0,
  "Tasks_Automated_Percentage": 40.0,
  "AI_Training_Hours": 10.0,
  "Creativity_Requirement": 4.0,
  "Selected_Model": "XGBoost"
}
```

#### **Example Output Response (Prediction Payload)**

```json
{
  "Prediction_Class": "Medium Risk",
  "Risk_Level_Code": 1,
  "Probabilities": {
    "Low Risk": 0.18,
    "Medium Risk": 0.67,
    "High Risk": 0.15
  },
  "Status": "Success"
}
```

---

### 3. Frontend Features (`app.py`)

- **Single Employee Evaluation:** Real-time feature adjustment via interactive sliders and dropdowns. Results display as visual confidence badges alongside probability metrics.
- **Batch CSV Processing:** Allows uploading structured `.csv` files, processes hundreds of records concurrently through `predictor.py`, and presents output tables with built-in export capability (`Download Predictions CSV`).
- **Dynamic Model Switching:** Allows users to switch between **XGBoost**, **Logistic Regression**, and **SVM** algorithms in real time to compare prediction outcomes.

Here is a breakdown of your model comparison, evaluation metrics, sanity check observations, and an analysis of which model performed best for your project.

---

## 1. Model Performance Comparison Table

Below is the summary of model evaluation metrics on the test set across **Logistic Regression**, **Random Forest**, **Support Vector Classifier (SVC)**, and **XGBoost**:

| Model                               | Accuracy  | Weighted Precision | Weighted Recall | Weighted F1-Score | Per-Class F1-Score [Low, Med, High] |
| ----------------------------------- | --------- | ------------------ | --------------- | ----------------- | ----------------------------------- |
| **Support Vector Classifier (SVC)** | **0.934** | **0.934**          | **0.934**       | **0.934**         | [0.950, 0.900, 0.952]               |
| **Logistic Regression**             | 0.926     | 0.926              | 0.926           | 0.926             | [0.941, 0.887, 0.948]               |
| **XGBoost Classifier**              | 0.921     | 0.921              | 0.921           | 0.921             | [0.936, 0.881, 0.947]               |
| **Random Forest Classifier**        | 0.880     | 0.880              | 0.880           | 0.880             | [0.907, 0.818, 0.914]               |

---

## 2. Key Findings & Discussion

### Overall Performance Trend

- **Support Vector Classifier (SVC)** achieved the top overall metrics across all evaluation criteria, reaching **93.4% accuracy** and a **0.934 weighted F1-score**.
- **Logistic Regression** performed surprisingly well in second place (**92.6% accuracy**), outperforming complex ensemble methods like XGBoost and Random Forest.
- Across all models, predicting the **"Medium" risk class** was consistently the most challenging class to classify (lowest F1-score), while **"Low"** and **"High"** risk classes achieved higher precision and recall scores.

---

## 3. Sanity Check Observations

Looking at the sample predictions from the sanity check table:

- **Consistency on Clear Cases:** All models successfully agreed on distinct edge cases (e.g., indices 1, 2, 3, 7, 8), correctly classifying High-risk and Low-risk cases.
- **Borderline Class Ambiguity:** Discrepancies primarily occur around border samples between neighboring risk levels (e.g., Index 0 and Index 9):
- **Index 0 (Actual: Low):** XGBoost correctly predicted **Low**, whereas Logistic Regression and SVC misclassified it as **Med**.
- **Index 9 (Actual: Low):** Logistic Regression, SVC, and XGBoost predicted **Med**, while Random Forest misclassified it as **Med** as well.

---

## 4. Best Performing Model & Why

### **Best Model:** Support Vector Classifier (SVC)

### **Why SVC Performed Best:**

1. **Effective Decision Boundaries in High-Dimensional Feature Spaces:** SVC excels at finding optimal hyperplanes with maximum margins between classes, especially when continuous numerical features (such as percentages, hours, and experience) scaled via `RobustScaler` exhibit clear boundary margins.
2. **Robustness to Overfitting:** Tree ensembles (especially Random Forest at 88.0%) showed signs of over-fitting or sensitivity to noisy split thresholds, whereas SVC's regularized margin optimization maximized generalization on unseen test data.
3. **Strong Handling of Linear & Non-Linear Interactions:** Logistic Regression performed strongly (92.6%), demonstrating that the data features have strong, close-to-linear separable components. SVC builds upon this by effectively capturing subtle margin boundaries between the **Medium** class and extreme classes (**Low** / **High**).

## Lessons Learned

Throughout this project, I gained practical experience in the complete machine learning workflow, from data preprocessing and feature engineering to model training, evaluation, and deployment. I learned the importance of preparing high-quality data by handling categorical variables, scaling numerical features, and creating new features that improved model performance. I also gained experience comparing multiple classification algorithms, including Logistic Regression, Support Vector Machine (SVM), and XGBoost, and selecting the most suitable models based on evaluation metrics such as accuracy, precision, recall, and F1-score.

### Challenges Faced

The main challenge I faced during this project was deploying the machine learning application. Initially, I built the project using a React frontend and a Flask backend. However, I experienced difficulties connecting the frontend to the backend API, including handling API communication and maintaining the integration between the two components. This made deployment more complex than expected. To simplify the deployment process and focus on demonstrating the machine learning model, I decided to rebuild the application using Streamlit. Streamlit provided a simpler and more efficient way to deploy the application while preserving all the core machine learning functionality.

### What I Would Improve

If I were to continue developing this project, I would improve my knowledge of full-stack deployment using React and Flask so I could successfully integrate and deploy separate frontend and backend applications. I would also explore cloud deployment platforms and containerization tools such as Docker to make the deployment process more scalable and easier to manage.

### Key Takeaways

This project taught me that deployment is an important part of the machine learning lifecycle. Choosing the right deployment framework depends on the project's goals. While React and Flask offer greater flexibility for full-stack applications, Streamlit is a practical choice for quickly deploying and demonstrating machine learning models. I also learned that selecting the appropriate technology can save development time and simplify the deployment process without affecting the quality of the machine learning solution.

# my deploymen link= [shiine252-ai-impact-on-jobs-layoff-risk-predictor-app-v25ayj.streamlit.app](https://shiine252-ai-impact-on-jobs-layoff-risk-predictor-app-v25ayj.streamlit.app/)

# my repo link =[github.com/Shiine252/AI-Impact-on-Jobs-Layoff-Risk-Predictor](https://github.com/Shiine252/AI-Impact-on-Jobs-Layoff-Risk-Predictor)
