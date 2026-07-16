import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ===============================
# STEP 1: LOAD & INSPECT
# ===============================

CSV_PATH = "../../../dataset/raw_car_dataset.csv"

df = pd.read_csv(CSV_PATH)

print("\n========== STEP 1: LOAD & INSPECT ==========\n")

print("First 10 Rows")
print(df.head(10))

print("\nShape")
print(df.shape)

print("\nDataset Info")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("\nLocation Value Counts")
print(df["Location"].value_counts(dropna=False))

print("\nKey Issues Found:")
print("- Price contains mixed formatting.")
print("- Missing values exist.")
print("- Location contains typos and unknown values.")
print("- Dataset contains duplicates and outliers.")

# ===============================
# STEP 2: CLEAN PRICE
# ===============================

print("\n========== STEP 2: CLEAN PRICE ==========\n")

df["Price"] = (
    df["Price"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

print("Price Data Type:")
print(df["Price"].dtype)

print("\nPrice Skewness:")
print(df["Price"].skew())

# ===============================
# STEP 3: FIX CATEGORY ERRORS
# ===============================

print("\n========== STEP 3: FIX CATEGORY ERRORS ==========\n")

df["Location"] = (
    df["Location"]
    .replace({
        "Subrb": "Suburb",
        "??": pd.NA
    })
)

print(df["Location"].value_counts(dropna=False))

# ===============================
# STEP 4: IMPUTE MISSING VALUES
# ===============================

print("\n========== STEP 4: IMPUTE MISSING VALUES ==========\n")

df["Odometer_km"] = df["Odometer_km"].fillna(
    df["Odometer_km"].median()
)

df["Doors"] = df["Doors"].fillna(
    df["Doors"].mode()[0]
)

df["Accidents"] = df["Accidents"].fillna(
    df["Accidents"].mode()[0]
)

df["Location"] = df["Location"].fillna(
    df["Location"].mode()[0]
)

print("Missing Values After Imputation")
print(df.isnull().sum())

# ===============================
# STEP 5: REMOVE DUPLICATES
# ===============================

print("\n========== STEP 5: REMOVE DUPLICATES ==========\n")

before = df.shape

df = df.drop_duplicates()

after = df.shape

print(f"Before : {before}")
print(f"After  : {after}")

print(f"Rows Removed : {before[0] - after[0]}")

# ===============================
# STEP 6: OUTLIER CAPPING (IQR)
# ===============================

print("\n========== STEP 6: OUTLIER CAPPING ==========\n")


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - (k * iqr)
    upper = q3 + (k * iqr)
    return lower, upper


# Price
low_price, high_price = iqr_fun(df["Price"])

# Odometer
low_odo, high_odo = iqr_fun(df["Odometer_km"])

# Cap outliers
df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

print("Price Bounds:")
print(f"Lower: {low_price:.2f}")
print(f"Upper: {high_price:.2f}")

print("\nOdometer Bounds:")
print(f"Lower: {low_odo:.2f}")
print(f"Upper: {high_odo:.2f}")

print("\nSummary After Capping")
print(df[["Price", "Odometer_km"]].describe())

# ===============================
# STEP 7: ONE-HOT ENCODING
# ===============================

print("\n========== STEP 7: ONE-HOT ENCODING ==========\n")

df = pd.get_dummies(
    df,
    columns=["Location"],
    drop_first=False,
    dtype=int
)

print("New Dummy Columns:")

location_cols = [col for col in df.columns if col.startswith("Location_")]

print(location_cols)

# ===============================
# STEP 8: FEATURE ENGINEERING
# ===============================

print("\n========== STEP 8: FEATURE ENGINEERING ==========\n")

CURRENT_YEAR = 2025

# Feature 1
df["CarAge"] = CURRENT_YEAR - df["Year"]

# Feature 2
df["Km_per_Year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)

# Feature 3
df["Is_Urban"] = (
    df["Location_City"] |
    df["Location_Suburb"]
).astype(int)

# Alternative Target
df["LogPrice"] = np.log1p(df["Price"])

print(df.head())

# ===============================
# STEP 9: FEATURE SCALING
# ===============================

print("\n========== STEP 9: FEATURE SCALING ==========\n")

dont_scale = {"Price", "LogPrice"}

dummy_cols = [col for col in df.columns if col.startswith("Location_")]

exclude = dummy_cols + ["Is_Urban"]

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

features_to_scale = [
    col for col in numeric_cols
    if col not in dont_scale
    and col not in exclude
]

scaler = StandardScaler()

df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

print(df[features_to_scale].head())

# ===============================
# STEP 10: FINAL CHECKS
# ===============================

print("\n========== STEP 10: FINAL CHECKS ==========\n")

print("Dataset Info")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("\nDescribe")
print(df.describe())

OUT_PATH = "./clean_car_dataset.csv"

df.to_csv(OUT_PATH, index=False)

print(f"\nDataset successfully saved to: {OUT_PATH}")


# ===============================
# SANITY CHECKS
# ===============================

assert df["Price"].dtype == float

assert "LogPrice" in df.columns

assert df.isnull().sum().sum() == 0

assert any(col.startswith("Location_") for col in df.columns)

scaled_means = df[features_to_scale].mean().round()

print("\nScaled Means")
print(scaled_means)

print("\nAll sanity checks passed!")
