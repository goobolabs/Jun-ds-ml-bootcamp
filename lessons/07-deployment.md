# Lesson 7 – Deployment

> In **Lesson 6**, we covered Clustering — finding structure without labels. A trained model sitting on your laptop does not help users yet. Tonight we put it to work: **Deployment**.

---

## What You'll Learn

By the end of this lesson, students will be able to:

- Explain why **deployment** is a separate stage after training and evaluation.
- Save a trained model and its preprocessing artifacts with **joblib**.
- Rebuild the same features at prediction time so the API matches training.
- Serve predictions through a simple **REST API** (Flask) and call it from a UI or `curl`.
- Describe basic **monitoring** and when to **retrain** after a model is live.

---

## Why Deployment Matters

In Lessons 3–6 you built clean data, trained models, and measured metrics. That is the lab.

In the real world, a doctor, bank officer, or app does not open your Jupyter notebook. They need a **reliable way to send new inputs and get a prediction back**.

> Training answers: *“How good is this model on test data?”*  
> Deployment answers: *“How does a user get a prediction tomorrow?”*

Without deployment, the Data Science lifecycle stops early. With deployment, your model becomes a product.

---

## What is Deployment?

**Definition:**

- **Deployment** is the process of packaging a trained model (and the steps that prepare its inputs) so other systems or people can request predictions.

Typical pieces:

- A **saved model file** (not just a notebook cell).
- The **same cleaning / encoding / scaling** used in training.
- An **interface** — often a web API, sometimes a batch job or embedded app.

---

### Real-World Examples

- 🏦 **Loan approval:** An officer fills a form → API returns Approved / Rejected with confidence.
- 🏡 **House prices:** A website sends size, bedrooms, location → API returns estimated price.
- 📧 **Spam filter:** Email server sends text features → model returns spam / not spam.
- 📦 **Nightly batch:** A script scores 50,000 customers offline and writes results to a database.

---

## Common Deployment Patterns

You do not need every pattern. Beginners usually start with an **API**.

| Pattern | Idea | Good for |
| --- | --- | --- |
| REST API | Client sends JSON → server returns prediction | Apps, demos, final projects |
| Web app UI | Form in the browser talks to your API | Humans using the model |
| Batch scoring | Run predictions on a schedule (hourly/nightly) | Large offline lists |
| Embedded | Model loads inside a mobile/desktop app | Offline or low-latency devices |

> For this bootcamp (and most final projects), **API + optional UI** is enough.

---

## Saving What You Need to Serve

A model alone is not enough. At prediction time you must transform a raw request into the **same feature columns** the model saw during training.

### Save these artifacts

- **Model** — e.g. `lr_model.joblib`, `rf_model.joblib`
- **Scaler** (if you used `StandardScaler`) — e.g. `loan_scaler.pkl`
- **Column order** — e.g. `train_columns.json` so one-hot / engineered features line up

> If training scaled Income and engineered DebtToIncome, prediction must do the same. Mismatch = wrong or broken predictions.

### Saving with `joblib` and `.pkl`

`joblib` and `pickle` (often saved as `.pkl`) both **write Python objects to a file** so you can load them later without recreating them. This is called **serialization** (or pickling).

People often confuse them because they are related — but they are not the same tool.

| Feature | `pickle` (`.pkl`) | `joblib` |
| --- | --- | --- |
| What it is | Python standard library | Third-party library built on top of pickle |
| Installation | Included with Python | `pip install joblib` |
| Best for | General Python objects | Large NumPy arrays and ML models |
| Speed | Good | Usually faster for large numerical data |
| Compression | Manual | Built-in support |

#### `pickle`

Part of Python itself:

```python
import pickle

model = {"name": "My Model", "accuracy": 0.95}

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
```

#### `joblib`

Simpler API for large machine learning models (what we use in this bootcamp):

```python
import joblib

joblib.dump(model, "models/rf_model.joblib")
model = joblib.load("models/rf_model.joblib")
```

Training a model can take minutes. Saving it means you load a ready model in the API instead of retraining every time:

```python
from sklearn.ensemble import RandomForestClassifier
import joblib

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "random_forest.joblib")
# later…
model = joblib.load("random_forest.joblib")
```

#### File extensions are just names

All of these can work:

- `pickle.dump(model, file)`
- `joblib.dump(model, "model.joblib")`
- `joblib.dump(model, "model.pkl")` — same `joblib` format, different filename

The extension does **not** decide the format by itself. Still, prefer `.joblib` for joblib files and `.pkl` for pickle files so readers know what to expect. In our Goobo demo you will see both (e.g. `rf_model.joblib` and `loan_scaler.pkl`) — both are fine when saved/loaded with the matching tool.

#### Security warning

> Never load a `.pkl` or `.joblib` file from someone you do not trust.

`pickle.load(...)` and `joblib.load(...)` can run arbitrary Python code while loading. Treat these files like executables, not like safe CSVs.

#### Which should you use?

- **General Python objects** → `pickle`
- **Scikit-learn models / scalers** → `joblib` (recommended in this course)
- **PyTorch** → `torch.save()` / `torch.load()`
- **TensorFlow / Keras** → `model.save()`
- **XGBoost / LightGBM / CatBoost** → their native save/load methods when available

In practice, for scikit-learn in this bootcamp, **`joblib` is the usual choice** because it handles large NumPy-based model data efficiently.

---

## REST API Basics (Beginner View)

A **REST API** is a server that listens for HTTP requests.

For ML demos we usually need:

- `GET /` — health / docs (“what does this API expect?”)
- `POST /predict` — send features, receive a prediction

Important ideas:

- **JSON request** — client sends fields like Income, CreditScore, …
- **JSON response** — server returns label, confidence, and often echoes the input
- **Query params** — e.g. `?model=lr` or `?model=rf` to choose which saved model to use

Example request body (loan / Goobo Classifier):

```json
{
  "Income": 65000,
  "CreditScore": 720,
  "EmploymentYears": 5,
  "LoanAmount": 15000,
  "HasCollateral": "Yes",
  "PreviousDefaults": "No"
}
```

Example response shape:

```json
{
  "model": "random_forest",
  "label": "Approved",
  "prediction": 1,
  "confidence": 0.87
}
```

---

## Our Demo: Goobo Classifier

We redeploy what you built in **Lesson 5** — loan approval — as a live API branded **Goobo Classifier**.

| Piece | Role |
| --- | --- |
| Problem type | Classification (Approved vs Rejected) |
| Models | Logistic Regression + Random Forest |
| Framework | Flask + flask-cors |
| UI (optional) | Next.js client under `deployment/client/` |

Path: [`deployment/`](../deployment/)

```
deployment/
├── processing.py   # Lesson 5 cleaning + save scaler/columns
├── model.py        # Train LR + RF + save joblib (+ optional custom test)
├── utils.py        # Raw form → engineered/scaled row
├── app.py          # Flask API
├── models/         # Saved artifacts
├── client/         # Optional web UI
└── requirements.txt
```

### How the pieces connect

1. **`processing.py`** cleans the loan dataset and saves the scaler + training columns.
2. **`model.py`** trains LR and RF, prints metrics (as in Lesson 5), saves models for serving, then optionally tests a raw custom applicant via `utils`.
3. **`utils.py`** turns a raw JSON applicant into one feature row matching training.
4. **`app.py`** loads models once at startup and exposes `/predict`.

> Rule: **train once → save artifacts → load in the API → reuse `prepare_features_from_raw` for every request.**

---

## Coding Session

Run everything from the `deployment/` folder.

**Step 1 — Install API dependencies**

```bash
cd deployment
pip install -r requirements.txt
```

**Step 2 — Process data and save scaler / columns**

[`deployment/processing.py`](../deployment/processing.py)

```bash
python processing.py
```

**Step 3 — Train models and save joblib files**

[`deployment/model.py`](../deployment/model.py)

```bash
python model.py
```

This also runs an optional custom raw-input check through `prepare_features_from_raw` (same idea as the house demo).

**Step 4 — Start the API**

[`deployment/app.py`](../deployment/app.py)

```bash
python app.py
```

The API listens on port **8000**.

**Step 5 — Test with curl**

```bash
curl -X POST "http://127.0.0.1:8000/predict?model=rf" \
  -H "Content-Type: application/json" \
  -d '{
    "Income": 65000,
    "CreditScore": 720,
    "EmploymentYears": 5,
    "LoanAmount": 15000,
    "HasCollateral": "Yes",
    "PreviousDefaults": "No"
  }'
```

Try `model=lr` as well and compare labels / confidence.

**Step 6 — (Optional) Start the UI**

```bash
cd client
npm install
npm run dev
```

Open http://localhost:3000 — the form should call your Flask API.

More detail: [`deployment/README.md`](../deployment/README.md).

---

## What Happens Inside `/predict`

When a request arrives:

1. Read `?model=lr|rf` and pick the loaded model.
2. Read JSON body; reject the request if required fields are missing.
3. Call `prepare_features_from_raw(...)` — binary Yes/No mapping, DebtToIncome, IncomePerYearEmployed, scaling.
4. Run `model.predict` (and `predict_proba` for confidence).
5. Return JSON: model name, input echo, prediction, label, confidence.

This is the same idea for **any** project API — house prices, diabetes risk, flight delay — only the fields and preprocessing change.

---

## After Launch: Monitoring and Retraining

Deployment is not “file and forget.”

### Watch for

- **Performance drop** — accuracy / F1 / business KPIs worse than in testing.
- **Data drift** — new applicants look different (incomes, credit scores, etc.).
- **Broken inputs** — missing fields, typos, unexpected categories.
- **Latency / errors** — API timeouts or 500 responses.

### When to retrain

- Enough new labeled data arrives.
- Product rules change (e.g., new collateral policy).
- Metrics show the model no longer matches reality.

Retrain with the same pipeline, save new artifacts, and redeploy — do not silently change columns without updating `utils.py`.

---

## For Your Final Project

Your capstone expects a **served model**, not only a notebook:

- Save the best model (+ scaler / columns if needed).
- Expose a `/predict` (or equivalent) endpoint.
- Document the JSON input fields clearly.
- Optional: a small UI that calls your API.

Use this Goobo Classifier folder as the template: process → train/save → utils → Flask app.

---

## Summary

- **Deployment** makes a trained model available to users and other systems.
- Save the **model** and everything needed for **identical preprocessing** at prediction time.
- Use **`joblib`** (preferred for scikit-learn) or **`pickle`** to serialize models — never load untrusted `.pkl` / `.joblib` files.
- A beginner-friendly pattern is a **Flask REST API** (`POST /predict`) plus an optional web UI.
- Our demo reuses the **Lesson 5 loan classifier** as **Goobo Classifier** under [`deployment/`](../deployment/).
- Run: `processing.py` → `model.py` → `app.py`, then test with curl or the Next.js client.
- After go-live, **monitor** performance and **retrain** when data or metrics drift.
- **Next (optional):** Continue with the [bonus guides](../bonus/README.md) — Deep Learning, math refreshers, AI/GenAI, career path, portfolio, and ethics.

---

*Lesson 7 of 7*

*End of Lesson 7*
