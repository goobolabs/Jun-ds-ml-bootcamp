# 📌 Final Project Proposal

**Power Plant Energy Output Prediction API**
*A Machine Learning Regression System for Combined Cycle Power Plants*

---

## 1. Certificate Name

> **Abdidahir Bashir Ali**

---

## 2. Project Title and Description

### 🏷️ Project Title
**Power Plant Energy Output Prediction API**

### 📝 Description

Combined cycle power plants must constantly balance electricity supply with grid demand, but their electrical output is highly sensitive to ambient environmental conditions such as temperature, pressure, and humidity. Operators need a fast, reliable way to estimate expected power output under current conditions so they can plan load dispatch and avoid over- or under-generation.

This project builds a machine learning regression model that predicts the net hourly electrical energy output of a combined cycle power plant using ambient sensor readings. The trained model is deployed as a FastAPI application that accepts sensor measurements and returns the predicted power output in megawatts (MW). Plant operators and grid management systems benefit by using these predictions to optimize load scheduling and improve operational efficiency.

---

## 3. Problem Type

**🎯 Regression**

This is a regression problem because the target variable — net hourly electrical energy output (`PE`), measured in megawatts (MW) — is a continuous numerical value.

---

## 4. Dataset

| | |
|---|---|
| **Dataset Name** | Combined Cycle Power Plant (CCPP) |
| **Source** | UCI Machine Learning Repository |
| **Dataset Link** | [archive.ics.uci.edu/dataset/294/combined+cycle+power+plant](https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant) |
| **Expected Size** | 9,568 rows |
| **Target Column** | `PE` — Net hourly electrical energy output (MW) |

### Main Features

| Code | Feature | Description |
|:---:|---|---|
| `AT` | Ambient Temperature (°C) | Outdoor air temperature; directly affects gas turbine combustion efficiency. |
| `AP` | Ambient Pressure (mbar) | Air pressure; influences air density entering the turbine. |
| `RH` | Relative Humidity (%) | Humidity level; affects air density and combustion. |
| `V` | Exhaust Vacuum (cm Hg) | Vacuum level from the steam turbine; affects steam cycle efficiency. |

These four ambient/environmental variables directly drive the thermodynamic efficiency of the plant's gas and steam turbines, making them strong predictors of electrical output.

### ⚙️ Preprocessing Plan

- Check for and handle any missing values
- Apply feature scaling (standardization) to the four numeric inputs to benefit distance/gradient-sensitive models
- Use an 80/20 train/test split (with a fixed random seed) applied identically across all three algorithms for a fair comparison

---

## 5. Algorithms I Plan to Train

| Algorithm | Reason for Selection |
|---|---|
| **Linear Regression** | Serves as a simple, interpretable baseline to measure how much predictive power comes from non-linear relationships in the data. |
| **Random Forest Regressor** | Captures non-linear interactions between ambient variables (e.g., temperature and humidity jointly affecting output) without requiring manual feature scaling. |
| **Gradient Boosting Regressor** | An advanced ensemble method that builds on weak learners sequentially, typically achieving the highest accuracy on smooth, non-linear tabular regression problems like this one. |

These three algorithms will be trained and compared to identify the best-performing regression model. Two (Linear Regression, Random Forest Regressor) come from the bootcamp curriculum; Gradient Boosting Regressor is researched independently via scikit-learn documentation.

---

## 6. Evaluation Plan

The following evaluation metrics will be used to compare all regression models:

- ✅ Mean Absolute Error (MAE)
- ✅ Root Mean Squared Error (RMSE)
- ✅ R² Score

### 🏆 Best Model Selection

The best model will be selected by the **highest R² Score** on the test set. Since the target (`PE`) has a narrow, well-behaved range (420–496 MW), R² gives the clearest picture of how much output variance the model explains, making it the most meaningful single metric for this operational forecasting tool.

> If two models are within **0.005** of each other on R² (a near-tie), the tie will be broken by the **lower RMSE**, since RMSE penalizes larger prediction errors more heavily — an important property for avoiding costly over/under-generation decisions.

---

## 7. Deployment Sketch

| | |
|---|---|
| **Framework** | FastAPI |
| **Endpoint** | `POST /predict` |

### Input (JSON)

```json
{
  "AT": 23.5,
  "AP": 1012.3,
  "RH": 65.0,
  "V": 45.8
}
```

### Output (JSON)

```json
{
  "predicted_power_output_mw": 452.31
}
```

The API receives four ambient sensor readings and returns the predicted net electrical power output of the plant in megawatts.

---

## 8. Repository Plan

```text
power-plant-prediction-api/
├── dataset/
│   └── ccpp_data.csv
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── api/
│   └── app.py
├── models/
│   └── best_model.pkl
├── notebooks/
│   └── experimentation.ipynb
├── README.md
├── requirements.txt
└── project_paper.md
```

This structure separates raw data, preprocessing/training code, the trained model artifact, the API layer, and documentation — keeping the project organized and easy to deploy.
