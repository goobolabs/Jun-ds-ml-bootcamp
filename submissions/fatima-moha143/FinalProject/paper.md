# Flight Delay Prediction Using Machine Learning
# GitHub Repository:
https://github.com/fatima-moha143/fligh_delay_predict.git

<<<<<<< HEAD
## Student Information

**Student Name:** Fadumo mohamed omar 

**Project Title:** Flight Delay Prediction Using Machine Learning

**Project Type:** Classification Problem

**Programming Language:** Python

**Framework:** FastAPI

**Libraries:** Scikit-learn, Pandas, NumPy, Joblib, Jinja2



## Abstract

Flight delays are one of the biggest challenges in the aviation industry. They affect airline operations, increase operational costs, and reduce passenger satisfaction. This project presents a machine learning solution that predicts whether a flight will be **On-Time** or **Delayed** using historical flight information.

Three classification algorithms were trained and evaluated: Logistic Regression, Random Forest, and Gradient Boosting. After comparing their performance, the best model was deployed using FastAPI with a simple HTML and CSS web interface. The application allows users to enter flight information and instantly receive a prediction along with the model's confidence score.

---

# 1. Introduction

Machine learning has become an important technology for solving real-world problems across many industries. In aviation, predicting flight delays helps airlines improve scheduling, reduce operational costs, and provide better services to passengers.

The goal of this project is to develop an intelligent prediction system capable of classifying flights as either **On-Time** or **Delayed** based on historical flight information.

---

# 2. Problem Statement

Flight delays negatively impact airlines and passengers by increasing costs, disrupting schedules, and causing customer dissatisfaction. Manual prediction is difficult because many operational factors influence delays.

This project addresses this problem by developing a supervised machine learning model that predicts flight status before departure.

---

# 3. Objectives

The objectives of this project are:

- Analyze historical flight data.
- Clean and preprocess the dataset.
- Train multiple machine learning classification models.
- Compare model performance.
- Select the best-performing model.
- Deploy the final model using FastAPI.
- Develop an interactive web application for predictions.

---

# 4. Dataset Description

The project uses a Flight Delay dataset containing historical flight records.

## Dataset Summary

| Item | Value |
|------|------:|
| Rows | 539,382 |
| Features | 7 |
| Target | Class |

### Input Features

| Feature | Description |
|---------|-------------|
| Flight | Flight Number |
| Time | Departure Time |
| Length | Flight Duration |
| Airline | Airline Code |
| AirportFrom | Departure Airport |
| AirportTo | Arrival Airport |
| DayOfWeek | Day of Week |
=======
**Machine Learning Final Project**

# GitHub Repository:
https://github.com/fatima-moha143/fligh_delay_predict.git

---

## Student Information

**Student Name:** Fadumo mohamed omar 

**Project Title:** Flight Delay Prediction Using Machine Learning

**Project Type:** Classification Problem

**Programming Language:** Python
>>>>>>> 83876d23551c1ef5c90541491dac5802fca59096

**Framework:** FastAPI

<<<<<<< HEAD
=======
**Libraries:** Scikit-learn, Pandas, NumPy, Joblib, Jinja2

---

# Abstract

Flight delays remain one of the major operational challenges in the aviation industry. Delays can increase airline operating costs, disrupt airport schedules, and negatively affect passenger satisfaction. Early prediction of flight delays enables airlines to make informed operational decisions, optimize resource allocation, and communicate expected delays to passengers before departure.

This project presents a complete machine learning solution for predicting whether a flight will depart **On-Time** or **Delayed** based on historical flight information. Several classification algorithms were trained, evaluated, and compared to determine the most suitable model for deployment.

Three supervised learning algorithms were implemented:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

After evaluating the models using multiple classification metrics, the best-performing model was selected and deployed using FastAPI. A user-friendly web interface was also developed using HTML and CSS, allowing users to enter flight information and receive real-time predictions together with prediction confidence.

This project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, deployment, and user interaction.

---

# Table of Contents

1. Introduction
2. Problem Statement
3. Project Objectives
4. Dataset Description
5. Data Preprocessing
6. Machine Learning Models
7. Model Evaluation
8. Results and Discussion
9. Deployment
10. Challenges
11. Lessons Learned
12. Future Improvements
13. Conclusion

---

# 1. Introduction

Air transportation plays an essential role in connecting people and businesses worldwide. Every day, thousands of commercial flights operate across different airports, serving millions of passengers. Despite improvements in aviation technology and operational planning, flight delays remain a common issue affecting airlines and travelers.

A delayed flight often causes missed connections, increased operational expenses, scheduling conflicts, and customer dissatisfaction. Airlines therefore seek intelligent systems capable of predicting delays before departure so that preventive measures can be taken.

Machine Learning provides an effective solution by learning patterns from historical flight data. Instead of relying on manual rules, machine learning models automatically identify relationships between flight characteristics and delay outcomes.

The primary objective of this project is to build an accurate classification model capable of predicting whether a scheduled flight will be **On-Time** or **Delayed**.

---

# 2. Problem Statement

Flight delays have significant financial and operational consequences for airlines. Unpredictable delays reduce efficiency and negatively impact passenger experience.

The challenge addressed in this project is to develop a machine learning model capable of accurately classifying flights into one of two categories:

- **On-Time**
- **Delayed**

The prediction system should provide fast, reliable, and interpretable results while supporting deployment through a web application.

---

# 3. Project Objectives

The main objectives of this project are:

- Study historical flight information.
- Clean and preprocess raw flight data.
- Transform categorical variables into machine learning features.
- Scale numerical variables.
- Train multiple classification algorithms.
- Compare model performance.
- Select the best-performing model.
- Deploy the final model using FastAPI.
- Build a responsive web interface for end users.

---

# 4. Dataset Description

## Dataset Overview

The project uses a Flight Delay dataset containing historical flight information collected from airline operations.

Each observation represents a single scheduled flight.

The prediction target indicates whether the flight departed on time or experienced a delay.

## Dataset Size

| Item | Value |
|------|------:|
| Rows | 539,382 |
| Features | 7 |
| Target Variable | Class |

## Target Variable

>>>>>>> 83876d23551c1ef5c90541491dac5802fca59096
| Value | Meaning |
|------:|---------|
| 0 | On-Time |
| 1 | Delayed |
<<<<<<< HEAD

---

# 5. Data Preprocessing

Before training the models, several preprocessing steps were performed:

- Dataset inspection
- Duplicate removal
- Missing value checking
- One-Hot Encoding for categorical features
- Feature scaling using StandardScaler
- Saving preprocessing artifacts for deployment

These preprocessing steps ensured consistency between training and prediction.

# 6. Machine Learning Models

Three classification algorithms were trained and evaluated.

## Logistic Regression

Logistic Regression was used as the baseline classifier because it is simple, fast, and easy to interpret.

## Random Forest

Random Forest combines multiple decision trees to improve prediction accuracy. It demonstrated the best overall performance in this project.

## Gradient Boosting

Gradient Boosting builds trees sequentially by correcting previous prediction errors. It achieved competitive performance but was slightly lower than Random Forest.

---

# 7. Model Evaluation
=======

## Input Features

| Feature | Description |
|---------|-------------|
| Flight | Flight identification number |
| Time | Scheduled departure time |
| Length | Flight duration |
| Airline | Airline code |
| AirportFrom | Departure airport |
| AirportTo | Destination airport |
| DayOfWeek | Day on which the flight operates |

The dataset contains both numerical and categorical variables, making preprocessing an essential step before model training.

---

# 5. Data Preprocessing

Raw datasets are rarely suitable for direct use in machine learning models. Before model training, the dataset was carefully inspected and transformed into a clean and structured format. Proper preprocessing improves model performance, reduces noise, and ensures consistency between training and deployment.

The following preprocessing steps were applied.

## 5.1 Data Inspection

The dataset was first loaded into a Pandas DataFrame and inspected to understand its overall structure.

The following checks were performed:

- Dataset dimensions
- Data types
- Missing values
- Duplicate records
- Target distribution
- Summary statistics

These checks helped identify potential quality issues before model training.

---

## 5.2 Duplicate Handling

Duplicate records can negatively affect model learning by introducing repeated observations.

The dataset was examined for duplicate rows, and duplicated records were removed to improve data quality and reduce unnecessary bias during training.

---

## 5.3 Missing Value Analysis

The dataset was checked for missing values in every feature.

Missing values may reduce model performance if left untreated.

After inspection, the dataset contained either no significant missing values or they were handled appropriately before model training.

---

## 5.4 Categorical Feature Encoding

Machine learning algorithms cannot process text directly.

The following categorical features were transformed using **One-Hot Encoding**.

| Feature |
|----------|
| Airline |
| AirportFrom |
| AirportTo |

One-Hot Encoding converts each category into numerical binary columns while preserving information without introducing ordinal relationships.

Example:

| Airline |
|----------|
| AA |
| DL |
| UA |

becomes

| Airline_AA | Airline_DL | Airline_UA |
|------------|------------|------------|
| 1 | 0 | 0 |

---

## 5.5 Feature Scaling

Numerical variables often have different ranges.

The following numerical variables were standardized using **StandardScaler**.

- Flight
- Time
- Length
- DayOfWeek

Standardization transforms features to have approximately:

- Mean = 0
- Standard Deviation = 1

Scaling improves learning efficiency for several machine learning algorithms.

---

## 5.6 Preparing Features for Deployment

One challenge during deployment is ensuring that prediction inputs contain exactly the same feature structure used during training.

To solve this problem:

- Training feature names were saved.
- The fitted StandardScaler was saved.
- During prediction, incoming user data is transformed using the same preprocessing pipeline.

This guarantees consistency between training and inference.

---

# 6. Exploratory Data Analysis (EDA)
>>>>>>> 83876d23551c1ef5c90541491dac5802fca59096

Exploratory Data Analysis was performed to better understand the characteristics of the dataset before model development.

Several statistical summaries and visualizations were generated.

The analysis focused on:

- Distribution of the target variable
- Numerical feature distributions
- Relationships between variables
- Category frequencies
- Data balance

EDA provides useful insights that guide preprocessing and model selection.

---

## 6.1 Target Distribution

The target variable represents whether a flight departed on time or experienced a delay.

Target classes:

| Class | Description |
|--------|-------------|
| 0 | On-Time |
| 1 | Delayed |

Understanding class balance is important because highly imbalanced datasets may require additional preprocessing techniques.

---

## 6.2 Feature Relationships

Relationships between numerical variables were examined to identify possible correlations.

Examples include:

- Flight Length vs Delay
- Departure Time vs Delay
- Day of Week vs Delay

These relationships help explain how different factors influence flight delays.

---

## 6.3 Categorical Analysis

Categorical variables were analyzed individually.

Important observations included:

- Airlines with higher delay frequencies
- Airports associated with more delays
- Common departure and destination airports

Such insights improve understanding of the operational characteristics represented in the dataset.

---

# 7. Machine Learning Models

Three supervised classification algorithms were trained and compared.

Each model predicts whether a flight is expected to be **On-Time** or **Delayed**.

---

## 7.1 Logistic Regression

Logistic Regression is one of the most widely used binary classification algorithms.

Instead of predicting continuous values, it estimates the probability that an observation belongs to a particular class.

Advantages include:

- Fast training
- Simple implementation
- Easy interpretation
- Strong baseline model

Limitations include:

- Assumes mostly linear relationships
- Less effective for highly complex patterns

---

## 7.2 Random Forest Classifier

Random Forest is an ensemble learning algorithm composed of multiple decision trees.

Each tree makes an independent prediction, and the final prediction is determined through majority voting.

Advantages include:

- High prediction accuracy
- Handles nonlinear relationships
- Robust against overfitting
- Performs well on mixed feature types

Random Forest produced the strongest overall performance during this project.

---

## 7.3 Gradient Boosting Classifier

Gradient Boosting builds trees sequentially.

Each new tree attempts to correct errors made by previous trees.

Advantages include:

- High predictive performance
- Captures complex relationships
- Handles structured datasets effectively

Disadvantages:

- Longer training time
- Requires careful parameter tuning

Despite its strong predictive ability, it performed slightly below the selected best model in this project.

---

## 7.4 Model Training

The dataset was divided into training and testing subsets.

General workflow:

```
Dataset
    │
    ▼
Preprocessing
    │
    ▼
Train/Test Split
    │
    ▼
Train Models
    │
    ▼
Evaluate Performance
    │
    ▼
Select Best Model
```

Each algorithm was trained using the same processed dataset to ensure a fair comparison.

The resulting trained models were saved using **Joblib** for later deployment in the FastAPI application.


---

# 8. Model Evaluation

After training the machine learning models, each algorithm was evaluated using a separate testing dataset. Model evaluation is essential because it measures how well a trained model performs on unseen data and helps identify the most reliable classifier for deployment.

The following evaluation metrics were used:

- Accuracy
- Precision
- Recall
- F1-Score

<<<<<<< HEAD
## Model Comparison

| Model | Description |
|--------|-------------|
| Logistic Regression | Baseline model |
| Random Forest | Best performing model |
| Gradient Boosting | High-performance boosting model |

Random Forest achieved the highest overall performance and was selected for deployment.

---

# 8. Deployment

The selected model was deployed using **FastAPI**.

The web application was developed using:

- HTML
- CSS
- FastAPI
- Scikit-learn
- Joblib

Users enter flight information through a simple interface, and the system predicts whether the flight will be **On-Time** or **Delayed**, together with the confidence score.

---

# 9. Challenges

During development, several challenges were encountered:

- Preparing categorical variables for prediction.
- Keeping training and prediction features consistent.
- Integrating FastAPI with the HTML interface.
- Loading the trained machine learning model correctly.

These challenges were solved by implementing a reusable preprocessing pipeline and saving the trained preprocessing objects.

---

# 10. Conclusion

This project successfully demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and deployment.
=======
Each metric provides different insights into model performance and together they offer a comprehensive evaluation.

## 8.1 Accuracy

Accuracy measures the proportion of correctly classified observations.

**Formula**

Accuracy = Correct Predictions / Total Predictions

Although accuracy is useful, it should not be the only metric considered because it may produce misleading results when datasets are imbalanced.

---

## 8.2 Precision

Precision measures how many flights predicted as delayed were actually delayed.

High precision means the model produces fewer false alarms.

---

## 8.3 Recall

Recall measures how many delayed flights were successfully identified.

High recall is important because missing delayed flights can negatively affect airline planning.

---

## 8.4 F1-Score

F1-Score combines Precision and Recall into one metric.

It provides a balanced evaluation when both false positives and false negatives are important.

---

# 9. Model Comparison

Three classification algorithms were trained and evaluated using the same preprocessing pipeline.

| Model | Strength | Performance |
|--------|----------|-------------|
| Logistic Regression | Simple and interpretable | Good baseline |
| Random Forest | High accuracy and stability | Best Overall |
| Gradient Boosting | Powerful boosting algorithm | Competitive |

Random Forest produced the most reliable predictions and was therefore selected as the final deployment model.

---

# 10. Deployment

The selected model was deployed using **FastAPI**, allowing users to make predictions through a web application.

The deployment process consisted of the following components:

- FastAPI backend
- HTML user interface
- CSS styling
- Joblib model loading
- Prediction pipeline
- Real-time classification

The application accepts user input through an HTML form, processes the features, loads the trained model, and returns the predicted flight status together with the confidence score.

---

## Deployment Workflow

```
User

   │

   ▼

HTML Form

   │

   ▼

FastAPI Backend

   │

   ▼

Feature Preparation

   │

   ▼

Machine Learning Model

   │

   ▼

Prediction

   │

   ▼

Display Result
```

---

# 11. Web Application

A simple web application was developed to demonstrate the trained model.

The user enters the following information:

- Flight Number
- Departure Time
- Flight Length
- Airline
- Departure Airport
- Destination Airport
- Day of Week

After clicking **Predict Flight**, the application displays:

- Logistic Regression Prediction
- Random Forest Prediction
- Gradient Boosting Prediction
- Best Model
- Final Prediction
- Prediction Confidence

This interface allows users to interact with the model without using code.

---

# 12. Challenges Encountered

Several technical challenges were encountered during the project.

### Data Preprocessing

Preparing categorical variables while maintaining consistency between training and deployment required careful feature alignment.

### Feature Encoding

Ensuring that new user inputs generated exactly the same feature columns as the training dataset was an important deployment challenge.

### Model Deployment

Integrating the trained machine learning model with FastAPI and connecting it to an HTML interface required additional debugging and testing.

### Prediction Consistency

The preprocessing pipeline used during prediction had to exactly match the preprocessing performed during model training to ensure reliable results.

---

# 13. Lessons Learned

This project provided valuable practical experience throughout the complete machine learning lifecycle.
>>>>>>> 83876d23551c1ef5c90541491dac5802fca59096

Three machine learning algorithms were compared, with **Random Forest** selected as the best-performing model.

<<<<<<< HEAD
The deployed FastAPI application provides a simple and effective way for users to predict whether a flight is likely to be **On-Time** or **Delayed**.

This project highlights the practical application of machine learning in solving real-world aviation problems.

---

=======
- Understanding real-world classification problems.
- Importance of data preprocessing.
- Working with categorical and numerical features.
- Comparing multiple machine learning algorithms.
- Evaluating model performance using multiple metrics.
- Saving trained models using Joblib.
- Building REST APIs with FastAPI.
- Creating interactive machine learning web applications.
- Integrating backend models with frontend interfaces.

---

# 14. Future Improvements

Several improvements could further enhance the project.

These include:

- Hyperparameter optimization
- Cross-validation
- Feature engineering
- Additional flight-related features
- Real-time flight information
- Cloud deployment
- User authentication
- Prediction history
- Dashboard visualization
- Mobile-friendly interface

These improvements would increase both prediction accuracy and overall usability.

---

# 15. Conclusion

This project successfully developed a complete machine learning system capable of predicting flight delays using historical flight information.

The project followed the full machine learning pipeline, including:

- Data collection
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Model comparison
- Deployment using FastAPI
- Development of an interactive web interface

Three supervised learning algorithms were trained and compared:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

Among these models, **Random Forest Classifier** demonstrated the strongest overall performance and was selected as the production model.

The deployed application allows users to submit flight information through a web interface and instantly receive predictions indicating whether a flight is likely to be **On-Time** or **Delayed**, together with the model's confidence score.

Overall, this project demonstrates how machine learning can be applied to solve real-world aviation problems while providing an accessible and user-friendly deployment solution.

---

>>>>>>> 83876d23551c1ef5c90541491dac5802fca59096
