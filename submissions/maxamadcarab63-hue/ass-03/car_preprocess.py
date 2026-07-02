import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sklearn

CSV_PATH='car_l3_dataset.csv'

df=pd.read_csv(CSV_PATH)

# print(df.head(10))
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print(df["Price"].head(10))
# print(df["Price"].skew())

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
# print("Location Counts After Type/unknown fix")
# print(df["Location"].value_counts(dropna=False))

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])
# print(df.isnull().sum())

before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("Before: ", "After: ", after)

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size,  high_size  = iqr_fun(df["Odometer_km"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_size,  upper=high_size)
# print("Price after IQR clipping: ")
# print(df["Price"].describe())

df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
# print("One Hot Encoded of location: ")
# print([c for c in df.columns if c.startswith("Location")])
# print(df.head(10))

CURRENT_YEAR = 2026
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Is_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])
# print(df.head())

dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
# print("After Scaling")
# print(df.head())


# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) Save
OUT_PATH = "car_l3_dataset.csv"
df.to_csv(OUT_PATH, index=False)