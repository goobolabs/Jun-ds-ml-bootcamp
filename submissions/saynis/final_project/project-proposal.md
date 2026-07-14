# Final Project Proposal

## 1. Certificate Name

**Mahamed Abdi Fatah**

## 2. Project Title and Description

### SuuqPulse AI: Hidden Market Regime Discovery and Staple Food Price Shock Prediction

SuuqPulse AI is a two-stage machine learning project that will analyze staple-food prices in Somalia and Ethiopia. First, an unsupervised model will discover hidden market regimes by grouping market–commodity pairs with similar price behavior. Second, supervised classification models will use recent price movements and the discovered regime to predict whether a price shock is likely to happen in the following month.

The project could support NGOs, government agencies, food-security teams, traders, and market-monitoring organizations. It is intended as an early-warning and decision-support tool, not as a replacement for expert market analysis.

## 3. Problem Type

This project combines **clustering** and **classification**.

The first stage is an unsupervised clustering problem. K-Means will discover groups of market–commodity pairs with similar historical behavior without using a target label.

The second stage is a supervised binary classification problem. It will predict:

- **Price Shock**
- **Normal Price Movement**

The target column will be named `price_shock_next_month`. A row will initially be labelled as a Price Shock when the following month's price increases by at least 15% compared with the current month. The threshold may be reviewed during exploratory analysis, but the same final rule will be used for all supervised models.

The API will return both the discovered market regime and the predicted probability of a price shock.

## 4. Dataset

I will use food-price data from the **World Food Programme Price Database**, published through the Humanitarian Data Exchange.

**Global dataset:**  
https://data.humdata.org/dataset/global-wfp-food-prices

**Somalia dataset:**  
https://data.humdata.org/dataset/wfp-food-prices-for-somalia

**Ethiopia dataset:**  
https://data.humdata.org/dataset/wfp-food-prices-for-ethiopia

I will begin with the Somalia and Ethiopia files and keep staple-food commodities with enough continuous monthly observations. The processed modeling dataset is expected to contain at least **5,000 monthly market–commodity records**, exceeding the minimum requirement of 1,000 rows. The exact count will be reported after cleaning.

The main original columns will include:

- `adm0_name` — country
- `adm1_name` — region
- `mkt_name` — market
- `cm_name` — commodity
- `pt_name` — retail or wholesale price type
- `um_name` — unit
- `cur_name` — currency
- `mp_month` and `mp_year` — observation date
- `mp_price` — recorded price

I will engineer features such as one-month and three-month price change, rolling averages, rolling volatility, distance from the recent average, previous spike count, month of the year, and market-regime cluster.

Preprocessing will include duplicate removal, missing-value checks, date creation, chronological sorting, and filtering short or incomplete series. Prices with different currencies, units, or price types will not be compared incorrectly. Older observations will be used for training and newer observations for validation and testing.

## 5. Algorithms I Plan to Train

### K-Means Clustering

K-Means will discover hidden market regimes from features such as average growth, volatility, spike frequency, trend, and distance from the recent average. I will test several values of `k`, inspect the cluster centers, and assign meaningful names only after training, such as Stable Market, Seasonal Volatile Market, or Shock-Sensitive Market.

K-Means is an additional first-stage algorithm. The following three supervised algorithms will be trained and compared on the same time periods.

### Logistic Regression

Logistic Regression will provide a simple and interpretable classification baseline.

### Decision Tree Classifier

A Decision Tree can learn non-linear rules from price changes, volatility, seasonality, and the market-regime feature.

### Random Forest Classifier

Random Forest combines many decision trees, reduces the overfitting of a single tree, and is suitable for structured market data.

The scaler and K-Means model will be fitted only on training data before transforming later observations. The discovered cluster will then be encoded as an additional feature for the classifiers.

## 6. Evaluation Plan

The clustering stage will be evaluated using:

- Silhouette Score
- Davies–Bouldin Index
- Cluster-size distribution
- Cluster-center interpretation

The three classifiers will be compared using:

- Accuracy
- Precision for the Price Shock class
- Recall for the Price Shock class
- F1-score for the Price Shock class
- ROC-AUC
- Confusion Matrix

The main model-selection metric will be the **F1-score for the Price Shock class**. Shock months may be less common than normal months, so accuracy alone may be misleading. F1-score balances finding real shocks with avoiding too many false alerts.

If two models have similar F1-scores, recall for the Price Shock class will be the tie-breaker because missing a real shock is more serious in an early-warning system.

I will also compare classifier performance with and without the K-Means cluster feature. This will test whether the hidden market regime improves prediction instead of assuming that it does.

## 7. Deployment Sketch

I will deploy the complete pipeline using **FastAPI**.

The `POST /predict` endpoint will accept the market, commodity, current month, and recent monthly prices:

```json
{
  "market": "Mogadishu",
  "commodity": "Sorghum",
  "current_month": 7,
  "monthly_prices": [9000, 9200, 9400, 9600, 9800, 10100, 10800, 11000, 11900, 13000, 14500, 15100]
}
```

The API will calculate rolling features, assign a market regime, and use the winning classifier to return:

```json
{
  "market_regime": "Shock-Sensitive Market",
  "prediction": "Price Shock",
  "shock_probability": 0.84,
  "alert_level": "HIGH"
}
```

The saved artifacts will include the scaler, K-Means model, regime-name mapping, preprocessing logic, and only the best supervised classifier.

## 8. Repository Plan

```text
suuqpulse-ai/
├── api/
│   ├── app.py
│   └── schemas.py
├── dataset/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
│   └── exploration.ipynb
├── src/
│   ├── preprocess.py
│   ├── build_features.py
│   ├── train_clusters.py
│   ├── train_classifiers.py
│   ├── evaluate.py
│   └── predict.py
├── tests/
│   └── test_api.py
├── project-proposal.md
├── project_paper.md
├── README.md
├── requirements.txt
└── .gitignore
```

The repository will separate data preparation, feature engineering, clustering, supervised training, evaluation, API code, model artifacts, and tests. The README will explain the dataset, chronological split, market regimes, comparison results, winning model, setup commands, and `/predict` usage.
