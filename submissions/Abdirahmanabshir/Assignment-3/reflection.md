# Data Preprocessing Reflection

## Step 1 – Inspection
I inspected the dataset using head(), shape, info(), missing values, and value counts to understand its quality before cleaning.

## Step 2 – Price Cleaning
I removed currency symbols and commas, then converted Price to float so it could be used for analysis and machine learning.

## Step 3 – Category Cleaning
I corrected spelling mistakes (Subrb → Suburb) and converted unknown values (??) into missing values before imputation.

## Step 4 – Missing Values
I used the median for Odometer_km because it is robust to outliers. I used the mode for Doors, Accidents, and Location because they represent the most common values.

## Step 5 – Duplicate Removal
I removed duplicate rows to avoid giving repeated observations extra influence during model training.

## Step 6 – Outlier Capping
I used the IQR method to detect and cap extreme values in Price and Odometer_km while keeping all observations.

## Step 7 – One-Hot Encoding
I converted the Location column into numerical dummy variables so machine learning algorithms can use it.

## Step 8 – Feature Engineering
I created CarAge, Km_per_Year, Is_Urban, and LogPrice to provide more useful information to the model.

## Step 9 – Feature Scaling
I standardized continuous numerical features using StandardScaler while leaving the target variables and dummy variables unchanged.

## Step 10 – Final Checks
I confirmed that there were no missing values, verified the data types, and saved the cleaned dataset.