

# Mobile Price Range Classification — Project Paper

**Author:** SAKARIYE JAMAC

**Project:** Final Project — ML Model Development and Deployment

**Repository:** https://github.com/sakijamac4-lab/Mobile-Price-Range-Classification-.git

---

## 1. Problem Statement and Motivation

Mobile phone manufacturers and retailers need a fast, data-driven way to position a
new device within the market — deciding whether a phone belongs in the budget,
mid-range, high-end, or flagship price tier based on its hardware specifications
alone, before a final retail price is set.

This project frames that decision as a **multi-class classification problem**: given
a set of hardware specifications for a mobile phone (battery capacity, camera
resolution, RAM, screen resolution, storage, and 4G support), predict which of four
price tiers the phone belongs to:

- **0 — Low cost**
- **1 — Medium cost**
- **2 — High cost**
- **3 — Very High cost**

Price-tier prediction is an important task that's used regularly in the mobile phone market. 
It can help companies decide on product pricing, compare themselves against competitors,
and build apps that offer recommendations. It's also a great fit as a capstone project 
because it covers all the tasks taught in the bootcamp: data cleaning, feature engineering, 
multi-class classification, and real API deployment.

---

## 2. Dataset and Preprocessing

### 2.1 Source

Source: https://www.kaggle.com/datasets/navjotkaushal/mobile-price-classification-dataset/data
The dataset contains 2,000 mobile phone records downloaded from Kaggle.

### 2.2 Features

After cleaning, the following 8 raw features are used, plus one engineered feature:

| Feature | Description |
|---|---|
| `Battery_power_mAh` | Battery capacity in mAh |
| `Front_camera` | Front camera resolution (MP) |
| `4G` | Whether the phone supports 4G (Yes/No) |
| `Internal_memeory_gb` | Internal storage (GB) |
| `Primary_camera` | Rear camera resolution (MP) |
| `px_height` | Screen resolution height (pixels) |
| `Pixel_width` | Screen resolution width (pixels) |
| `Ram_mb` | RAM (MB) |
| `total_pixels` *(engineered)* | `px_height × Pixel_width` — a proxy for overall screen resolution/quality that isn't directly present in the raw data |

The target label is `price_range` (0–3, described above).

### 2.3 Preprocessing pipeline (`processing.py`)

All cleaning is implemented in code, not just described on paper:

1. **Column selection** — keep only the 8 raw features plus the label.
2. **Duplicate removal** — `drop_duplicates()` to avoid inflating any one phone
   profile's influence on training.
3. **Categorical typo normalization** — the raw `4G` column contains inconsistent
   values (`"yes"`, `"Yse"`, `"1"`, etc.); a mapping dictionary
   normalizes all variants to a clean `"Yes"`/`"No"` before encoding.
4. **Unit stripping** — several numeric columns arrive with units baked into the
   string (e.g. `"1500mAh"`, `"13MP"`, `"32GB"`); a regex extracts the numeric
   portion and casts it to `int`.
5. **IQR-based outlier capping** — for each of the 7 numeric columns, the
   interquartile range (Q1–Q3) is computed and values are clipped to
   `[Q1 − 1.5×IQR, Q3 + 1.5×IQR]`. This limits the influence of a small number of
   extreme phone specs without discarding rows outright.
6. **Label encoding** — `4G` → `{No: 0, Yes: 1}`; `price_range` →
   `{Low cost: 0, Medium cost: 1, High cost: 2, Very High cost: 3}`.
7. **Feature engineering** — `total_pixels = px_height × Pixel_width`, added
   *after* the target is encoded so there is no leakage from the label into the
   feature.
8. **Scaling** — all numeric (non-binary, non-label) columns are scaled with
   **`RobustScaler`** (median/IQR-based).

The fitted scaler, the training feature-column order, and the list of scaled
columns are all persisted to `models/` (`scaler.pkl`, `train_columns.json`,
`scale_cols.joblib`) so that the exact same transformation can be replayed at
inference time on a single new phone — this is what makes the deployment step in
Section 5 possible without re-fitting anything on live traffic.

---

## 3. Algorithms

Four classifiers were trained on an identical, stratified 80/20 train/test split
(`random_state=42`), so all comparisons below are apples-to-apples:

### 3.1 Logistic Regression
A linear baseline (`max_iter=1000`). Chosen because it is fast, interpretable, and
gives a useful lower bound: if a tree-based model can't clearly beat it, the extra
complexity may not be worth it.

### 3.2 Decision Tree
A single tree classifier. Chosen as a simple non-linear baseline that can capture
threshold-style rules (e.g. "RAM > X and battery > Y") that a linear model cannot,
at the risk of overfitting on a dataset this size.

### 3.3 Random Forest
An ensemble of 200 trees (`n_estimators=200`). Chosen because it generally
generalizes better than a single Decision Tree by averaging over many
de-correlated trees, and it is one of the two required bootcamp algorithms.

### 3.4 XGBoost
A gradient-boosted tree ensemble (`n_estimators=200`, `eval_metric="mlogloss"`).
Chosen as the "researched independently" algorithm beyond the bootcamp core —
gradient boosting typically outperforms bagging (Random Forest) on structured
tabular data like this one, because trees are added sequentially to correct the
previous ensemble's errors rather than being built independently.



---

## 4. Results and Discussion

### 4.1 Comparison table



| Algorithm | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) |
|---|---|---|---|---|
| Logistic Regression | 0.9625 | 0.9626 | 0.9625 | 0.9624 |
| XGBoost | 0.9425 | 0.9424 | 0.9425 | 0.9423 |
| Random Forest | 0.9350 | 0.9350 | 0.9350 | 0.9350 |
| Decision Tree | 0.8675 | 0.8697 | 0.8675 | 0.8680 |

The best model is chosen based on the macro F1-score, not plain accuracy. 
The reason: F1-score evaluates all four price tiers (Low, Medium, High, Very High) equally 
it doesn't matter how many phones fall into each tier.

For example, if a model does well on Medium and High (the middle tiers, which have the most data), 
but performs poorly on Low and Very High (the extreme tiers), accuracy could end up looking high 
but that's misleading, since the model isn't actually handling the easier tiers well.
F1-score corrects for that bias by scoring each tier equally.

That's why model.py uses F1-score alone to determine the best model, and automatically prints its name.


Winning model: Logistic Regression won on the real data with an F1-score of 0.9624, outperforming the runner-up, XGBoost (0.9423), by a margin of ~0.0201 (about 2.01 percentage points).
### 4.2 Confusion matrix discussion

model.py also prints a full 4×4 confusion matrix for every model, showing where the model got its predictions wrong. When analyzing this table, look at two things:

1. Type of error: Is it an error between adjacent tiers (e.g., Medium wrongly predicted as High), or an error between tiers that are far apart (e.g., Low wrongly predicted as Very High)?

Errors between adjacent tiers are expected — this is normal, since mobiles near adjacent tiers share similar characteristics, so it doesn't need much concern.
Errors between tiers that are far apart (Low → Very High) are concerning and indicate the model isn't classifying well — you should look at how to prevent this.

2. Underperforming class: Is there one tier (e.g., Very High) that the model consistently gets wrong, predicting other tiers instead?

Once you have the actual confusion matrices, you'll write here what you observe — for example, "most errors occur between Medium and High, which is expected" or "the model consistently misclassifies Very High as High, indicating it struggles to distinguish the highest tier."

Across all four models, the errors are concentrated entirely in adjacent tiers, with no errors between tiers that are far apart (Low ↔ Very High). Logistic Regression has the fewest errors overall. Decision Tree has the most errors, particularly for the High class (18% of true High phones were misclassified as either Medium or Very High). Random Forest and XGBoost fall in between — more errors than Logistic Regression but fewer than Decision Tree. No single class is consistently underperforming across all models, but High appears to be the hardest tier to classify correctly

### 4.3 Sanity checks

Beyond the automated metrics computed on the test set, there are two other kinds of checks that verify the model's predictions:

1. Single-row check: Section 7 of model.py takes one held-out phone and prints both the true label (what it actually was) and each model's prediction. This serves as a quick check showing whether the models perform sensibly on a specific phone.

2. Three hand-written predictions: Three custom phone specifications (one budget, one mid-range, one flagship) were run through the deployed model using the same function (prepare_features_from_raw()) that the live API uses. The goal is to confirm that a hand-written spec produces a sensible price tier — for example, a phone with low battery, low RAM, and a weak camera should come out as Low cost, while one with high RAM and a good camera should come out as High or Very High.

Both checks matter because metrics like F1-score are aggregate numbers that don't show whether the model is correct on specific, concrete cases — these checks confirm that "what I measured" and "what actually happens" line up.

| # | Input summary | Predicted price range |
|---|---|---|
| 1 | 1000mAh, 7MP front, 16GB, 4G | Low cost (0) |
| 2 | 1500mAh, 5MP front, 32GB, 4G | High cost (2) |
| 3 | 1500mAh, 5MP front, 64GB, 4G | Very High cost (3) |


---

## 5. Deployment Notes

### 5.1 API

The winning model can be used through a FastAPI app (app.py) — this is a type of app that can be 
served directly over the internet. Each of the four trained models (Logistic Regression,Decision Tree, 
Random Forest, XGBoost) is saved separately in its own file (lr_model.joblib, 
dt_model.joblib, rf_model.joblib, xgb_model.joblib).

The reason: if a user wants to switch to using Random Forest or XGBoost directly, 
they can add a small parameter to the request URL (a query parameter) to choose the model
they want. If nothing is specified, the API automatically defaults to Logistic Regression.

This matters because it allows a single API to showcase and compare all four models  instead of only deploying one

```
POST /predict?model=lr|dt|rf|xgb
```

**Request body:**

```json
{
  "Battery_power_mAh": 1500,
  "Front_camera": 5,
  "4G": "Yes",
  "Internal_memeory_gb": 32,
  "Primary_camera": 13,
  "px_height": 800,
  "Pixel_width": 1200,
  "Ram_mb": 2048
}
```

**Response:**

```json
{
  "model": "Logistic Regression",
  "input": { "...": "echoed back" },
  "prediction": 0,
  "label": "Low cost",
  "confidence": 0.42
}
```

`confidence` is the predicted-class probability from `predict_proba`, available
for all four models.

### 5.2 Serving-time preprocessing (`utils.py`)

When a request arrives at the API, it comes in as raw, uncleaned JSON (e.g., "4G": "Yes") — not in the properly scaled format the model expects. utils.py bridges this gap between the raw incoming data and what the model needs:

1. _to_binary(): This function takes the 4G value in whatever form it arrives — "Yes"/"No", 1/0, or true/false — and converts all of them into a consistent format of 0 or 1, so the model can understand it.

2. prepare_features_from_raw(): This function performs three steps in sequence:

It reconstructs the total_pixels feature (by multiplying px_height and Pixel_width), since the incoming data doesn't include it.
It reorders the columns so they match the same order used during training (train_columns.json) — if the order were different, the model would misinterpret the features.
It applies the already-fitted RobustScaler (.transform() only, never .fit_transform()), so that the single new incoming phone is scaled the exact same way the training data was scaled.

The reason all of this matters: if a new phone went through steps that didn't match the training data (for example, if a new scaler were fit instead of using the original one), the model would produce a wrong prediction — without raising any error. That's why utils.py ensures every new phone follows the exact same steps the training data went through.

### 5.3 Frontend (extra credit)

A lightweight static frontend (`client/index.html`) is included — a single HTML
file with an embedded form and JavaScript `fetch()` call, requiring no build step
(no Node.js/Next.js). It lets a user fill in phone specs, pick a model from a
dropdown, and see the predicted tier, confidence, and a visual price-tier gauge.
CORS is enabled on the FastAPI app (`CORSMiddleware`) so the static page can call
the API directly from the browser.

**Example curl test:**

```bash
curl -X POST "http://127.0.0.1:8000/predict?model=xgb" \
  -H "Content-Type: application/json" \
  -d '{
    "Battery_power_mAh": 1500,
    "Front_camera": 5,
    "4G": "Yes",
    "Internal_memeory_gb": 32,
    "Primary_camera": 13,
    "px_height": 800,
    "Pixel_width": 1200,
    "Ram_mb": 2048
  }'
```

---

## 6. Lessons Learned

- Train/inference parity is the hardest part of deployment, not the modeling. Most of the deployment work wasn't about choosing an algorithm — it was making sure a raw, uncleaned JSON phone spec goes through the exact same transformations (unit stripping, total_pixels engineering, scaling) as the training data, in the same column order, using the same fitted scaler rather than a freshly-fit one. A mismatch here can silently produce wrong predictions without ever raising an error.

- Scaler choice (RobustScaler vs StandardScaler) matters a lot for outlier-prone tabular data. Switching from StandardScaler to RobustScaler was a deliberate choice after recognizing that phone specs (battery, RAM, camera MP) commonly contain outliers, and that median/IQR-based scaling is less distorted by them than mean/std-based scaling. This choice taught me that every preprocessing step needs to be evaluated against the specific data, rather than defaulting to a generic decision without justification.

- Flexible input validation vs. strict schemas is a real trade-off. A strict Pydantic schema (4G: int with ge=0, le=1) rejects anything that isn't exactly 0 or 1, which is safer but less forgiving for API consumers who naturally send "Yes"/"No". Adding a small _to_binary() normalization function at the preprocessing boundary — rather than loosening validation everywhere — kept the API both flexible and safe.

- Saving all trained models, not just the winner, adds real value for very little extra cost. Persisting all four models (not just the best-by-F1 one) let the API expose a ?model= selector, useful for demonstrating and comparing the algorithms live rather than only trusting a single offline metric.



