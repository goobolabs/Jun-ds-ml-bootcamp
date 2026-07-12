# Final Project Proposal
---
## 1. Certificate Name
**Suhayb Hassan Mohammoud**

---

## 2. Project Title and Description
### Project Title
Bank Loan Approval and Creditworthiness Predictor

### Description
The traditional process of evaluating loan applications in banking institutions often relies on manual verification, which is time-consuming, prone to human error, and inconsistent. This project addresses the real-world problem of credit risk management by developing an automated machine learning system that predicts whether a loan applicant is creditworthy. By analyzing historical financial attributes, employment status, and credit histories, this system will accurately assess the risk level of each applicant. Financial organizations, loan officers, and underrepresented creditworthy applicants will benefit from this solution, as it ensures faster loan processing times, minimizes the bank’s non-performing loans (defaults), and eliminates human bias in credit assessments.

---

## 3. Problem Type
This project is a **Classification** problem (specifically Binary Classification). The machine learning model will analyze input features to predict a discrete category, determining whether a loan application should be **Approved (1)** or **Rejected (0)** based on the applicant's risk profile.

---

## 4. Dataset
*   **Source:** Kaggle Loan Approval Prediction Dataset
    *   **Link:** [https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset)
*   **Size:** The dataset contains exactly **4,269 rows**.
*   **Target Column:** `loan_status` (Represents the final decision: `Approved` or `Rejected`).
*   **Main Features:**
    *   `no_of_dependents`: Number of dependents the applicant has (Numeric)
    *   `education`: Education status (Categorical: Graduate / Not Graduate)
    *   `self_employed`: Self-employment status (Categorical: Yes / No)
    *   `income_annum`: Annual income of the applicant (Numeric)
    *   `loan_amount`: Total loan amount requested (Numeric)
    *   `loan_term`: The duration/term of the loan in years (Numeric)
    *   `cibil_score`: Credit score of the applicant (Numeric, ranging from 300 to 900)
    *   `residential_assets_value`: Value of the applicant's residential property (Numeric)
    *   `commercial_assets_value`: Value of the applicant's commercial property (Numeric)
    *   `luxury_assets_value`: Value of luxury items owned like cars/jewelry (Numeric)
    *   `bank_asset_value`: Total bank asset value/liquid cash (Numeric)

---

## 5. Algorithms You Plan to Train
To determine the best classifier for this problem, I will train and compare the following **three distinct algorithms**:

1.  **Logistic Regression (Bootcamp Core):** This algorithm fits an S-shaped curve to the data and serves as an excellent, highly interpretable baseline model for binary classification that outputs explicit class probabilities.
2.  **Random Forest Classifier (Bootcamp Core):** This is an ensemble method that combines multiple decision trees using majority voting, which prevents overfitting and captures non-linear relationships between applicant features without complex engineering.
3.  **Support Vector Machines (SVM - Self-Researched):** This algorithm works by finding the optimal hyperplane boundary that maximizes the margin between the approved and rejected classes in a high-dimensional space.

---

## 6. Evaluation Plan
*   **Comparison Metrics:** I will evaluate and compare all trained models using a multi-metric approach, tracking **Accuracy**, **Precision**, **Recall**, and the **F1-Score** from the generated Confusion Matrix.
*   **Single Metric for Best Model:** The best model will be selected based on the highest **F1-Score**. 
    *   *Reason:* Loan status datasets are typically highly imbalanced (with more approvals than rejections). Relying on accuracy alone would be misleading. Furthermore, for a bank, False Positives (approving a risky client who will default) and False Negatives (rejecting a good client) are both highly costly. The F1-Score provides a balanced harmonic mean of Precision and Recall, ensuring the selected model optimizes both risk mitigation and revenue retention.

---

## 7. Deployment Sketch
*   **Framework:** **FastAPI** will be utilized to construct a high-performance web API.
*   **The `/predict` Endpoint Accepts (JSON Input):**
    ```json
    {
      "no_of_dependents": 2,
      "education": "Graduate",
      "self_employed": "No",
      "income_annum": 4200000,
      "loan_amount": 15000000,
      "loan_term": 10,
      "cibil_score": 680,
      "residential_assets_value": 8000000,
      "commercial_assets_value": 2000000,
      "luxury_assets_value": 3000000,
      "bank_asset_value": 4000000
    }
    ```
*   **The `/predict` Endpoint Returns (JSON Output):**
    ```json
    {
      "prediction_label": 1,
      "status": "Approved",
      "approval_probability": 0.89
    }
    ```

---

## 8. Repository Plan
The project structure will follow a modular format to separate preprocessing pipelines, data exploration, and API code:
```bank-loan-predictor/
├── dataset/
│   ├── loan_approval_dataset.csv
│   └── clean_loan_dataset.csv
├── notebooks/
│   └── exploratory_analysis.ipynb
├── src/
│   ├── preprocess.py
│   └── train.py
├── api/
│   └── app.py
├── models/
│   └── best_loan_model.pkl
├── README.md
└── project_paper.md
```