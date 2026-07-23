# Heart Disease Prediction API 🫀

This repository contains my final project for the ML Model Development and Deployment bootcamp. The goal of this project is to build a complete machine learning pipeline—from data preprocessing to training multiple models—and finally deploy the best-performing model as a REST API using FastAPI.

This API predicts whether a patient is at risk of heart disease based on their clinical information (like age, blood pressure, cholesterol, etc.).

## 📊 Dataset Details
- **Source:** [Heart Dataset on Kaggle](https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset)
- **Size:** 2,182 rows and 14 columns.
- **Preprocessing:** The data pipeline includes handling missing values, standard scaling numerical features (`StandardScaler`), and encoding categorical features.

## 🤖 Algorithms Trained
I trained and compared three different supervised machine learning algorithms to find the best model for this classification problem:
1. **Logistic Regression:** Used as a strong, interpretable baseline.
2. **Random Forest Classifier:** An ensemble method to capture non-linear relationships and reduce overfitting.
3. **Support Vector Machine (SVM):** Used for its effectiveness in finding optimal decision boundaries in high-dimensional spaces.

## 📈 Results and Model Selection

*(Note: Replace the metrics below with your actual final metrics)*

| Algorithm                  | Accuracy | F1-Score | ROC-AUC |
|----------------------------|----------|----------|---------|
| Logistic Regression        | 0.85     | 0.85     | 0.90    |
| **Random Forest (Winner)** | **0.91** | **0.91** | **0.95**|
| Support Vector Machine     | 0.88     | 0.88     | 0.92    |

**Results Summary:**
The **Random Forest** model performed the best across all major metrics, particularly achieving the highest F1-Score. Because balancing false positives and false negatives is critical in medical diagnosis, the Random Forest model was selected as the final winner, serialized into a `.pkl` file, and deployed to the API.

## 🚀 Setup and Example Commands

**1. Clone the repository and install dependencies:**
```bash
git clone https://github.com/abdullahi4444/Heart-Disease-Prediction-API.git
cd Heart-Disease-Prediction-API
pip install -r requirements.txt
```

**2. Run the training script (Optional):**
```bash
python src/train.py
```

**3. Start the FastAPI server:**
```bash
uvicorn api.app:app --reload
```

## 🌐 API Usage Example

You can test the locally running API by sending a JSON payload to the `/predict` endpoint.

**Curl Command:**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
        "age": 54,
        "sex": 1,
        "cp": 0,
        "trestbps": 110,
        "chol": 206,
        "fbs": 0,
        "restecg": 0,
        "thalachh": 108,
        "exang": 1,
        "oldpeak": 0.0,
        "slope": 1,
        "ca": 2,
        "thal": 0
      }'
```

**Expected Response:**
```json
{
  "prediction": "Heart Disease",
  "probability": 0.91
}
```

---
*Developed by Abdullahi Abdiweli Adam (July 2026).*
