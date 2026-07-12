# Reflection

## Data Preprocessing Reflection

In this assignment, I built a preprocessing pipeline to clean and prepare the dataset for machine learning. My goal was to make the data consistent, remove errors, and create useful features while avoiding data leakage.

### Data Inspection

I started by loading the dataset and inspecting its structure using methods such as `head()`, `shape`, `info()`, and checking for missing values. This helped me identify formatting issues, missing data, duplicate rows, and inconsistent categorical values.

### Cleaning the Target Variable

The `Price` column contained currency symbols and commas, so I removed these characters before converting the column to a numeric data type. This ensured that mathematical operations could be performed correctly on the target variable.

### Fixing Category Errors

The `Location` column contained inconsistent values such as `"Subrb"` and `"??"`. I corrected the typo by changing `"Subrb"` to `"Suburb"` and treated `"??"` as a missing value. Cleaning categorical values before imputation prevents similar categories from being treated as different groups.

### Handling Missing Values

I selected different imputation methods based on the type of data:

* I used the **median** for `Size_sqft` because it is less affected by extreme values.
* I used the **mode** for `Bedrooms` and `Location` because these are categorical or discrete variables where the most common value is a reasonable replacement.

### Removing Duplicates

I removed duplicate rows to avoid repeated observations that could bias analysis or machine learning models. I also compared the dataset shape before and after removing duplicates to confirm the number of rows removed.

### Handling Outliers

I applied the **Interquartile Range (IQR)** method to detect outliers in `Price` and `Size_sqft`. Instead of deleting these records, I capped them using the upper and lower IQR limits. This reduces the influence of extreme values while keeping all observations.

### Encoding Categorical Data

I converted the `Location` column into one-hot encoded columns. This allows machine learning algorithms to work with categorical data without assuming any order between categories.

### Feature Engineering

I created several additional features to provide more useful information:

* **HouseAge** calculates the age of the house using the current year.
* **Rooms_Per_1000sqft** measures room density relative to property size.
* **Size_per_Bedrooms** estimates the average space available per bedroom.
* **Is_City** is a binary indicator showing whether the property is located in the city.
* **Log_Price** applies a logarithmic transformation to the target variable to reduce skewness and provide an alternative target for future modeling.

### Feature Scaling

I standardized continuous numerical features using `StandardScaler`. I intentionally did not scale `Price`, `Log_Price`, or the one-hot encoded location columns because target variables and binary indicator variables generally should not be standardized.

### Conclusion

This preprocessing pipeline produced a clean dataset with consistent values, no missing data, engineered features, encoded categorical variables, reduced outlier effects, and standardized numerical features. The final dataset is ready for machine learning and further analysis.
