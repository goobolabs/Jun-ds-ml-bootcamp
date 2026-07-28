# ⚡ Power Plant Energy Output Prediction API

Predicting the net hourly electrical energy output of a combined cycle power plant from ambient sensor readings, and serving the best-performing model through a FastAPI `/predict` endpoint.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Deployed-009688)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E)
![License](https://img.shields.io/badge/status-complete-brightgreen)

**Repository:** [github.com/abdi-bashiir/power-plant-prediction-api](https://github.com/abdi-bashiir/power-plant-prediction-api)

---

## Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Algorithms Trained](#algorithms-trained-3)
- [Results — Model Comparison](#results--model-comparison)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [API Usage](#api-usage)
- [Notes on Scope Changes](#notes-on-scope-changes-from-the-proposal)

---

## Project Description

Combined cycle power plants must constantly balance electricity supply with grid demand, but their electrical output is highly sensitive to ambient environmental conditions such as temperature, pressure, and humidity.

This project trains and compares three regression algorithms to predict net hourly electrical energy output (`PE`, in megawatts) from four ambient sensor readings, then deploys the best-performing model as a REST API.

**Who benefits:** plant operators and grid management systems, who can use these predictions to plan load dispatch and avoid over- or under-generation.

---

## Dataset

| | |
|---|---|
| **Name** | Combined Cycle Power Plant (CCPP) |
| **Source** | [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant) |
| **Size** | 9,568 rows |
| **Target** | `PE` — Net hourly electrical energy output (MW) |

### Input Features

| Feature | Description |
|:---:|---|
| `AT` | Ambient Temperature (°C) |
| `AP` | Ambient Pressure (millibar) |
| `RH` | Relative Humidity (%) |
| `V` | Exhaust Vacuum (cm Hg) |

**Engineered features** *(added in `src/preprocess.py`)*: `AT_x_RH` · `AT_x_AP` · `AT_squared` · `AT_div_V` — interaction and polynomial terms that help capture non-linear relationships between ambient conditions and power output.

### Preprocessing Pipeline

```
Missing-value check  →  Feature engineering  →  80/20 split  →  StandardScaler (fit on train only)
```

---

## Algorithms Trained (3)

| Algorithm | Source | Why it was included |
|---|:---:|---|
| Linear Regression | Bootcamp | Simple, interpretable baseline |
| Random Forest Regressor | Bootcamp | Captures non-linear interactions, no scaling required |
| Gradient Boosting Regressor | Independent research | Sequential ensemble, strong on smooth non-linear data |

All three were trained on the **same train/test split** for a fair comparison.

---

## Results — Model Comparison

| Algorithm | MAE | RMSE | R² |
|---|:---:|:---:|:---:|
| Linear Regression | 3.385 | 4.255 | 0.9376 |
| **Random Forest** 🏆 | **2.350** | **3.261** | **0.9633** |
| Gradient Boosting | 2.929 | 3.802 | 0.9502 |

> **Best model: Random Forest Regressor** (R² = 0.9633, RMSE = 3.261 MW)
>
> **Selection rule:** highest R² Score; ties within 0.005 broken by lower RMSE. Random Forest won outright, well above the tie-break threshold.

**Key finding:** Random Forest outperformed both alternatives on every metric, confirming the relationship between ambient conditions and power output is meaningfully non-linear. Sanity checks on held-out samples showed prediction errors of roughly **1–5 MW** against actual values in the 420–496 MW range — **under 1% relative error**.

---

## Repository Structure

```text
power-plant-prediction-api/
├── dataset/
│   └── ccpp_data.csv
├── src/
│   ├── preprocess.py     # missing-value check, feature engineering, split & scale
│   ├── train.py          # trains all 3 models, prints comparison table, saves best model
│   └── evaluate.py       # reloads saved model, verifies metrics, sanity checks, plots
├── api/
│   ├── app.py            # FastAPI app exposing POST /predict
│   └── static/
│       └── index.html    # control-panel style prediction dashboard
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
├── notebooks/
│   ├── *_actual_vs_predicted.png
│   └── feature_importance.png
├── README.md
├── requirements.txt
└── project_paper.md
```

---

## How to Run

### 1 · Install dependencies

```bash
pip install -r requirements.txt
```

### 2 · Train the models

```bash
python src/train.py
```
> Prints a missing-value report, the comparison table, the selected best model, and 3 sanity-check predictions. Saves `models/best_model.pkl` and `models/scaler.pkl`.

### 3 · Evaluate the saved model *(optional — independent verification)*

```bash
python src/evaluate.py
```
> Reloads the saved model and scaler, re-verifies metrics, prints sanity checks, and saves plots to `notebooks/`.

### 4 · Run the API

```bash
uvicorn api.app:app --reload
```
> Available at **http://127.0.0.1:8000** — visit `/` in a browser for the interactive dashboard.

---

## API Usage

**Endpoint:** `POST /predict`

<table>
<tr><th>curl</th><th>PowerShell</th></tr>
<tr>
<td>

```bash
curl -X POST \
  http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"AT": 23.5, "AP": 1012.3,
       "RH": 65.0, "V": 45.8}'
```

</td>
<td>

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/predict" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"AT": 23.5, "AP": 1012.3,
          "RH": 65.0, "V": 45.8}'
```

</td>
</tr>
</table>

**Example response:**

```json
{
  "predicted_power_output_mw": 452.95
}
```

---

## Notes on Scope Changes from the Proposal

The approved proposal listed four raw sensor features. During implementation, four additional **engineered features** (`AT_x_RH`, `AT_x_AP`, `AT_squared`, `AT_div_V`) were added to help the models capture non-linear interactions between ambient conditions.

The three algorithms, evaluation metrics, and best-model selection rule are unchanged from the proposal.

---

<p align="center"><i>Built as part of the Goobo Labs DS/ML Bootcamp final capstone project.</i></p>
