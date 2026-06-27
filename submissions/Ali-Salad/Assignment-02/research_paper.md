Social Media Usage Among the Somali Population
Ali Salad | DS/ML Bootcamp | Assignment 02 | June 2026

1. Dataset Overview
This dataset examines social media usage patterns among internet-connected Somalis across Mogadishu, Hargeisa, Kismayo, Bosasso, and Baidoa. Data was collected via structured survey (Google Forms and paper, dual Somali/English), targeting ages 13-55 across varying income, education, and urban/rural backgrounds. 106 raw responses were gathered; after removing duplicates and blank rows, 101 usable rows remain.

2. Features & Label

Input Features (X) - 13 variables:
Feature | Type | Description
AGE | Numeric | Respondent age in years
Gender | Categorical | Male, Female, Other
City/Town | Categorical | Somali city of residence
Platform Used | Categorical | Primary platform (Facebook, TikTok, etc.)
Daily Usage (hrs) | Numeric | Average daily hours on social media
Frequency | Categorical | Daily, Weekly, Rarely
Internet Type | Categorical | Mobile Data, WiFi, Broadband, Both
Device | Categorical | Smartphone, Laptop, Tablet
Monthly Income | Numeric | Estimated income in USD
Education Level | Categorical | Highest level attained
Purpose | Categorical | Entertainment, Business, News, etc.
Date Surveyed | Date | Survey completion date
Name | - | Dropped pre-modelling (privacy)

Target Label (y): Satisfaction - ordinal integer scale 1-5 (1 = Very Dissatisfied, 5 = Very Satisfied). Raw data contained mixed text/numeric formats, unified during cleaning.

3. Data Quality Issues

Issue | Column(s) | Detail
Missing values | All 15 columns | 5-35 NaNs per column; AGE: 25, Internet Type: 35
Impossible values | AGE, Daily Usage | AGE: 999, -5; Usage: 25 hrs/day, -1 hr
Text-as-number | AGE | "Twenty" stored as string
Inconsistent casing | Gender, Platform, City | "male", "MALE", "M", "m" - same value
Mixed abbreviations | City, Platform | "MGQ"/"Xamar" = Mogadishu; "FB"/"FACEBOOK"
Numeric format mix | Monthly Income | "", "977 USD", "low", bare integers
Date format mix | Date Surveyed | Six formats including DD/MM/YYYY, "May 2024"
Mixed satisfaction scale | Satisfaction | Text ("Satisfied") and numeric (1-5) combined
Duplicates | All columns | 5 fully duplicated rows
Blank rows | All columns | 5 completely empty rows
Class imbalance | Platform Used | Facebook/Instagram over-represented

Cleaning applied a 19-step pipeline: null standardisation, type coercion, value normalisation, IQR-based outlier capping, duplicate removal, date parsing, and StandardScaler feature scaling. Final feature space: 65 columns post one-hot encoding.

4. Learning Type

This is a supervised classification problem. Each row has a known label (Satisfaction), making the task learning a mapping f(X) -> y. With five ordinal classes, suitable algorithms include Random Forest, Logistic Regression (multi-class), and Gradient Boosting.

5. ML Use Cases

Classification (primary): Predict satisfaction score from demographic and usage features - useful for telecoms and platforms identifying dissatisfied users.
Regression (secondary): Predict daily usage from age, income, and platform - relevant for advertising targeting or digital wellbeing tools.
Clustering (exploratory): Segment users by behaviour and location without the label - applicable for market segmentation across Somali cities.
