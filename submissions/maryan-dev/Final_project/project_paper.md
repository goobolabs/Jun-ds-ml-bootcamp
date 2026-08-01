# 🧠 WellMind AI: Lifestyle Category Classification and API Deployment

**👩‍💻 Author:** Maryan Mohamed Adam
**🎓 Bootcamp:** DS-ML Bootcamp (Goobo Labs)
**📌 Project:** Final Project — ML Model Development and Deployment
**📅 Date:** July 2026

---

## 📝 1. Abstract

This project develops a machine learning-based lifestyle classification system called WellMind AI. The system predicts whether a user's lifestyle is Healthy, Average, or Poor using ten lifestyle-related features such as sleep duration, sleep quality, stress level, physical activity, and BMI category. Multiple machine learning algorithms were compared, with XGBoost selected as the final model based on Macro F1-score. The trained model was deployed using FastAPI and integrated with optional React and Flutter applications.

## 🎯 2. Problem Statement and Motivation

Many people lack a simple way to understand how sleep duration, sleep quality, physical activity, stress, and BMI-related habits combine into an overall lifestyle risk profile. This project builds a **supervised multi-class classifier** that assigns each user one of three labels: **Healthy**, **Average**, or **Poor** lifestyle category.

The problem is a **classification** task suitable for API deployment: given a JSON object with ten lifestyle fields, the system returns a category, a wellness score for explanation, and rule-based recommendations. Motivation includes public health awareness, coursework capstone requirements, and demonstrating an end-to-end pipeline from raw CSV through model comparison to FastAPI and optional React/Flutter clients.

> The model is **not** a medical device; it is an educational ML deployment built on a public lifestyle dataset.

---

## 📂 3. Dataset and Preprocessing

### 📊 3.1 Source and Size
| repo | live app |
|---|---|
**🔗 Repository:** https://github.com/maryan-dev/wellmind-ai-prediction
**🌐 Live App:** https://well-mind-ai-prediction.vercel.app


| Detail | Value |
|---|---|
| File | `notebook/data/raw/Sleep_Data_Sampled.csv` |
| Rows | 15,000 (requirement: ≥1,000) |
| Columns | 13 |
| Original columns | Demographics, sleep metrics, activity, stress, BMI, steps, sleep disorder, etc. |
| Source | Sleep Health Data (Kaggle), created by Imaginative_Coder |
| Dataset link | https://www.kaggle.com/datasets/imaginativecoder/sleep-health-data-sampled |

### 🧹 3.2 Preprocessing Pipeline

Implemented in **`notebook/1_preprocessing.ipynb`** and **`notebook/paths.py`**:

1. **Cleaning** — Handle missing values, consistent dtypes, valid ranges for sleep hours and scores.
2. **Feature engineering** (for target and dashboard only) — Sleep Score, Activity Score, Stress Index, Fatigue Score, Wellness Score — used to define **Lifestyle Category** with bounded wellness rules and small Gaussian noise so the target is not a perfect deterministic function of raw inputs.
3. **Encoding** — Categorical fields (Gender, Occupation, BMI Category, Sleep Disorder) encoded for modeling; numeric fields scaled where needed.
4. **Split** — 80% train / 20% test, stratified on target, saved as:
   - `notebook/data/train_processed.csv`
   - `notebook/data/test_processed.csv`
   - `notebook/data/test_targets.csv` (labels for evaluation)

> **Important design choice:** The classifier is trained on **10 raw lifestyle columns only**, not on derived wellness scores, to avoid target leakage. Derived scores appear in the API response for user-facing dashboards.

### 🏷️ 3.3 Target Definition

| Class | Approximate Rule |
|---|---|
| Healthy | Wellness score ≥ 75 |
| Average | 50–74 |
| Poor | < 50 |

Noise is added before binning so classes overlap slightly, mimicking real label uncertainty.

---

## 🤖 4. Algorithms

All models were trained on the **same** train set and evaluated on the **same** test set in **`notebook/2_train_models.ipynb`**.

| Algorithm | Rationale |
|---|---|
| **Logistic Regression** | Strong baseline; interpretable linear boundaries in encoded feature space. |
| **Decision Tree** | Non-linear splits; easy to visualize; risk of overfitting controlled via depth. |
| **Random Forest** | Bagging reduces variance; handles mixed feature types well. |
| **K-Nearest Neighbors** | Instance-based comparison to similar profiles in training data. |
| **XGBoost** | Gradient boosted trees; often best on tabular data; handles interactions. |

**Clustering (supplementary):** `notebook/3_clustering.ipynb` applies K-Means and Agglomerative clustering for lifestyle segments (e.g. "High Stress User"); clustering supports dashboard narratives but the deployed `/predict` endpoint uses the **supervised winner**.

---

## 🏆 5. Results and Discussion

### 📈 5.1 Model Comparison (Test Set)

Metrics exported to **`notebook/outputs/model_comparison.csv`**. Summary:

| Algorithm | Test Accuracy | Macro F1 | Notes |
|---|---|---|---|
| **XGBoost** | **0.839** | **0.793** | **Selected best model** |
| K-Nearest Neighbors | 0.831 | 0.788 | Close second |
| Random Forest | 0.788 | 0.764 | Higher train–test gap |
| Logistic Regression | 0.780 | 0.764 | Stable baseline |
| Decision Tree | 0.774 | 0.754 | Most overfit among trees |

**Selection rule:** Highest test Macro F1 (stated in proposal). XGBoost wins by ~0.005 F1 over KNN while maintaining strong accuracy.

Macro-averaged precision and recall align with accuracy in this run because the report uses macro averaging across the three classes. A confusion matrix can be regenerated from notebook 2 for the best model.

### 💡 5.2 Why XGBoost Fits Best

Boosted trees capture non-linear interactions (e.g. low sleep quality combined with high stress) without manual feature crosses. Train–test gap for XGBoost (≈0.03 accuracy gap in CSV) is moderate compared with a single deep decision tree or an unconstrained random forest.

### ✅ 5.3 Sanity Checks (Best Model / API)

Three labeled scenarios are documented in **`scripts/run_sanity_checks.py`**. With the API running:

```bash
py -3 scripts/run_sanity_checks.py
```

Expected behavior:

1. **High sleep + activity, low stress** → higher wellness score; category **Healthy** or **Average**.
2. **Short sleep, high stress, low steps** → lower wellness; category **Poor** or **Average**.
3. **Moderate inputs** → mid wellness; **Average** most likely.

Production **`POST /predict`** uses **`notebook/inference.py`** (aligned with **`notebook/4_inference.ipynb`**) when **`notebook/artifacts/best_model.pkl`** is present; otherwise the API returns **503** (ML not loaded).

---

## 🚀 6. Deployment Notes

### ⚙️ 6.1 API

- **Stack:** FastAPI (`api/app.py`)
- **Start:** `py -3 -m uvicorn api.app:app --reload --host 127.0.0.1 --port 8000`
- **Main endpoint:** `POST /predict`
- **Additional:** `GET /models/comparison`, `POST /predict/all-models` (compare algorithms on one user payload)

**Example request:**

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d "{\"age\":32,\"gender\":\"Male\",\"occupation\":\"Engineer\",\"sleep_duration\":8,\"sleep_quality\":9,\"stress_level\":3,\"physical_activity_level\":85,\"daily_steps\":9500,\"bmi_category\":\"Normal Weight\",\"sleep_disorder\":\"Healthy\"}"
```

**Example response fields:** `lifestyle_category`, `wellness_score`, `confidence`, `scores`, `recommendations`, `model_name`.

**XGBoost** (`notebook/artifacts/best_model.pkl`) is used for production when artifacts load successfully; the metrics table justifies this choice.

### 🌐 6.2 Frontend (Optional / Extra Credit)

- **Web:** React + Vite (`frontend/`) — wellness form, dashboard, ML metrics page.
- **Mobile:** Flutter (`mobile/`) — same user flows.

Both call the same JSON API.

### 🗂️ 6.3 Repository Layout

| Path | Role |
|---|---|
| `notebook/` | Data, preprocessing, training, artifacts |
| `api/` | FastAPI service and inference helpers |
| `frontend/` | Web UI |
| `mobile/` | Mobile UI |
| `scripts/run_sanity_checks.py` | Three sanity checks |

---

## 🎓 7. Lessons Learned

1. **Leakage awareness** — Separating dashboard wellness scores from classifier inputs made the project defensible and improved learning outcomes.
2. **Fair comparison** — One shared split and one primary metric (macro F1) avoided cherry-picking.
3. **Deployment reality** — Packaging encoders with the model and validating JSON schemas in FastAPI reduced integration bugs with the React client.
4. **Improvements** — Add probability calibration, SHAP explanations, and automated tests in CI; register models with MLflow; deploy with Docker for production.

---

## 🏁 8. Conclusion

WellMind AI successfully demonstrates the complete machine learning workflow, from preprocessing and feature engineering to model training, evaluation, and deployment. Among five supervised learning algorithms, XGBoost achieved the best performance and was selected for deployment. The project satisfies the bootcamp requirements and provides a practical wellness classification system that can be extended with explainable AI and cloud deployment.

---

## 📚 9. References

- Imaginative_Coder. *Sleep Health Data*. Kaggle. https://www.kaggle.com/datasets/imaginativecoder/sleep-health-data-sampled
- Scikit-learn Documentation: https://scikit-learn.org/stable/
- XGBoost Documentation: https://xgboost.readthedocs.io/
- Course materials: Data Science & Machine Learning (DS-ML) Bootcamp, Goobo Labs
