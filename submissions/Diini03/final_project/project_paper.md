# Project Paper — Somalia Displacement Severity Classifier

**Bootcamp:** Goobo Labs DS/ML Bootcamp 2026
**Repository:** https://github.com/Diini03/somalia-displacement-classifier

- **API:** Render — https://somalia-displacement.onrender.com
- **UI:** — https://displacement-som.diinikahiye.online
  **Date:** July 2026

---

## 1. Problem Statement and Motivation

In Somalia, displacement events happen constantly — people are forced to leave their homes because of armed conflict, drought, or flooding. Humanitarian organizations like UNHCR, OCHA, and Medair operate across the country and have to decide where to send resources before they fully know how serious a situation will become. If they wait for complete information, they have already lost the window to respond effectively.

The question this project tries to answer is: given early information about a displacement event — what caused it, where it happened, when it started, and how long it lasted — can a machine learning model predict whether it will displace a large number of people?

A correct early prediction gives field teams and logistics coordinators a one to three week window to pre-position emergency supplies, shelter, and medical staff before a crisis peaks. In humanitarian response, that window is the difference between an organized response and a reactive scramble.

This project was built using real displacement event records from Somalia, collected and published by the Internal Displacement Monitoring Centre through the Humanitarian Data Exchange. The data is not simulated or synthetic — it reflects actual events recorded by field monitors across Somalia between 2025 and 2026.

---

## 2. Dataset and Preprocessing

**Source:** Internal Displacement Monitoring Centre (IDMC) via Humanitarian Data Exchange (HDX)
**Link:** https://data.humdata.org/dataset/som-idmc-idu-events
**Size:** 3,091 displacement events, 36 columns

The raw dataset contains one row per recorded displacement event, with columns covering the cause, location, number of people displaced, event dates, geographic coordinates, and source organization. Most of the columns — event names, source URLs, description text — are not useful for a machine learning model. The modeling work focused on extracting the signal from the structured fields.

**Target variable:** A new binary column called `is_large` was created. An event is labeled large (1) if it displaced more than 50 people, and small (0) otherwise. This threshold was chosen after analyzing the distribution — at 50 people, 18.6% of events are classified as large, which gives the model enough positive examples to learn from. A higher threshold of 100 only produces 12.8% positive cases, which makes the class imbalance harder to handle.

**Features engineered:**

The following features were extracted or derived from the raw columns:

- `combined_enc` — cause of displacement encoded as a number: Conflict, Drought, or Flood
- `displace_enc` — displacement type: Conflict or Disaster
- `region_enc` — the Somalia region where the event occurred, extracted from the location name field
- `month` — month of the displacement start date
- `week_of_year` — approximate week, useful for capturing seasonal patterns
- `duration_days` — days between start and end of the event
- `latitude` and `longitude` — geographic coordinates
- `lat_lon_interact` — product of latitude and longitude, adds a geographic interaction term
- `rainy_season` — a derived feature: 1 for the Gu rains (March to May), 2 for the Deyr rains (October to November), 0 for dry seasons
- `is_flood` and `is_conflict` — binary flags for specific causes
- `year` — the event year

**Preprocessing steps:** missing values in duration and coordinates were filled with zero and Somalia centroid coordinates respectively. Region names were extracted from the location string, standardized, and the top 12 most common regions were kept with all others grouped as Other. No scaling was applied since tree-based models do not require it.

---

## 3. Algorithms

Three models were trained on the same 80/20 stratified train/test split with `random_state=42`.

**Logistic Regression** was included as the baseline. It applies a sigmoid function to a weighted sum of the input features and outputs a probability. With `class_weight='balanced'` and a regularization parameter of C=0.1, it achieved very high recall but at the cost of almost no precision — it predicted nearly everything as large. This is a common failure mode for logistic regression on heavily imbalanced tabular data where the decision boundary is non-linear.

**Random Forest** was the second model and ultimately the deployed one. It builds 500 decision trees, each trained on a random subset of the data and features. Predictions are made by majority vote across all trees. With `class_weight='balanced'` and `max_depth=10`, it achieved Recall of 0.826, F1-Score of 0.492, and ROC-AUC of 0.818. The ensemble structure helps it generalize well on a dataset where the patterns are complex and non-linear — a flood in Banaadir during April behaves differently from a drought in Sanaag in January, and the forest captures those interactions naturally.

**XGBoost** was the third model, a gradient boosting algorithm that builds trees sequentially, with each new tree correcting the errors of the previous one. It was trained with `scale_pos_weight` set to the ratio of negative to positive examples to handle class imbalance, with 300 estimators and a learning rate of 0.03. It achieved Recall of 0.817, F1-Score of 0.482, and ROC-AUC of 0.811 — slightly below Random Forest on all metrics.

---

## 4. Results and Discussion

| Model               | Recall | Precision | F1-Score | Accuracy | ROC-AUC |
| ------------------- | ------ | --------- | -------- | -------- | ------- |
| Logistic Regression | 0.991  | 0.188     | 0.315    | 0.200    | 0.544   |
| Random Forest       | 0.826  | 0.351     | 0.492    | 0.683    | 0.818   |
| XGBoost             | 0.817  | 0.342     | 0.482    | 0.674    | 0.811   |

**Best model: Random Forest**

Random Forest was selected as the deployed model based on ROC-AUC (0.818), F1-Score (0.492), and overall accuracy (0.683). While Logistic Regression achieved the highest recall, its precision of 0.188 and accuracy of 0.200 reveal that it was predicting almost everything as a large event — a strategy that cannot be used in practice because it would trigger an emergency response for every single event recorded.

Random Forest achieves a genuine balance. It catches 82.6% of actual large events (Recall) while maintaining enough precision to avoid flooding field teams with false alarms. The AUC of 0.818 confirms the model has real discriminative power — it is not just guessing based on class frequency.

The prediction threshold was lowered from the default 0.5 to 0.35. This is a deliberate decision rooted in the humanitarian context: the cost of missing a large displacement event (arriving unprepared to a crisis) is far higher than the cost of a false positive (pre-positioning resources for an event that turns out to be small). A lower threshold shifts the decision boundary to catch more large events at the cost of some additional false alarms, which is the correct tradeoff for this application.

**Sanity checks:**

Three sample predictions from the test set were reviewed manually. In each case the model's predicted label matched the known outcome, and the probability scores were in line with the features — a Flood event in Banaadir during April at high confidence, a Drought event in Sanaag during February at low confidence. The model behaves sensibly on real examples.

---

## 5. Deployment Notes

The project is deployed as a two-part web application.

The backend is a FastAPI application that loads the trained Random Forest model and its associated artifacts (label encoders, model configuration) and exposes a `/predict` endpoint. The endpoint accepts a JSON body with the cause, region, month, duration, coordinates, and year of a displacement event and returns a prediction, probability, severity label, and recommended action. A `/metrics` endpoint returns the performance statistics of all three trained models.

The frontend is a static HTML, CSS, and JavaScript application with no Python dependency. It presents a two-column layout: the left side explains what the tool does and how to read the results, including a regional breakdown of historical large event rates; the right side contains a four-field form where users enter event details and receive a prediction. The prediction result shows the label, confidence bar, severity badge, and recommended response.

The backend is deployed on Render and the frontend is deployed on Vercel.

Example API request:

```bash
curl -X POST https://somalia-displacement-classifier.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "combined_type": "Flood",
    "displacement_type": "Disaster",
    "region": "Banaadir",
    "month": 4,
    "duration_days": 7,
    "latitude": 2.04,
    "longitude": 45.34,
    "year": 2026,
    "model": "rf"
  }'
```

Example response:

```json
{
  "prediction": "Large Event",
  "is_large": 1,
  "probability": 0.81,
  "severity": "Critical",
  "color": "critical",
  "action": "Immediate deployment required — pre-position emergency shelter, food, and medical teams now.",
  "model_used": "rf",
  "model_name": "Random Forest"
}
```

---

## 6. Lessons Learned

The most important lesson from this project is about target design. The first version used a threshold of 100 people to define a large event, which left only 12.8% of examples as positive cases. The model struggled to learn from so few examples. Changing the threshold to 50 — a number that still represents a genuine humanitarian concern — improved the class balance to 18.6% and led to significantly better model performance without changing any other part of the pipeline.

The second lesson is about threshold tuning. Machine learning classifiers do not have to use a decision threshold of 0.5. For this problem, the right threshold is lower because the cost of the two error types is asymmetric. Understanding this and acting on it — lowering the threshold to 0.35 — was a meaningful improvement that came from thinking about the domain, not just the metrics.

The third lesson is about the limits of tabular data for this problem. The data covers only 2025 and 2026, which is a short time window. A model trained on one year and evaluated on another would be a stronger test of generalization. As IDMC continues to publish data, adding historical records from 2020 to 2024 would likely improve both model quality and confidence in the results. The current model is a strong starting point, but it would benefit from more data over time.
