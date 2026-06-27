import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

RAW_PATH = "raw_car_dataset.csv"
OUTPUT_PATH = "clean_car_dataset.csv"

print("=" * 70)
print("STEP 1: Load & Inspect")
print("=" * 70)

df = pd.read_csv(RAW_PATH)

print("\nhead(10):")
print(df.head(10))

print("\nshape:", df.shape)

print("\ninfo():")
df.info()

print("\nMissing value counts:")
print(df.isna().sum())

print("\nLocation value counts (raw):")
print(df["Location"].value_counts(dropna=False))

print(
    "\nKey issues observed:\n"
    "- Price is stored as text, mixing plain numbers with '$' and commas "
    "(e.g. '$1,500').\n"
    "- Odometer_km and Doors have missing values.\n"
    "- Location has typos ('Subrb') and unknown placeholders ('??'), plus "
    "real missing values.\n"
    "- There appear to be duplicate rows.\n"
    "- Price and Odometer_km contain extreme outliers (e.g. 135000, "
    "120000, 380000+ km) that look like data entry errors.\n"
)


# ---------------------------------------------------------------------------
# Step 2: Clean Target Formatting (Price)
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 2: Clean Target Formatting (Price)")
print("=" * 70)

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

print("\nPrice dtype:", df["Price"].dtype)
print("Price skewness:", round(df["Price"].skew(), 3))
print("\nPrice describe():")
print(df["Price"].describe())


# ---------------------------------------------------------------------------
# Step 3: Fix Category Errors before Imputation
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 3: Fix Category Errors before Imputation")
print("=" * 70)

df["Location"] = df["Location"].astype(str).str.strip()
df["Location"] = df["Location"].replace({"nan": np.nan})

location_map = {
    "Subrb": "Suburb",
    "City": "City",
    "Suburb": "Suburb",
    "Rural": "Rural",
}
df["Location"] = df["Location"].replace(location_map)

# Convert unknown markers to true missing values
df["Location"] = df["Location"].replace({"??": np.nan})

print("\nLocation value counts (after normalizing typos/unknowns):")
print(df["Location"].value_counts(dropna=False))

print("\nMissing counts after this step:")
print(df.isna().sum())


# ---------------------------------------------------------------------------
# Step 4: Impute Missing Values (justify choices)
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 4: Impute Missing Values")
print("=" * 70)

odometer_median = df["Odometer_km"].median()
doors_mode = df["Doors"].mode()[0]
location_mode = df["Location"].mode()[0]

print(f"\nOdometer_km median used for imputation: {odometer_median}")
print(f"Doors mode used for imputation: {doors_mode}")
print(f"Location mode used for imputation: {location_mode}")
print(
    "\nJustification:\n"
    "- Odometer_km is a continuous numeric feature with outliers, so the "
    "median is more robust than the mean.\n"
    "- Doors is a discrete/categorical-like numeric feature with a small "
    "set of repeated values, so the mode (most common value) makes more "
    "sense than a median or mean.\n"
    "- Location is categorical, so the mode is the only sensible central "
    "tendency.\n"
    "- Accidents has no missing values, so it needs no imputation.\n"
)

df["Odometer_km"] = df["Odometer_km"].fillna(odometer_median)
df["Doors"] = df["Doors"].fillna(doors_mode)
df["Location"] = df["Location"].fillna(location_mode)

print("Missing counts after imputation:")
print(df.isna().sum())


# ---------------------------------------------------------------------------
# Step 5: Remove Duplicates
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 5: Remove Duplicates")
print("=" * 70)

shape_before = df.shape
n_duplicates = df.duplicated().sum()
df = df.drop_duplicates().reset_index(drop=True)
shape_after = df.shape

print(f"\nShape before: {shape_before}")
print(f"Shape after: {shape_after}")
print(f"Rows removed: {shape_before[0] - shape_after[0]}")


# ---------------------------------------------------------------------------
# Step 6: Outliers (IQR capping)
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 6: Outliers (IQR capping)")
print("=" * 70)


def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper


price_lower, price_upper = iqr_bounds(df["Price"])
odo_lower, odo_upper = iqr_bounds(df["Odometer_km"])

print(f"\nPrice IQR bounds: lower={price_lower:.2f}, upper={price_upper:.2f}")
print(f"Odometer_km IQR bounds: lower={odo_lower:.2f}, upper={odo_upper:.2f}")

df["Price"] = df["Price"].clip(lower=price_lower, upper=price_upper)
df["Odometer_km"] = df["Odometer_km"].clip(lower=odo_lower, upper=odo_upper)

print("\nPrice describe() after capping:")
print(df["Price"].describe())
print("\nOdometer_km describe() after capping:")
print(df["Odometer_km"].describe())


# ---------------------------------------------------------------------------
# Step 7: One-Hot Encode Categorical(s)
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 7: One-Hot Encode Categorical(s)")
print("=" * 70)

cols_before = set(df.columns)
df = pd.get_dummies(df, columns=["Location"], prefix="Location")
new_cols = sorted(set(df.columns) - cols_before)

print("\nNew one-hot columns created:")
print(new_cols)

# get_dummies produces boolean columns in recent pandas; cast to int for clarity
for col in new_cols:
    df[col] = df[col].astype(int)


# ---------------------------------------------------------------------------
# Step 8: Feature Engineering (no leakage)
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 8: Feature Engineering")
print("=" * 70)

current_year = 2026  # snapshot year of this dataset/assignment

df["CarAge"] = current_year - df["Year"]

# Safe handling: avoid division by zero for brand-new cars (age 0)
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

is_urban_col = "Location_City" if "Location_City" in df.columns else None
if is_urban_col:
    df["Is_Urban"] = df[is_urban_col]
else:
    df["Is_Urban"] = 0

df["LogPrice"] = np.log(df["Price"] + 1)

print(
    "\nFeatures engineered: CarAge, Km_per_year, Is_Urban "
    "(LogPrice added as an alternative target, not a feature).\n"
)
print(df[["Year", "CarAge", "Odometer_km", "Km_per_year", "Is_Urban", "Price", "LogPrice"]].head())


# ---------------------------------------------------------------------------
# Step 9: Feature Scaling (X only)
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 9: Feature Scaling (X only)")
print("=" * 70)

continuous_features = ["Odometer_km", "Doors", "Accidents", "Year", "CarAge", "Km_per_year"]

scaled_df = df.copy()
scaling_stats = {}

for col in continuous_features:
    mean = scaled_df[col].mean()
    std = scaled_df[col].std(ddof=0)  # population std
    scaling_stats[col] = (mean, std)
    scaled_df[col] = (scaled_df[col] - mean) / std

df = scaled_df

print("\nScaled continuous features (mean/std used):")
for col, (mean, std) in scaling_stats.items():
    print(f"  {col}: mean={mean:.3f}, std={std:.3f}")

print("\nSample of scaled values:")
print(df[continuous_features].head())

print(
    "\nNote: Price and LogPrice are left unscaled (they are targets, not "
    "features). 0/1 dummy columns (Location_*) are also left unscaled."
)


# ---------------------------------------------------------------------------
# Step 10: Final Checks & Save
# ---------------------------------------------------------------------------
print("=" * 70)
print("STEP 10: Final Checks & Save")
print("=" * 70)

print("\nFinal info():")
df.info()

print("\nFinal missing value counts (should all be zero):")
print(df.isna().sum())

print("\nFinal describe():")
print(df.describe())

df.to_csv(OUTPUT_PATH, index=False)
print(f"\nSaved cleaned dataset to '{OUTPUT_PATH}'")


# ---------------------------------------------------------------------------
# Sanity checks (assertions)
# ---------------------------------------------------------------------------
print("=" * 70)
print("SANITY CHECKS")
print("=" * 70)

assert df["Price"].dtype == float, "Price should be float"
assert "LogPrice" in df.columns and pd.api.types.is_numeric_dtype(df["LogPrice"]), \
    "LogPrice should exist and be numeric"
assert df.isna().sum().sum() == 0, "No missing values should remain"
assert any(col.startswith("Location_") for col in df.columns), \
    "At least one Location_* dummy column should exist"

for col in continuous_features:
    col_mean = df[col].mean()
    col_std = df[col].std(ddof=0)
    assert abs(col_mean) < 1e-6, f"{col} mean should be ~0 after scaling"
    assert abs(col_std - 1) < 1e-6, f"{col} std should be ~1 after scaling"

print("\nAll sanity checks passed.")
