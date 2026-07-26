# 🎓 Student AI Tools vs Exam Score Prediction API

A Machine Learning project that predicts students' academic performance after using Artificial Intelligence (AI) learning tools. This project was developed as the final capstone project for the Data Science & Machine Learning Bootcamp.

---

# 📌 Project Overview

Artificial Intelligence tools such as ChatGPT, Gemini, Microsoft Copilot, and Perplexity AI are becoming common learning assistants for students worldwide. This project investigates how AI usage, study habits, and screen time influence students' academic performance.

The project builds several regression models to predict students' exam scores after using AI tools and deploys the best-performing model as a REST API using FastAPI.

---

# 🎯 Objectives

The main objectives of this project are:

- Predict students' grades after using AI tools.
- Compare multiple regression algorithms.
- Evaluate model performance using standard regression metrics.
- Deploy the best model using FastAPI.
- Demonstrate an end-to-end Machine Learning workflow.

---

# 🧠 Machine Learning Problem

**Problem Type**

Regression

**Target Variable**

```
grades_after_ai
```

The model predicts a student's expected exam score after using AI learning tools.

---

# 📂 Dataset

**Dataset Name**

Student AI Tools vs Exam Scores

**Source**

https://www.kaggle.com/datasets/muneebmuhammadali/student-ai-tools-vs-exam-scores/data

**Rows**

1000

**Features**

| Feature | Description |
|----------|-------------|
| Age | Student age |
| Education_Level | Current education level |
| Study_Hours_Per_Day | Average daily study hours |
| Uses_AI | Whether the student uses AI |
| AI_Tools_Used | AI tool used by the student |
| Purpose_of_AI | Main purpose of AI usage |
| Grades_Before_AI | Previous academic grade |
| Daily_Screen_Time_Hours | Daily screen time |

**Target**

```
Grades_After_AI
```

---

# 🧹 Data Preprocessing

The dataset was cleaned and prepared before model training.

The preprocessing pipeline includes:

- Loading the dataset
- Data inspection
- Handling missing values
- Removing duplicate records
- IQR outlier capping
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Train/Test Split

---

# 🤖 Machine Learning Models

Three regression algorithms were trained and compared.

## 1. Linear Regression

- Simple baseline model
- Easy to interpret
- Fast training

---

## 2. Random Forest Regressor

- Ensemble learning algorithm
- Handles non-linear relationships
- Reduces overfitting

---

## 3. Gradient Boosting Regressor

- Boosting algorithm
- Builds trees sequentially
- Often provides the highest prediction accuracy

---

# 📊 Evaluation Metrics

Each model is evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

Example comparison:

| Model | R² | MAE | RMSE |
|------|------|------|------|
| Linear Regression | 0.84 | 3.10 | 4.20 |
| Random Forest | 0.92 | 2.05 | 2.95 |
| Gradient Boosting | 0.94 | 1.80 | 2.60 |

The best-performing model is selected based on the highest R² score and lowest prediction errors.

---

# 📁 Project Structure

```
student-ai-performance-api/

│
├── dataset/
│   └── student_ai_tools_vs_exam_scores.csv
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_comparison.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── api/
│   └── app.py
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── README.md
├── project_paper.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/student-ai-performance-api.git
```

Move into the project folder

```bash
cd student-ai-performance-api
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Train the Models

Run

```bash
python src/train.py
```

This script will

- preprocess the dataset
- train all models
- compare performance
- save the best model

---

# 🌐 Run the API

Start FastAPI

```bash
uvicorn api.app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Swagger UI will automatically appear.

---

# 📩 API Example

## Request

```json
{
  "Age": 21,
  "Education_Level": "College",
  "Study_Hours_Per_Day": 5,
  "Uses_AI": "Yes",
  "AI_Tools_Used": "ChatGPT",
  "Purpose_of_AI": "Homework",
  "Grades_Before_AI": 75,
  "Daily_Screen_Time_Hours": 6
}
```

## Response

```json
{
  "Predicted_Grade": 87.4
}
```

---

# 📈 Results

The models were compared using the same testing dataset.

The best-performing model achieved the highest R² score and the lowest MAE and RMSE values, making it the preferred model for deployment.

---

# 🔮 Future Improvements

Future enhancements include:

- Increase dataset size
- Include attendance records
- Include socioeconomic variables
- Try XGBoost and LightGBM
- Deploy online using Render or Railway
- Build a Streamlit dashboard

---

# 📚 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- FastAPI
- Uvicorn
- Jupyter Notebook

---

# 📖 References

- Kaggle Dataset  
  https://www.kaggle.com/datasets/muneebmuhammadali/student-ai-tools-vs-exam-scores/data

- Scikit-learn Documentation  
  https://scikit-learn.org/stable/

- FastAPI Documentation  
  https://fastapi.tiangolo.com/

- Pandas Documentation  
  https://pandas.pydata.org/docs/

- NumPy Documentation  
  https://numpy.org/doc/

---

# 👨‍💻 Author

**Mohamed Abdirahman Hassan Yusuf**

Data Science & Machine Learning Bootcamp

2026

---

# ⭐ License

This project was developed for educational purposes as part of the Data Science & Machine Learning Bootcamp Final Capstone Project.
