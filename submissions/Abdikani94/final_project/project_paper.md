# Bank Customer Intelligence System

## Machine Learning Project Paper

**Author:** Abdi Kani Mohamed Hassan  
**Date:** July 2026  
**GitHub Repository:** https://github.com/Abdikani94/Bank-Customer-Intelligence-System

---

# 1. Introduction

Banks conduct marketing campaigns to promote financial products such as term-deposit accounts. Contacting every customer is expensive and inefficient because most customers do not subscribe. Banks also need a better way to understand different customer groups and their financial characteristics.

This project developed an end-to-end machine learning system that performs two tasks:

1. **Classification:** Predict whether a customer will subscribe to a term deposit.
2. **Clustering:** Group customers into similar segments using demographic and financial information.

The trained models were deployed using FastAPI, and a React dashboard was developed to allow users to enter customer information and view prediction and segmentation results.

---

# 2. Project Objectives

The main objectives were:

- Analyze the Bank Marketing Dataset.
- Prepare customer data for machine learning.
- Train and compare multiple classification algorithms.
- Select the best classification model using F1-score.
- Compare K-Means, Agglomerative Clustering, and DBSCAN.
- Create meaningful customer segments.
- Deploy the selected models using FastAPI.
- Build a responsive React dashboard for user interaction.

---

# 3. Dataset Description

The project uses the **Bank Marketing Dataset** obtained from Kaggle.

**Dataset source:**  
https://www.kaggle.com/datasets/mdnaimislam165436/bank-marketing-dataset-uci

The dataset contains:

- **45,211 rows**
- **17 columns**
- **Target column:** `y`

The target values are:

- `yes` — the customer subscribed to a term deposit.
- `no` — the customer did not subscribe.

The dataset contains customer demographic, financial, and campaign information, including:

- Age
- Job
- Marital status
- Education
- Account balance
- Housing loan
- Personal loan
- Contact information
- Campaign contacts
- Previous campaign information

The deployed API uses these eight input features:

```text
age, job, marital, education, balance, housing, loan, campaign
```

---

# 4. Exploratory Data Analysis

Exploratory Data Analysis was completed in `notebooks/eda.ipynb`.

The main findings were:

- The dataset contains 45,211 rows and 17 columns.
- Seven columns are numerical and ten are categorical.
- No standard missing values were found.
- No duplicate rows were found.
- Unknown categorical values occur in `job`, `education`, `contact`, and `poutcome`.
- The target is imbalanced, with approximately 88.3% non-subscribers and 11.7% subscribers.
- Customers without housing or personal loans showed higher subscription rates.
- Tertiary-educated customers had a higher subscription rate.
- Account balance contained valid extreme values that required robust preprocessing rather than automatic removal.

The `duration` feature was excluded because it is known only after the marketing call and would cause data leakage.

---

# 5. Data Preprocessing

The following preprocessing steps were applied:

1. The dataset was checked for missing values and duplicates.
2. The `duration` feature was removed to prevent data leakage.
3. Only the eight deployment features were selected.
4. Numerical features were processed using `RobustScaler`.
5. Categorical features were transformed using `OneHotEncoder` with unknown-category handling.
6. Feature selection was applied using `SelectPercentile`.
7. The target variable was converted into binary values.
8. The classification data was divided into training and testing sets.
9. Preprocessing and models were combined in Scikit-learn pipelines.

Using pipelines ensures that the same transformations are applied during both training and API prediction.

---

# 6. Supervised Learning

## 6.1 Classification Task

The classification task predicts whether a customer will subscribe to a term deposit.

The output is:

```text
Yes
No
```

Three classification algorithms were trained and evaluated:

- Logistic Regression
- Random Forest
- XGBoost

Because the dataset is imbalanced, the models were compared using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

F1-score was used as the primary model-selection metric because it balances precision and recall.

## 6.2 Classification Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Random Forest | **0.7997** | **0.2733** | 0.4291 | **0.3339** |
| XGBoost | 0.7143 | 0.2265 | 0.5974 | 0.3285 |
| Logistic Regression | 0.6376 | 0.1917 | **0.6522** | 0.2963 |

## 6.3 Best Classification Model

**Random Forest** was selected as the final classification model because it achieved the highest F1-score of **0.3339**. It also achieved the highest accuracy and precision among the tested models.

Logistic Regression produced the highest recall, but it also generated many false-positive predictions. XGBoost achieved stronger recall than Random Forest, but its F1-score was slightly lower.

## 6.4 Random Forest Confusion Matrix Summary

The selected Random Forest model produced the following results:

- Correctly predicted 6,778 non-subscribers.
- Correctly predicted 454 subscribers.
- Incorrectly predicted 1,207 non-subscribers as subscribers.
- Missed 604 actual subscribers.

The selected model was saved as:

```text
backend/models/classification_model.pkl
```

---

# 7. Unsupervised Learning

## 7.1 Clustering Task

The clustering task groups customers using the same eight deployment features. The target column `y` was not used to create the clusters.

Three clustering algorithms were evaluated:

- K-Means
- Agglomerative Clustering
- DBSCAN

The main evaluation metrics were:

- Silhouette Score
- Davies-Bouldin Index
- Cluster size and business usability
- Ability to assign new customers through the deployed system

## 7.2 K-Means Evaluation

Different values of `K` were tested. Although the Elbow Method suggested approximately four clusters, `K = 2` achieved the strongest K-Means evaluation results:

| Metric | Result |
|---|---:|
| Silhouette Score | **0.5968** |
| Davies-Bouldin Index | **0.8302** |
| Number of clusters | **2** |

## 7.3 Comparison with Other Algorithms

Agglomerative Clustering achieved a Silhouette Score of **0.7265** and a Davies-Bouldin Index of **0.5661**, but it produced a highly imbalanced second cluster containing only 58 customers in the evaluation sample.

DBSCAN achieved a Silhouette Score of **0.6328** and a Davies-Bouldin Index of **0.3789**, but its second cluster contained only eight customers and 3.36% of customers were classified as noise.

Although Agglomerative Clustering and DBSCAN produced strong internal scores, their smallest clusters were too limited for broad business use. They also do not provide a simple standard `predict()` method for assigning new customers.

**K-Means with two clusters** was selected because it produced the most usable and deployable customer segmentation.

## 7.4 Customer Segments

### Cluster 0 Typical-Balance Customers

- Customer count: **43,316**
- Percentage: **95.81%**
- Average balance: approximately **899.98**
- Common job: blue-collar
- Common education: secondary
- Most customers have housing loans.
- Most customers do not have personal loans.
- Subscription rate: **11.53%**

API description:

```text
Typical-balance customers, often blue-collar or secondary-educated, with many holding housing loans.
```

### Cluster 1  High-Balance Professional Customers

- Customer count: **1,895**
- Percentage: **4.19%**
- Average balance: approximately **11,929.27**
- Common job: management
- Common education: tertiary
- Most customers do not have housing loans.
- Most customers do not have personal loans.
- Subscription rate: **15.51%**

API description:

```text
High-balance professional customers, often management or tertiary-educated, usually without housing or personal loans.
```

The selected clustering model was saved as:

```text
backend/models/clustering_model.pkl
```

---

# 8. Backend Development

The backend was developed using FastAPI.

The application includes:

- Request validation using Pydantic
- Model loading using Joblib
- CORS configuration for the React frontend
- Swagger API documentation
- Health-status endpoint
- Prediction and clustering endpoints

## 8.1 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Returns basic API information |
| `GET` | `/health` | Confirms that the API is running |
| `POST` | `/predict` | Predicts term-deposit subscription |
| `POST` | `/cluster` | Assigns a customer segment |

## 8.2 Prediction Request

```json
{
  "age": 35,
  "job": "technician",
  "marital": "married",
  "education": "secondary",
  "balance": 2500,
  "housing": "no",
  "loan": "no",
  "campaign": 2
}
```

Example response:

```json
{
  "prediction": "Yes",
  "probability": 0.7781
}
```

## 8.3 Clustering Request

```json
{
  "age": 35,
  "job": "technician",
  "marital": "married",
  "education": "secondary",
  "balance": 2500,
  "housing": "no",
  "loan": "no",
  "campaign": 2
}
```

Example response:

```json
{
  "cluster": 0,
  "description": "Typical-balance customers, often blue-collar or secondary-educated, with many holding housing loans."
}
```

---

# 9. Frontend Development

The frontend was developed using React and Vite.

The frontend communicates with FastAPI through Axios and contains the following pages:

- **Dashboard:** Displays dataset and model summaries.
- **Prediction:** Accepts customer information and displays `Yes` or `No` with probability.
- **Segmentation:** Displays `Cluster 0` or `Cluster 1` with a description.
- **Analytics:** Displays classification and clustering information.
- **About:** Explains the project, dataset, and technologies.

The frontend also checks the `/health` endpoint and displays whether the API is connected.

The interface was designed as a responsive banking and analytics dashboard using custom CSS.

---

# 10. System Workflow

The complete prediction workflow is:

```text
User enters customer information
            ↓
React sends JSON to FastAPI
            ↓
Pydantic validates the request
            ↓
The saved pipeline preprocesses the data
            ↓
Random Forest predicts Yes or No
            ↓
FastAPI returns prediction and probability
            ↓
React displays the result
```

The clustering workflow is:

```text
User enters customer information
            ↓
React sends JSON to FastAPI
            ↓
Pydantic validates the request
            ↓
The saved clustering pipeline preprocesses the data
            ↓
K-Means assigns Cluster 0 or Cluster 1
            ↓
FastAPI returns the cluster and description
            ↓
React displays the customer segment
```

---

# 11. Technologies Used

## Machine Learning and Data Analysis

- Python
- pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Jupyter Notebook
- Joblib

## Backend

- FastAPI
- Pydantic
- Uvicorn
- Pydantic Settings

## Frontend

- React
- Vite
- Axios
- React Router
- CSS

## Testing and Development

- Pytest
- Ruff
- VS Code
- Git
- GitHub

---

# 12. Project Structure

```text
Bank-Customer-Intelligence-System/
├── backend/
│   ├── api/
│   │   ├── app.py
│   │   ├── predict.py
│   │   ├── cluster.py
│   │   └── config.py
│   ├── models/
│   │   ├── classification_model.pkl
│   │   └── clustering_model.pkl
│   └── src/
├── dataset/
│   └── bank-full.csv
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   └── package.json
├── notebooks/
│   ├── eda.ipynb
│   ├── classification.ipynb
│   └── clustering.ipynb
├── tests/
├── requirements.txt
├── README.md
└── project_paper.md
```

---

# 13. Testing

The system was tested through:

- Notebook evaluation outputs
- FastAPI Swagger documentation
- API request and response testing
- Backend health checks
- Pytest health-endpoint test
- React-to-FastAPI integration testing

The `/predict` and `/cluster` endpoints both returned successful HTTP `200` responses during testing.

---

# 14. Limitations

The project has several limitations:

- The classification dataset is highly imbalanced.
- The selected Random Forest model has a moderate F1-score and misses some actual subscribers.
- The system uses only eight features to maintain a simple deployment interface.
- Cluster 1 is much smaller than Cluster 0.
- The models were trained using one historical dataset and may require retraining for a different bank or market.
- The current deployment is local and is not yet hosted on a public cloud platform.

---

# 15. Future Improvements

Possible improvements include:

- Apply additional class-imbalance techniques.
- Perform more extensive hyperparameter tuning.
- Evaluate probability-threshold optimization.
- Add more model-performance visualizations to the frontend.
- Add batch prediction for multiple customers.
- Deploy the backend and frontend online.
- Monitor model performance using new customer data.

---

# 16. Lessons Learned

This project provided practical experience in:

- Performing exploratory data analysis.
- Preventing data leakage.
- Building reusable preprocessing pipelines.
- Comparing supervised and unsupervised algorithms.
- Selecting models using both metrics and practical usability.
- Saving and loading trained models.
- Developing and testing REST APIs.
- Connecting a React frontend to a machine learning backend.
- Organizing and documenting an end-to-end machine learning project.

---

# 17. Conclusion

The Bank Customer Intelligence System successfully combines supervised and unsupervised machine learning in a complete web application.

Random Forest was selected for term-deposit subscription prediction because it achieved the highest F1-score among the tested classification models. K-Means with two clusters was selected for customer segmentation because it produced meaningful, actionable, and deployable customer groups.

The FastAPI backend successfully serves both models through validated REST endpoints, while the React frontend allows users to submit customer information and view prediction and segmentation results.

The project demonstrates how machine learning can support customer analysis, targeted marketing, and data-driven decision-making in the banking sector.