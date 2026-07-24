# Project Proposal — Somalia Displacement Event Severity Prediction

---

## 1. Certificate Name

**Dini Mohamed Kahie**

---

## 2. Project Title and Description

**Title:** Somalia Displacement Event Severity Classifier

Every week in Somalia, people are forced to leave their homes because of conflict, drought, or flooding. Humanitarian organizations like UNHCR, OCHA, and Medair have to decide where to send resources — trucks, food, medical teams — before they fully know how bad a displacement event will get. If they wait for the full picture, it is already too late.

This project builds a machine learning model that predicts whether an incoming displacement event will be large (displacing more than 100 people) or small, based on early signals: the cause of displacement, the time of year, the region, and the event duration. The model is deployed as an API so that a field officer or a dashboard can send in basic event details and get back an immediate severity prediction.

The people who benefit are humanitarian field teams, NGO logistics coordinators, and government emergency response units operating in Somalia. A correct early prediction gives them a 1–3 week window to pre-position supplies and staff — which can directly reduce suffering.

---

## 3. Problem Type

**Classification** — binary output: `Large Event` (1) or `Small Event` (0).

The target column is `is_large_event`, which I will engineer from the `figure` column (number of people displaced). An event is labeled large if figure > 100, which covers the top 10% of events in the dataset. This is supervised learning — the historical outcomes are already known.

---

## 4. Dataset

- **Source:** Internal Displacement Monitoring Centre (IDMC) via the Humanitarian Data Exchange (HDX) — [https://data.humdata.org/dataset/som-idmc-idu-events](https://data.humdata.org/dataset/som-idmc-idu-events)
- **Size:** 3,091 rows, 36 columns
- **Target column:** `is_large_event` — 1 if the displacement event affected more than 100 people, 0 otherwise
- **Main features I plan to use:**

| Feature             | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `displacement_type` | Conflict or Disaster                                  |
| `combined_type`     | Conflict, Drought, or Flood                           |
| `month`             | Month of the displacement event (extracted from date) |
| `duration_days`     | Length of the event in days                           |
| `latitude`          | Geographic latitude of origin location                |
| `longitude`         | Geographic longitude of origin location               |
| `year`              | Year of the event (2025 or 2026)                      |

**Preprocessing plan:** engineer target column, extract date features, encode categoricals, cap outliers in `figure`, scale numeric features, stratified 80/20 train/test split.

---

## 5. Algorithms I Plan to Train

| #   | Algorithm               | Why it fits                                                                                                                      |
| --- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Logistic Regression** | Bootcamp baseline for binary classification — fast, interpretable, good starting point                                           |
| 2   | **Random Forest**       | Bootcamp ensemble — handles mixed feature types, robust to class imbalance, captures non-linear patterns                         |
| 3   | **XGBoost**             | Researched — gradient boosting often outperforms random forest on small-to-medium tabular datasets, strong on imbalanced classes |

All three are distinct. Two (Logistic Regression and Random Forest) come from bootcamp Lessons 4–5. XGBoost I will research via its official documentation and scikit-learn-compatible API.

---

## 6. Evaluation Plan

**Metrics for all models:**

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Best-model rule:** Pick the model with the highest **Recall** on the test set.

Recall is the right metric here because the cost of a false negative — predicting "small event" when it is actually large — is much higher than a false positive. Missing a large displacement event means NGOs arrive unprepared. Getting a false alarm is inconvenient but manageable. In humanitarian response, the rule is: better to over-prepare than to miss a crisis.

If two models tie on Recall, break the tie with higher F1-Score.

---

## 7. Deployment Sketch

- **Framework:** FastAPI
- **Endpoint:** `POST /predict`

**Input JSON:**

```json
{
  "displacement_type": "Disaster",
  "combined_type": "Drought",
  "month": 3,
  "duration_days": 6,
  "latitude": 2.12,
  "longitude": 45.27
}
```

**Output JSON:**

```json
{
  "prediction": "Large Event",
  "probability": 0.82,
  "message": "High severity — recommend pre-positioning response teams"
}
```

The API loads the best saved model from `models/best_model.pkl` plus the scaler and encoder artifacts saved during training.

---

## 8. Repository Plan

```text
somalia-displacement-classifier/
├── dataset/
│   └── som_idmc_idu_events.csv
├── src/
│   ├── preprocess.py       # Data cleaning, feature engineering, encoding, and scaling
│   └── train.py            # Train and compare all three models, then save the best model
├── api/
│   └── app.py              # FastAPI application with the /predict endpoint
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── exploration.ipynb   # Exploratory Data Analysis (EDA) and feature analysis
├── README.md
├── requirements.txt
└── project_paper.md
```
