# Customer Purchase Amount Prediction Using Machine Learning

## Project Overview

This project predicts the **Purchase Amount (USD)** that a customer is likely to spend based on demographic information, shopping preferences, and purchase history.

The project demonstrates an end-to-end machine learning workflow, including data preprocessing, model training, evaluation, model comparison, and deployment using **FastAPI**.

---

## Dataset

**Name:** Customer Shopping Trends Dataset

**Source:**
https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset/data

### Features

* Age
* Gender
* Category
* Item Purchased
* Size
* Color
* Season
* Review Rating
* Subscription Status
* Previous Purchases
* Payment Method
* Shipping Type
* Discount Applied
* Promo Code Used
* Frequency of Purchases

### Target

**Purchase Amount (USD)**

---

## Machine Learning Algorithms

The following regression models are trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The best-performing model is selected using **R² Score**, **MAE**, and **RMSE**.

---

## Data Preprocessing

The preprocessing pipeline includes:

* Exploratory Data Analysis (EDA)
* Removing duplicate records
* Handling missing values
* Encoding categorical variables
* Scaling numerical features
* Handling outliers
* Feature selection
* Train/Test split

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib
* Jupyter Notebook

---

## Project Structure

```text
customer-purchase-prediction/
│
├── dataset/
├── notebooks/
├── src/
├── api/
├── models/
├── README.md
├── project_paper.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/customer-purchase-prediction.git
```

Move into the project folder:

```bash
cd customer-purchase-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Train the Models

```bash
python src/train.py
```

---

## Run the API

```bash
uvicorn api.app:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Example API Request

### POST `/predict`

```json
{
  "Age": 29,
  "Gender": "Male",
  "Category": "Clothing",
  "Season": "Winter",
  "Review Rating": 4.5,
  "Previous Purchases": 12,
  "Subscription Status": "Yes"
}
```

### Example Response

```json
{
  "predicted_purchase_amount": 135.60
}
```

---

## Results Summary

Three regression algorithms are trained and evaluated using the same dataset and train/test split. The model with the highest R² Score and the lowest MAE and RMSE is selected as the final model and deployed through FastAPI.

---

## Author

**Abdullahi Hassan Shire**

Goobo Labs Data Science & Machine Learning Bootcamp

July 2026
