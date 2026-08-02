# ✈️Flight Delay Prediction System Using Machine Learning

## Abstract

The aviation industry depends heavily on punctual flight operations to ensure customer satisfaction and operational efficiency. However, unexpected delays continue to be a major challenge for airlines worldwide. Delayed flights increase operational costs, disrupt airport schedules, and negatively impact passengers. As the volume of air travel continues to grow, the need for intelligent systems capable of predicting delays has become increasingly important.

This project develops a machine learning system that predicts whether a scheduled flight will arrive **On-Time** or **Delayed** using historical flight information. Several supervised learning algorithms were trained and compared to identify the most accurate model. The selected model was deployed through a FastAPI web application, allowing users to obtain predictions using a simple web interface.

The project demonstrates the complete machine learning lifecycle, including data preprocessing, model development, evaluation, deployment, and user interaction.

---

# 1. Introduction

Flight delays affect millions of travelers every year and create significant operational challenges for airlines. Even a short delay may cause missed connections, increased fuel consumption, additional staffing costs, and passenger dissatisfaction.

Advances in machine learning provide new opportunities for analyzing historical flight data and predicting future delays. By identifying hidden patterns within flight information, predictive models can assist airlines in making informed operational decisions before departure.

This project focuses on building a classification model capable of predicting flight status using several important flight characteristics.

---

# 2. Project Goals

The primary goal of this project is to build an intelligent prediction system capable of determining whether a flight will be delayed.

Specific objectives include:

- Understanding the flight dataset.
- Cleaning and preparing the data.
- Encoding categorical variables.
- Scaling numerical variables.
- Training multiple classification algorithms.
- Comparing model performance.
- Deploying the best model using FastAPI.
- Building an interactive prediction website.

---

# 3. Dataset Overview

The dataset contains historical flight records collected from airline operations.

Each record represents one scheduled flight and includes operational information used for prediction.

## Dataset Summary

| Item | Value |
|------|------:|
| Total Records | 539,382 |
| Input Features | 7 |
| Target Classes | 2 |

### Input Variables

| Variable | Description |
|----------|-------------|
| Flight | Flight identification number |
| Time | Scheduled departure time |
| Length | Flight duration |
| Airline | Airline code |
| AirportFrom | Departure airport |
| AirportTo | Destination airport |
| DayOfWeek | Day of operation |

### Target Variable

| Value | Meaning |
|------:|---------|
| 0 | On-Time |
| 1 | Delayed |

The dataset contains both numerical and categorical variables, making preprocessing essential before model training.

---

# 4. Data Preparation

Raw datasets often contain inconsistencies that reduce machine learning performance. Therefore, several preprocessing techniques were applied before model training.

The preparation process included:

- Inspecting the dataset structure.
- Removing duplicate observations.
- Checking missing values.
- Encoding categorical variables using One-Hot Encoding.
- Standardizing numerical variables with StandardScaler.
- Saving preprocessing objects for future prediction.

These steps ensured that both training data and user input followed the same transformation process during deployment.

# Git Repository:

https://github.com/fatima-moha143/fligh_delay_predict.git
