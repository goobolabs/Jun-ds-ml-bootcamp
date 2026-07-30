# Online Shopper Purchase Intention Predictor
A Machine Learning web application that predicts whether an online shopper is likely to complete a purchase based on their browsing behavior.
The project combines **Machine Learning**, **FastAPI**, and **TypeScript** to provide real-time purchase predictions through a modern web interface.
---
## Features
- Predicts customer purchase intention- Multiple Machine Learning models- Real-time prediction API- Clean and responsive frontend- FastAPI backend- TypeScript frontend- Model confidence score- Easy-to-use interface
---
## Machine Learning Models
This project compares multiple classification algorithms and cluster:
- Logistic Regression- Random Forest- Gradient Boosting- XGBoost - k-means - GMM
Models were evaluated using:
- Accuracy- Precision- Recall- F1 Score- Confusion Matrix
The best-performing model is automatically used for prediction.
---
## Tech Stack
### Backend- FastAPI- Python- Scikit-learn- Pandas- Joblib
### Frontend- TypeScript- HTML- CSS
### Machine Learning- Scikit-learn- XGBoost- SMOTE (Class Imbalance Handling)
---
## Project Structure
```online_shopper_predictor/│├── api/│   └── app.py│├── frontend/│   ├── index.html│   ├── app.ts│   └── styles.css│├── model/│   ├── random_forest.joblib│   ├── logistic.joblib│   ├── gradient_boosting.joblib│   ├── xgboost.joblib│   └── scaler.joblib│├── train_process/│   ├── processing.ipynb│   └── train.ipynb│├── data/│   └── online_shopper_cleaned.csv│├── requirements.txt└── README.md```
---
## Dataset
Dataset: **Online Shoppers Purchasing Intention Dataset**
Features include:
- Administrative- Administrative Duration- Informational- Informational Duration- Product Related- Product Related Duration- Bounce Rate- Exit Rate- Page Values- Special Day- Month- Visitor Type- Weekend
Target:
- Revenue (Purchase: Yes / No)
- Revenue
0    3885
1     150
Name: count, dtype: int64
Revenue
0    972
1     37
Name: count, dtype: int64
---
## Installation
Clone the repository
```bash git clone (https://github.com/Asmaa-Abdi/online-shopper-intention.git)```
Move into the project
```bash cd online-shopper-predictor```
Create virtual environment
```bash python -m venv venv```
Activate environment
Windows
```bash venv\Scripts\activate```
Install dependencies
```bash pip install -r requirements.txt```
---
## Run FastAPI
```bash uvicorn api.app:app --reload```
Open:
```http://127.0.0.1:8000/docs```
---
## Run Frontend
Open
```frontend/index.html```
or run using VS Code Live Server.
---
## API Endpoint
### POST
```/predict```
Returns
```json{  "model_used": "random_forest",  "prediction": 1,  "will_buy": true,  "confidence_score": 0.92}```
---
## Project Workflow
1. Load Dataset2. Clean Data3. Feature Engineering4. Handle Class Imbalance using SMOTE5. Train Multiple Models6. Evaluate Performance7. Save Best Model8. Deploy Prediction API9. Connect Frontend with FastAPI

---
## Future Improvements
- Deploy on Render- Typescript Frontend- PostgreSQL Integration- User Authentication- Prediction History Dashboard- Docker Deployment
---
## Author
**Asmaa**
Machine Learning & Backend Developer
(https://github.com/Asmaa-Abdi/online-shopper-intention.git)
---

