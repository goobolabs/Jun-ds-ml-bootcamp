# Final Project Proposal

**Date:** July 2026

---

## 1. Certificate Name

**Ali Omar Abdi**

---

## 2. Project Title and Description

**Title:** Diabetes Risk Prediction API

Diabetes often goes undiagnosed until complications appear, especially in settings where routine lab screening is not widely accessible. This project builds a machine learning model that predicts whether a person is likely to have diabetes based on easily collected demographic and health information (age, gender, BMI, hypertension, heart disease, smoking history, HbA1c level, and blood glucose level). The final deliverable is a REST API that accepts a patient's basic health profile as JSON and returns a diabetes risk prediction with a probability score — useful as a low-cost first-pass screening tool for clinics, health workers, or personal health apps, particularly in resource-limited settings such as Somalia where lab-based screening is not always readily available.

---

## 3. Problem Type

**Classification** — binary output: `Diabetic` (1) or `Not Diabetic` (0).

The target column is `diabetes`. This is supervised learning: the dataset contains historical patient records where the diabetes outcome is already known and confirmed. Classification is my one declared problem type for grading, model comparison, and API deployment.

**Clustering as an exploratory feature-engineering step:** Before training my classifiers, I will also run **K-Means clustering** (unsupervised) on the health features alone, to see whether patients naturally group into risk profiles (e.g. "high BMI + high HbA1c" vs. "older + hypertensive" vs. "low-risk baseline"). I will add the resulting cluster label as an extra input feature and test whether it improves classification performance. This is not one of my three required comparison algorithms and is not the deployed model — it's an exploratory step I will document in the project paper, since it lets me demonstrate all three techniques covered in the bootcamp (classification, regression concepts via probability output, and clustering) within a single, properly-scoped classification project.

---

## 4. Dataset

- **Source:** [Diabetes Prediction Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) (Kaggle).
- **Size:** 100,000 rows, 9 columns — well above the 1,000-row minimum. I plan to use the full dataset, or a stratified subsample if training time becomes a constraint on my machine.
- **Target:** `diabetes` — binary indicator of diabetes status (1 = diabetic, 0 = not diabetic).
- **Main features:**
  - `gender` — Male/Female (categorical)
  - `age` — age in years (numeric)
  - `hypertension` — 1 = has hypertension, 0 = does not (binary)
  - `heart_disease` — 1 = has heart disease, 0 = does not (binary)
  - `smoking_history` — never, former, current, not current, No Info (categorical)
  - `bmi` — Body Mass Index (numeric)
  - `HbA1c_level` — average blood sugar level over the past 2–3 months (numeric)
  - `blood_glucose_level` — blood glucose measurement (numeric)

**Preprocessing plan:** check and handle missing/placeholder values (e.g. "No Info" in `smoking_history`), encode categorical columns (`gender`, `smoking_history`) with one-hot encoding, scale numeric features (`age`, `bmi`, `HbA1c_level`, `blood_glucose_level`) with `StandardScaler`, and use a stratified 80/20 train/test split since the dataset is known to be imbalanced (diabetic cases are the minority class). As an added exploratory step, I will fit K-Means on the scaled health features to generate a `RiskCluster` label, then include it as an extra engineered feature when training the classifiers (see Section 3).

---

## 5. Algorithms I Plan to Train

| # | Algorithm | Why it fits |
| --- | --- | --- |
| 1 | **Logistic Regression** | Bootcamp baseline for binary classification (Lesson 5); fast, interpretable coefficients — useful for understanding which risk factors matter most. |
| 2 | **Random Forest** | Bootcamp ensemble (Lesson 5); handles the mix of numeric and categorical features well and captures non-linear interactions between risk factors like age and BMI. |
| 3 | **K-Nearest Neighbors (KNN)** | Bootcamp algorithm (Lesson 5, Assignment Five); a simple distance-based baseline that groups a new patient with the most similar past patients — useful as a sanity-check model against the more complex ones. |
| 4 | **XGBoost (Gradient Boosting)** | Researched independently — a strong, widely-used performer on structured/tabular medical datasets, and a good candidate for the best model given the class imbalance. |

This exceeds the **minimum of three** algorithms. Three (Logistic Regression, Random Forest, KNN) come from Lesson 5, well past the "at least two from the bootcamp" requirement. XGBoost I will research via the official XGBoost documentation and one tutorial, giving me one algorithm outside the bootcamp curriculum as required.

---

## 6. Evaluation Plan

**Metrics for all models (on the same held-out, stratified test set):**

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Best-model rule:** Rank all trained models by **F1-Score** on the test set. Because diabetic cases are the minority class in this dataset, Accuracy alone could be misleading — a model that predicts "not diabetic" for everyone would still score a high accuracy while catching zero real cases. F1 balances Precision and Recall, which matters here because both error types carry real cost: a false negative means a diabetic patient is told they are low-risk and may not seek care, while a false positive means an unnecessary follow-up test. If two models tie on F1, I will break the tie using **Recall**, since missing an actual diabetic case is the more harmful error in a screening context.

I will print a comparison table with one row per algorithm and save/deploy only the winner.

**Note on regression:** Since every classifier I use (Logistic Regression, Random Forest, KNN, XGBoost) can output a predicted probability rather than just a hard label, I will also report each model's predicted probability score for the sanity-check patients. This is not a separate regression model or a required deliverable — it's a natural extension of the classification output that gives a continuous risk score (e.g. "78% probability of diabetes") alongside the binary decision, which is more clinically useful than a flat yes/no.

---

## 7. Deployment Sketch

- **Framework:** FastAPI (auto-generated docs at `/docs`, consistent with the bootcamp's recommended stack).
- **Endpoint:** `POST /predict`
- **Input JSON example:**

```json
{
  "gender": "Female",
  "age": 45,
  "hypertension": 0,
  "heart_disease": 0,
  "smoking_history": "former",
  "bmi": 27.3,
  "HbA1c_level": 6.1,
  "blood_glucose_level": 135
}
```

- **Output JSON example:**

```json
{
  "prediction": "Diabetic",
  "probability": 0.78
}
```

The API will load the best saved model from `models/best_model.pkl` plus the fitted scaler and encoders needed to transform new input consistently with training.

---

## 8. Repository Plan

```
diabetes-risk-api/
├── dataset/
│   └── raw_diabetes_data.csv
├── src/
│   ├── preprocess.py       # cleaning, encoding, scaling, train/test split
│   ├── clustering.py       # K-Means exploratory step → RiskCluster feature
│   └── train.py            # train all 4 classifiers, compare, save best
├── api/
│   └── app.py              # FastAPI app with /predict
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── encoders.pkl
├── notebooks/
│   └── exploration.ipynb   # optional EDA + clustering visualization
├── README.md
├── requirements.txt
└── project_paper.md
```

**Run commands (planned):**

```bash
python src/train.py            # trains models, prints comparison table, saves best
uvicorn api.app:app --reload   # starts API locally
```

---

*Submitted for DS-ML Bootcamp — Final Project Proposal*