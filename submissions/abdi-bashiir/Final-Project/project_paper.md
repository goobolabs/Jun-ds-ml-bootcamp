# Power Plant Energy Output Prediction API — Project Paper

**Author:** Abdidahir Bashir Ali

---

## 1. Problem Statement and Motivation

### Why This Problem

Electricity is one of the subjects I am most interested in learning more about, and this project was chosen as an opportunity to apply machine learning to a real problem in that space.

Combined cycle power plants must constantly balance the electricity they generate with the demand placed on the grid, but their output is not constant — it changes continuously with ambient conditions such as temperature, pressure, and humidity.

### Why It Matters

Without a prediction tool like the one built in this project, plant operators would have to rely on guesswork or manual calculations to estimate how much power the plant will produce under current conditions. This creates a real risk of:

- **Over-generation** — wasting electricity and money
- **Under-generation** — destabilizing the grid and requiring costly emergency responses

This problem matters especially because ambient conditions change constantly throughout the day and across seasons, making manual estimation unreliable and a data-driven forecasting tool genuinely useful for operational planning.

---

## 2. Dataset and Preprocessing

### Dataset Overview

- **Source:** Combined Cycle Power Plant (CCPP) dataset, UCI Machine Learning Repository
- **Size:** 9,568 rows, collected from a real power plant over six years of operation
- **Why this dataset:** it directly matches the project's regression problem — continuous ambient sensor readings paired with the actual measured electrical output of the plant

### Target and Features

- **Target:** `PE` — net hourly electrical energy output, in megawatts
- **Raw input features**, each with a direct physical relationship to turbine efficiency:
  - `AT` — Ambient Temperature (°C)
  - `AP` — Ambient Pressure (millibar)
  - `RH` — Relative Humidity (%)
  - `V` — Exhaust Vacuum (cm Hg)

### Preprocessing Steps

1. **Missing-value check** — none were found
2. **Feature engineering** — four additional features created to capture non-linear/interaction effects a purely linear model would miss:
   - `AT_x_RH`, `AT_x_AP`, `AT_squared`, `AT_div_V`
3. **Train/test split** — 80/20, fixed random seed, so all three algorithms were compared on exactly the same split
4. **Standardization** — `StandardScaler` fitted only on the training set, then applied to both sets, to avoid data leakage

---

## 3. Algorithms

Three regression algorithms were trained and compared on the same train/test split.

### Linear Regression
A simple, interpretable baseline. It models the target as a weighted linear combination of the input features — fast to train, easy to reason about, and a reference point for measuring how much predictive power comes from non-linear relationships in the data.

### Random Forest Regressor
An ensemble method that builds many decision trees on different random subsets of the data and features, then averages their predictions. Included because it can capture non-linear interactions between ambient variables — such as temperature and humidity jointly affecting output — without requiring feature scaling, and it tends to be robust to noise in tabular data.

### Gradient Boosting Regressor
Researched independently. Builds trees sequentially, with each new tree correcting the errors of the ones before it. Included as a more advanced ensemble approach that typically performs well on smooth, non-linear tabular regression problems similar to this one.

> Two of the three algorithms (Linear Regression and Random Forest) come from the bootcamp curriculum; Gradient Boosting was researched independently through scikit-learn's documentation.

---

## 4. Results and Discussion

### Model Comparison

All three models were evaluated on the same held-out test set:

| Algorithm | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 3.385 | 4.255 | 0.9376 |
| Random Forest | **2.350** | **3.261** | **0.9633** |
| Gradient Boosting | 2.929 | 3.802 | 0.9502 |

### Best Model Selection

The best model was selected using the highest R² Score, with the lower RMSE used as a tie-breaker whenever two models were within 0.005 of each other on R².

**Random Forest Regressor** achieved the best result on every metric (R² = 0.9633, RMSE = 3.261 MW), with a margin over the second-best model (Gradient Boosting) well above the tie-break threshold — no tie-break was needed.

### Discussion

- Random Forest's clear advantage over the purely linear baseline suggests the relationship between ambient conditions and power output is meaningfully **non-linear** — consistent with the physical intuition that turbine efficiency doesn't respond to temperature, pressure, humidity, and vacuum in a simple additive way.
- **Sanity checks:** three held-out sample predictions differed from actual measured output by roughly **1–5 MW**, against a real output range of 420–496 MW — an error of **under 1%**, indicating the deployed model generalizes well to unseen data.

---

## 5. Deployment Notes

### API

The best model (Random Forest Regressor) and its feature scaler were deployed as a REST API built with **FastAPI**, exposing a single `POST /predict` endpoint.

**Request:**
```json
{"AT": 23.5, "AP": 1012.3, "RH": 65.0, "V": 45.8}
```

**Response:**
```json
{"predicted_power_output_mw": 452.95}
```

The endpoint reconstructs the same engineered features used during training before generating a prediction.

### Frontend

A web-based frontend was also built (`static/index.html`), styled as an industrial control-panel dashboard:
- Users adjust the four ambient readings using sliders
- Predicted output is displayed on an animated analog-style gauge
- The frontend communicates with `/predict` directly from the browser using JavaScript's `fetch()` API

### Testing

The API was tested locally using `curl`, PowerShell's `Invoke-RestMethod`, and directly through the browser frontend — all returned correct predictions consistent with the model's evaluation results.

---

## 6. Lessons Learned

### Biggest Challenge

The most difficult part of the project was not the modeling itself but the environment and deployment setup around it:

- After the initial model was trained, I noticed a small issue in how it had been built and decided to rebuild the environment from scratch — which introduced its own complications, since some tools and dependencies had to be reinstalled and reconfigured.
- Later, deploying the API, I ran into a **port conflict**: an older `uvicorn` process from a previous session was still holding port 8000 in the background without my knowledge, so the API kept responding with stale results even after the code was fixed. I resolved this by identifying and terminating the leftover process, then running the server on a different port to avoid the conflict entirely.

### What I Learned

- How APIs actually function in practice — how a client sends a request and a server processes it and returns a response
- Why feature scaling has to be applied *after* the train/test split, fitting only on the training data, so information from the test set never leaks into training — understanding data leakage in this concrete way was one of the more valuable takeaways

### What I Would Do Differently

If I were to build this project again, I would spend more time earlier on designing a more polished, professional-looking frontend, rather than treating it as an afterthought once the API was already working.

### Future Improvements

I would like to extend the model with additional input features that could affect prediction accuracy depending on the type of power plant:

- **Fuel Flow Rate**
- **Fuel Quality / Calorific Value**
- **Operating Hours (Age)** — older machines tend to run less efficiently than newer ones

None of these factors are captured by the current ambient-only feature set.
