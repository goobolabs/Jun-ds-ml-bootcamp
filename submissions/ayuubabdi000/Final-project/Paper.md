# Project Paper: Student Success AI — Course Completion Prediction API

### 🚀 [View Live Demo](https://student-success-ai-71cy-q3lco1qjj-ayub8.vercel.app/) | 🐙 [View Source Code or Repository](https://github.com/ayuubabdi000/student-success-ai)

## 1. Problem Statement and Motivation

Online learning platforms generate large amounts of student activity data, including login behavior, video engagement, assignment completion, quiz performance, and interaction patterns. However, many educational platforms still lack intelligent systems that can identify students who are at risk of dropping out before the problem becomes difficult to solve.

The problem addressed in this project is to build a machine learning system capable of predicting whether a student is likely to complete an online course based on their learning behavior and engagement data. The goal is to provide an AI-powered decision-support tool that helps educators identify struggling students early and provide targeted support.

In addition to completion prediction, this project also applies clustering techniques to discover different student learning behavior groups. These clusters help understand patterns among students, such as highly engaged learners, average learners, and students who may require additional intervention.

The final system provides a complete machine learning solution consisting of:

* A classification model for predicting course completion.
* A clustering model for identifying student learning profiles.
* A FastAPI backend for real-time predictions.
* A frontend interface for interacting with the AI system.

---

# 2. Dataset and Preprocessing

## Dataset Source and Size

The dataset used for this project is the **Course Completion Prediction Dataset** obtained from Kaggle.

The original dataset contained:

* **100,000 student records**
* **40 features**

The dataset includes information related to student engagement, learning activity, academic performance, and course interaction.

After preprocessing, the final dataset contained:

* **100,000 rows**
* **17 columns**
* **16 input features**
* **1 target variable**

The target variable is:

| Value | Meaning       |
| ----- | ------------- |
| 0     | Not Completed |
| 1     | Completed     |

## Features

The final model was trained using the following student behavior features:

* `Login_Frequency`
* `Average_Session_Duration_Min`
* `Video_Completion_Rate`
* `Discussion_Participation`
* `Time_Spent_Hours`
* `Days_Since_Last_Login`
* `Notifications_Checked`
* `Peer_Interaction_Score`
* `Assignments_Submitted`
* `Assignments_Missed`
* `Quiz_Attempts`
* `Quiz_Score_Avg`
* `Project_Grade`
* `Rewatch_Count`
* `App_Usage_Percentage`
* `Reminder_Emails_Clicked`

These features represent student engagement, academic activity, and learning consistency.

---

## Preprocessing Steps

The following preprocessing pipeline was applied before training the models:

### 1. Removing Unnecessary Features

Several columns were removed because they were identifiers, unrelated metadata, or features that did not contribute directly to predicting student completion.

Removed features included:

* Student information:

  * `Student_ID`
  * `Name`
  * `Gender`
  * `Age`
  * `Education_Level`
  * `Employment_Status`
  * `City`

* Course information:

  * `Course_ID`
  * `Category`
  * `Course_Level`
  * `CourseName`
  * `Course_Duration_Days`

* Payment information:

  * `Payment_Mode`
  * `Payment_Amount`
  * `Discount_Used`
  * `Fee_Paid`

* Other metadata:

  * `Enrollment_Date`
  * `Instructor_Rating`
  * `Satisfaction_Rating`
  * `Support_Tickets_Raised`
  * `Progress_Percentage`

---

### 2. Target Encoding

The target column was converted from text labels into numerical values:

```
Not Completed → 0
Completed → 1
```

This allowed machine learning algorithms to process the classification problem.

---

### 3. Feature Scaling

Numerical features were standardized using **StandardScaler**.

Scaling was applied because the dataset contains features with different value ranges. Standardization ensures that larger numerical values do not dominate the learning process.

---

### 4. Train-Test Split

The dataset was divided using an 80/20 split:

* Training data: **80,000 samples**
* Testing data: **20,000 samples**

The same split was used for all algorithms to ensure a fair comparison.

---

# 3. Algorithms

Three different machine learning algorithms were trained and evaluated.

## 1. Logistic Regression

### How it works

Logistic Regression is a supervised classification algorithm that predicts the probability of an observation belonging to a class. It uses the sigmoid function to convert input features into a probability between 0 and 1.

### Why it was chosen

Logistic Regression was selected as a baseline model because it is simple, fast, interpretable, and effective for binary classification problems. It also provides insight into how individual features influence student completion predictions.

### Performance

| Metric    | Score |
| --------- | ----: |
| Accuracy  | 0.602 |
| Precision | 0.597 |
| Recall    | 0.581 |
| F1-Score  | 0.589 |
| ROC-AUC   | 0.638 |

---

## 2. Random Forest Classifier

### How it works

Random Forest is an ensemble learning algorithm that creates multiple decision trees and combines their predictions. Each tree learns different patterns from random subsets of the data, and the final prediction is selected through majority voting.

### Why it was chosen

Random Forest was selected because it can capture complex relationships between student behaviors and course completion. It also provides feature importance information that helps explain model decisions.

### Performance

| Metric    | Score |
| --------- | ----: |
| Accuracy  | 0.587 |
| Precision | 0.583 |
| Recall    | 0.554 |
| F1-Score  | 0.568 |
| ROC-AUC   | 0.619 |

---

## 3. Gradient Boosting

### How it works

Gradient Boosting builds decision trees sequentially. Each new tree attempts to correct the errors made by previous trees, gradually improving prediction performance.

### Why it was chosen

Gradient Boosting was selected because it is a powerful ensemble technique capable of learning complex patterns in structured datasets.

### Performance

| Metric    | Score |
| --------- | ----: |
| Accuracy  | 0.598 |
| Precision | 0.591 |
| Recall    | 0.582 |
| F1-Score  | 0.587 |
| ROC-AUC   | 0.636 |

---

# 4. Results and Discussion

## Model Comparison

| Algorithm               |  Accuracy | Precision |    Recall |  F1-Score |   ROC-AUC |
| ----------------------- | --------: | --------: | --------: | --------: | --------: |
| **Logistic Regression** | **0.602** | **0.597** |     0.581 | **0.589** | **0.638** |
| Gradient Boosting       |     0.598 |     0.591 | **0.582** |     0.587 |     0.636 |
| Random Forest           |     0.587 |     0.583 |     0.554 |     0.568 |     0.619 |

---

## Model Selection

The selected production model was **Logistic Regression**.

The model was chosen because it achieved the highest overall performance:

* Highest Accuracy: **60.2%**
* Highest F1-score: **0.589**
* Highest ROC-AUC: **0.638**

The primary selection metric was the **F1-score** because it balances Precision and Recall. This is important because both false predictions are costly: incorrectly identifying successful students and failing to identify students who need support.

---

## Feature Importance

The most influential features were:

| Feature                | Importance |
| ---------------------- | ---------: |
| Video Completion Rate  |      0.122 |
| Quiz Score Average     |      0.096 |
| Project Grade          |      0.093 |
| Peer Interaction Score |      0.083 |
| App Usage Percentage   |      0.081 |

The results show that academic performance and engagement activities are strong indicators of student completion.

---

## Sanity Checks

Three sample predictions were tested using unseen student records.

### Sample 1

Input characteristics:

* Moderate video completion
* Average quiz score
* Active engagement

Prediction:

```
Completed
Confidence: 0.525
```

---

### Sample 2

Input characteristics:

* Low quiz score
* Lower project grade
* Reduced engagement

Prediction:

```
Not Completed
Confidence: 0.379
```

---

### Sample 3

Input characteristics:

* Limited study time
* Low interaction
* Moderate academic performance

Prediction:

```
Not Completed
Confidence: 0.453
```

These tests confirmed that the API correctly processes new student data and returns meaningful predictions.

---

# 5. Deployment Notes

The final Logistic Regression model was saved using Joblib along with the required preprocessing artifacts.

Saved artifacts include:

* Classification model
* Feature list
* Cluster model
* Cluster scaler
* Cluster profiles

## API Architecture

The backend was developed using **FastAPI**.

The API workflow:

1. User sends student information as JSON.
2. FastAPI validates the request.
3. Data is converted into a Pandas DataFrame.
4. The trained model generates a prediction.
5. The API returns the completion result and confidence score.

---

## Prediction Endpoint

```
POST /api/predict
```

Example request:

```json
{
  "Login_Frequency":4,
  "Average_Session_Duration_Min":35,
  "Video_Completion_Rate":57.3,"Discussion_Participation":3,
  "Time_Spent_Hours":3.6,
  "Days_Since_Last_Login":2,
  "Notifications_Checked":5,
  "Peer_Interaction_Score":6.3,
  "Assignments_Submitted":6,
  "Assignments_Missed":4,
  "Quiz_Attempts":4,
  "Quiz_Score_Avg":67.9,
  "Project_Grade":67.8,
  "Rewatch_Count":9,
  "App_Usage_Percentage":81,
  "Reminder_Emails_Clicked":4

}
```

Example response:

```json
{
  "prediction": 1,
  "label": "Completed",
  "confidence": 0.525
}
```

---

## Frontend Integration

A frontend application was created to allow users to interact with the AI system without directly calling the API.

The frontend uses:

* HTML
* CSS
* JavaScript
* Axios

Features include:

* Student completion prediction
* Confidence display
* Student behavior clustering
* Learning profile visualization

The frontend communicates with FastAPI through:

```
POST /api/predict
POST /api/cluster
```

---

# 6. Lessons Learned

## Challenges Faced

The main challenges during development were:

* Selecting useful features from a large dataset.
* Improving prediction performance when student success depends on many hidden factors.
* Comparing different algorithms and selecting the best model.
* Deploying the trained model as a reliable API.

The model achieved approximately 60% accuracy, showing that student completion prediction is a complex problem influenced by many factors beyond available behavioral data.

---

## Improvements for Future Work

Future improvements could include:

* Collecting additional student information such as previous academic history and motivation.
* Applying advanced models such as XGBoost and LightGBM.
* Performing hyperparameter tuning.
* Adding explainable AI methods such as SHAP.
* Creating personalized recommendations for struggling students.

---

## Key Takeaways

This project provided practical experience building a complete machine learning application from data preparation to deployment.

The main lessons learned were:

* Data preprocessing strongly affects model performance.
* Comparing multiple algorithms is necessary to choose the best solution.
* A simpler model can outperform complex models depending on the dataset.
* Deploying ML models requires careful management of preprocessing and model artifacts.
* Machine learning systems can provide valuable insights to support decision-making.

Overall, this project demonstrated the complete machine learning workflow: preparing data, training models, evaluating performance, deploying an API, and building an AI-powered educational support system.
