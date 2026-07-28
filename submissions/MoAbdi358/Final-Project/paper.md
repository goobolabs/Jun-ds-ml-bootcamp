# Customer Repeat Purchase Prediction API

> A Simple Explanation of My Machine Learning Project

**Author:** Mohamed Abdi Ahmed  
**Date:** July 2026  
**GitHub:** https://github.com/MoAbdi358/Customer-Repeat-Purchase-Prediction-API

---

# 1. What Is This Project About?

When someone buys something online for the first time, most of them never come back to buy again. This is a big problem for online shops because acquiring a new customer is much more expensive than retaining an existing one.

This project builds a **Machine Learning system** that analyzes a customer's first purchases and predicts whether they will become a **repeat buyer**.

The project also includes:

- **FastAPI backend** for serving prediction models
- **Next.js frontend dashboard** that allows non-technical users to enter customer information and instantly receive predictions

---

# 2. Project Objectives

The project aims to:

- Study the Online Retail II dataset
- Clean and preprocess the data
- Use only each customer's **first 90 days** of activity
- Train multiple machine learning models
- Compare models using evaluation metrics
- Select the best model using **F1-score**
- Deploy the best model as a REST API
- Build a user-friendly web dashboard

---

# 3. Dataset

**Dataset:** Online Retail II

**Source:**

- UCI Machine Learning Repository
- Kaggle

https://archive.ics.uci.edu/dataset/502/online+retail+ii

## Dataset Facts

- **Original Rows:** 1,067,371
- **Original Features:** 8

### Target Variable

A new column was created:

```text
repeat_purchase

1 → Customer purchased again
0 → Customer never purchased again
```

### Original Features

- Invoice Number
- Stock Code
- Description
- Quantity
- Invoice Date
- Price
- Customer ID
- Country

### Features Used for Prediction

The model uses **10 engineered features**:

- total_spend
- avg_order_value
- total_items
- total_transactions
- unique_products
- days_between_first_and_last_purchase
- purchase_frequency
- avg_items_per_order
- country
- has_returned_items

---

# 4. Exploratory Data Analysis (EDA)

Key findings:

- Original dataset contained **1,067,371 rows**
- **243,007 rows** had missing Customer IDs and were removed
- Cancelled invoices and returned items were preserved as useful behavioral indicators
- Final dataset contained **5,346 customers**

Customer distribution:

| Customer Type | Count |
|---------------|------:|
| Repeat Buyers | 3,649 |
| One-Time Buyers | 1,697 |

The dataset is therefore **slightly imbalanced**.

The analysis also showed that customers who purchased more frequently during their first 90 days were much more likely to return.

---

# 5. Data Preprocessing

The preprocessing pipeline included:

1. Remove missing Customer IDs
2. Detect cancelled invoices
3. Detect returned items
4. Identify each customer's first purchase date
5. Keep only the first 90 days of activity
6. Engineer customer-level features
7. Remove incomplete observation windows
8. Encode country using LabelEncoder
9. Scale numerical variables using StandardScaler
10. Split the data

## Train/Test Split

| Dataset | Customers |
|----------|----------:|
| Training | 4,276 |
| Testing | 1,070 |

---

# 6. Machine Learning Models

## Problem Type

Binary Classification

Question:

> Will the customer purchase again after their first 90 days?

---

## Models Compared

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

---

## Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

The primary metric used for model selection was **F1-Score**.

---

## Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|---------:|----------:|-------:|---------:|--------:|
| Logistic Regression | 0.6897 | 0.6888 | 0.9945 | **0.8139** | 0.7211 |
| Decision Tree | 0.6860 | 0.6858 | 0.9959 | 0.8123 | 0.7157 |
| Random Forest | 0.7075 | 0.7259 | 0.9178 | 0.8106 | 0.7331 |
| Gradient Boosting | 0.6991 | 0.7166 | 0.9247 | 0.8074 | 0.7263 |

---

## Best Model

**Logistic Regression**

Reasons:

- Highest F1-Score (0.8139)
- Very high Recall (0.9945)
- Successfully identified nearly every repeat customer

---

## Confusion Matrix

The Logistic Regression model correctly predicted:

- ✅ 726 Repeat Buyers
- ✅ 12 One-Time Buyers

Incorrect predictions:

- ❌ 328 False Positives
- ❌ 4 False Negatives

The trained model was saved as:

```text
models/best_model.pkl
```

---

# 7. Backend API

The backend was developed using **FastAPI**.

Features include:

- Pydantic input validation
- Automatic loading of trained models
- Feature scaling
- Country encoding
- CORS support
- Interactive Swagger documentation
- Health check endpoint

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/predict` | Customer prediction |

---

## Example Request

```json
{
  "total_spend": 350.50,
  "avg_order_value": 87.62,
  "total_items": 45,
  "total_transactions": 4,
  "unique_products": 12,
  "days_between_first_and_last_purchase": 30,
  "purchase_frequency": 0.13,
  "avg_items_per_order": 11.25,
  "country": "United Kingdom",
  "has_returned_items": 0
}
```

---

## Example Response

```json
{
  "prediction": "Repeat Buyer",
  "probability": 0.746,
  "model_predictions": {
    "Logistic Regression": {
      "prediction": "Repeat Buyer",
      "probability": 0.746
    },
    "Decision Tree": {
      "prediction": "Repeat Buyer",
      "probability": 0.682
    },
    "Random Forest": {
      "prediction": "Repeat Buyer",
      "probability": 0.6715
    },
    "Gradient Boosting": {
      "prediction": "Repeat Buyer",
      "probability": 0.6658
    }
  }
}
```

---

# 8. Frontend Dashboard

Built using:

- React
- Next.js
- TypeScript
- Tailwind CSS

Main features:

- KPI Summary
- Preset Customer Profiles
- Automatic Feature Calculation
- Model Comparison Panel
- API Health Monitoring
- Responsive Design

---

# 9. System Workflow

```text
User Inputs Customer Data
           │
           ▼
Frontend Calculates Derived Features
           │
           ▼
Generate Retention Forecast
           │
           ▼
FastAPI Receives Request
           │
           ▼
Validate Input
           │
           ▼
Encode Country
           │
           ▼
Scale Numerical Features
           │
           ▼
Run All Four Models
           │
           ▼
Return Predictions
           │
           ▼
Display Results on Dashboard
```

---

# 10. Technologies Used

## Machine Learning

- Python
- pandas
- NumPy
- Scikit-learn
- Joblib

## Backend

- FastAPI
- Pydantic
- Uvicorn

## Frontend

- React
- Next.js
- TypeScript
- Tailwind CSS
- Lucide React

## Development Tools

- VS Code
- Git
- TypeScript Compiler

---

# 11. Project Structure

```text
customer-repeat-purchase/
│
├── dataset/
│   ├── online_retail_II.csv
│   └── clean_customer_dataset.csv
│
├── models/
│   ├── best_model.pkl
│   ├── best_model.joblib
│   ├── scaler.pkl
│   ├── scale_cols.joblib
│   ├── train_columns.json
│   ├── country_encoder.joblib
│   └── *_model.joblib
│
├── client/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   ├── package.json
│   └── tsconfig.json
│
├── processing.py
├── model.py
├── utils.py
├── app.py
├── test_prediction.py
├── requirements.txt
├── README.md
```

---

# 12. Testing

The project was tested by:

- Training and validating all models
- Testing the preprocessing pipeline
- Using FastAPI Swagger documentation
- Sending HTTP requests to API endpoints
- Running TypeScript compiler checks
- Verifying successful prediction responses

---

# 13. Limitations

Current limitations include:

- Slight class imbalance
- Fixed 90-day observation window
- Logistic Regression captures only linear relationships
- Unseen countries require default encoding

---

# 14. Future Improvements

Potential enhancements include:

- Website clickstream features
- Shopping cart behavior
- Dynamic observation windows
- Profit-based decision thresholds
- Cloud deployment
- Real-time prediction services

---

# 15. Lessons Learned

Through this project I learned:

- Preventing data leakage
- Building reusable Scikit-learn pipelines
- Deploying machine learning APIs
- Connecting FastAPI with a React frontend
- Handling CORS
- Comparing multiple ML models
- Structuring a complete machine learning project

---

# 16. Conclusion

This project demonstrates a complete end-to-end machine learning application for predicting customer repeat purchases.

Four classification models were developed and evaluated, with **Logistic Regression** selected as the final model due to its superior **F1-Score (0.8139)** and excellent **Recall (0.9945)**.

The final system combines a FastAPI backend with a modern Next.js dashboard, allowing marketing teams to generate customer retention predictions without requiring programming knowledge. This solution can help businesses identify high-value customers, improve retention strategies, and optimize marketing campaigns.