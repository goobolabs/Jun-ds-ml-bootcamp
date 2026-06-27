# Reflection: Car Price Data Preprocessing

## Load & Inspect
The raw dataset had 145 rows and 6 columns. Right away I noticed `Price` was
stored as text (mixing plain numbers and `"$1,500"`-style strings),
`Odometer_km` and `Doors` had missing values, `Location` had typos and a
`"??"` placeholder, and there were clearly a few duplicate rows and extreme
outliers in `Price` and `Odometer_km`.

## Cleaning Price
I stripped the `$` and `,` characters and converted the column to `float`.
After cleaning, the distribution was heavily right-skewed (skewness well
above 1), which makes sense: most cars cluster around a similar price band,
but a handful of very high values pull the distribution to the right. This
is also why a log-transformed target (`LogPrice`) was useful later.

## Fixing Category Errors Before Imputation
I normalized `Location` text and mapped the typo `"Subrb"` to `"Suburb"`,
then converted the `"??"` placeholder to a true missing value (`NaN`). This
had to happen *before* imputation — otherwise `"??"` and `"Subrb"` would
have been treated as legitimate categories and would have distorted the
mode and the one-hot encoding later.

## Imputing Missing Values
- **Odometer_km → median**: it's a continuous numeric column with outliers
  (some very high mileage values), so the median is more robust than the
  mean, which outliers would pull upward.
- **Doors → mode**: `Doors` only takes a few repeated values (2, 3, 4, 5),
  so it behaves more like a categorical feature — the most frequent value
  is the most sensible fill.
- **Location → mode**: a categorical column has no meaningful mean/median,
  so the mode (most common location) is the only reasonable choice.

## Removing Duplicates
I dropped exact duplicate rows. This matters because duplicates would have
given certain car records extra weight in any later statistics or model
training, even though they don't represent new information.

## Outliers (IQR Capping)
I computed the IQR for `Price` and `Odometer_km` and capped values outside
`[Q1 - 1.5*IQR, Q3 + 1.5*IQR]` rather than removing the rows outright.
Capping preserves the row count and the information in the other columns
of that record, while preventing a few extreme values (like the $135,000
and $120,000 entries) from dominating the scale of the feature.

## One-Hot Encoding
`Location` was one-hot encoded into `Location_City`, `Location_Rural`, and
`Location_Suburb`. One-hot encoding avoids implying a false numeric
ordering between categories (e.g. City vs Suburb vs Rural aren't actually
on a numeric scale).

## Feature Engineering
- **CarAge** = current year − `Year`: more directly useful for a price
  model than a raw year value.
- **Km_per_year** = `Odometer_km` / `CarAge`, with `CarAge` of 0 replaced
  by 1 to avoid dividing by zero for brand-new cars. This captures usage
  intensity rather than just raw mileage.
- **Is_Urban** = 1 if the car is listed in the City location, 0 otherwise.
  This is a simplified urban/non-urban flag that could be useful on its own
  in addition to the full one-hot location columns.
- **LogPrice** = `log(Price + 1)`, added as an *alternative target*, not a
  feature, to address the right-skew in `Price` noted earlier. The `+ 1`
  avoids issues with `log(0)`.

## Feature Scaling
I standardized the continuous numeric features (`Odometer_km`, `Doors`,
`Accidents`, `Year`, `CarAge`, `Km_per_year`) to mean 0 and standard
deviation 1, using the population standard deviation. I deliberately did
**not** scale `Price` or `LogPrice`, since they are targets, not input
features, and scaling them would make the regression output harder to
interpret. I also left the one-hot `Location_*` dummy columns unscaled,
since they are already on a 0/1 scale and standardizing them would make
them harder to interpret as flags.

## Final Checks
After all steps, there are no missing values remaining, `Price` is a
float, `LogPrice` exists and is numeric, at least one `Location_*` dummy
column exists, and the scaled continuous columns have mean ≈ 0 and
population standard deviation ≈ 1 — all confirmed via assertions in the
script.
