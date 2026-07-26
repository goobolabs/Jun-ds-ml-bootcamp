# Project Paper — SuuqPulse AI

## Hidden Market Regime Discovery and Staple Food Price Shock Prediction using Machine Learning

**Bootcamp:** Goobo Labs DS/ML Bootcamp 2026  
**Repository:** https://github.com/saynis/SuuqPulse_AI  
**API:** https://suuqpulseai-production.up.railway.app  
**Frontend Dashboard:** https://suuq-pulse-ai.vercel.app  
**Date:** July 2026

# 1. Problem Statement and Motivation

Food price instability is a major challenge affecting communities and humanitarian planning. Sudden increases in staple food prices can reduce household purchasing power and may indicate early signs of a food security problem.

SuuqPulse AI is an early-warning machine learning system built for Somali food markets. Instead of only forecasting prices, the system first discovers hidden market behavior patterns and then predicts possible future price shocks.

The goal is to provide a data-driven decision support tool that helps analysts identify markets requiring attention.

# 2. Dataset and Preprocessing

The project uses the World Food Programme (WFP) Somalia Food Prices Dataset.

Raw dataset:
- 42,616 rows
- 16 columns

After preprocessing:
- 42,304 rows
- 14 columns

Coverage:
- 1995–2026
- 46 markets
- 18 regions
- 22 commodities

The model focuses on eight staple foods:
- Maize
- Imported rice
- Red sorghum
- White sorghum
- Wheat flour
- Sugar
- Vegetable oil
- Cowpeas

Preprocessing steps:
- Removed duplicates
- Removed missing location records
- Kept retail prices
- Added year and month features

# 3. Feature Engineering

The project converts raw prices into market behavior features:

- Average price change
- Price volatility
- Spike count
- Relative trend
- Seasonality

Relative trend:

Relative Trend = Price Slope / Average Price

This makes trends comparable between commodities with different price scales.

After feature engineering, the data became 341 market-commodity profiles.

# 4. Machine Learning Approach

SuuqPulse AI uses two stages.

## Phase 1: Unsupervised Learning

Algorithm:

K-Means Clustering

Purpose:

Discover hidden market regimes.

Features:
- Price change
- Volatility
- Spike count
- Relative trend
- Seasonality

Results:

| Regime | Profiles |
|---|---:|
| Growing | 233 |
| Stable | 98 |
| High Risk | 10 |

## Phase 2: Supervised Learning

The system predicts whether a price shock happens next month.

Models compared:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting

Results:

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Logistic Regression |64.4%|15.4%|51.9%|23.7%|
| Random Forest |86.8%|26.6%|13.7%|18.1%|
| Gradient Boosting |89.5%|61.3%|3.8%|7.1%|

Logistic Regression was selected because it achieved the best F1 score and recall.

# 5. Deployment

Architecture:

WFP Dataset → Preprocessing → Feature Engineering → K-Means → Classifier → FastAPI → Next.js Dashboard

The API loads saved models:
- scaler.pkl
- kmeans.pkl
- classifier.pkl
- metadata.joblib

The prediction endpoint returns:
- Market regime
- Shock probability
- Prediction result
- Recommendation

Deployment:

Backend:
https://suuqpulseai-production.up.railway.app

Frontend:
https://suuq-pulse-ai.vercel.app

# 6. Results and Discussion

The project successfully built a complete machine learning pipeline from raw data to a deployed application.

The clustering stage discovered meaningful market behavior patterns, while the classifier provides an early-warning signal for possible food price shocks.

Because shocks are rare events, F1 score and recall were more important than accuracy.

# 7. Limitations and Future Work

Future improvements include:

- Adding rainfall and climate data
- Adding conflict information
- Adding exchange rate information
- Using chronological validation
- Improving shock definitions

# 8. Lessons Learned

This project improved my understanding of the complete machine learning lifecycle:

- Data preprocessing
- Feature engineering
- Model comparison
- Model evaluation
- Model deployment
- Building production ML systems

SuuqPulse AI demonstrates how machine learning can transform historical food price data into a practical early-warning decision support system.