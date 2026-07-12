import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
CSV_PATH='raw_car_dataset.csv'

df=pd.read_csv(CSV_PATH)

# print(df.head(10))
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())
# print(df["Location"].value_counts(dropna=False))

df["Price"]=df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print(df["Price"].head(10))

df["Location"]=df["Location"].replace({"Subrb" : "Suburb", "??" : pd.NA})

# print(df["Location"].value_counts(dropna=False))

df["Size_sqft"]=df["Size_sqft"].fillna(df["Size_sqft"].median())
df["Bedrooms"]=df["Bedrooms"].fillna(df["Bedrooms"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])

# print(df.isnull().sum())

before=df.shape
df=df.drop_duplicates()
after=df.shape

# print("Before:",before, "After:",after)

def iqr_fun(series, k=1.5):
    q1, q3 =series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower=q1-k*iqr
    upper=q3+k*iqr
    return lower,upper



lower_price, high_price=iqr_fun(df["Price"])
lower_size, high_size=iqr_fun(df["Size_sqft"])

# print(lower_price,high_price)
# print(lower_size,high_size)
df["Price"]=df["Price"].clip(lower=lower_price, upper=high_price)
df["Size_sqft"]=df["Size_sqft"].clip(lower=lower_size, upper=high_size)

# print(df["Price"].describe())
df=pd.get_dummies(df, columns=["Location"], drop_first=False).astype(int)

# print([ c for c in df.columns if c.startswith("Location")])
# print(df.head(10))

CURRENT_YEAR=2026
df["HouseAge"]=CURRENT_YEAR - df["YearBuilt"]
# print(df.head())
df["Rooms_Per_1000sqft"]=(df["Bathrooms"]+df["Bedrooms"]) / (df["Size_sqft"] /1000)
# print(df.head())
df["Size_per_Bedrooms"]=df["Size_sqft"] / df["Bedrooms"].replace(0, np.nan)

# print(df.head())

df["Is_City"]=df["Location_City"].astype(int)

# print(df.head())
df["Log_Price"]=np.log(df["Price"])

# print(df["Log_Price"])

dont_scale={"Price", "Log_Price"}
numeric_col=df.select_dtypes(include=["int64","float64"]).columns.tolist()
exclude=[c for c in df.columns if c.startswith("Location_")]+ ["Is_City"]
num_features_to_scale=[c for c in numeric_col if c not in exclude and c not in dont_scale]

scaler = StandardScaler()
df[num_features_to_scale]=scaler.fit_transform(df[num_features_to_scale])

OUT_PUT="clean_car_dataset.csv"
df.to_csv(OUT_PUT, index=False)