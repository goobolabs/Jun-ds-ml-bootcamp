# 1. Importting Libraries

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Testing if its ok is must show like this (3.0.3)
# print(pd.__version__)

#3. Loading the data
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "Climate_Clean_Dataset.csv")

df = pd.read_csv(CSV_PATH)
# print(df.head()) 

# 4. Slipting the dataset

X = df.drop(columns=[
    "RainfallAmount_mm",
    "Unnamed: 0",
    "RecordID",
    "isItRainy",
    "isItDrought",
    "ClimateCondition_Rainy",
    "ClimateCondition_Drought"
])
y = df["RainfallAmount_mm"]

# 4. Training the model, Phase 1
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42) 

# 4. Training the model, Phase 2
lr = LinearRegression()
lr.fit(X_train, y_train)

# 5. Making the prediction

lr_pred = lr.predict(X_test)
# print("Printing All Linear Regression Pridictions")
# print(lr_prediction) 

rf = RandomForestRegressor(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# print("Printing All Random Forest Regression Pridictions")
# print(rf_prediction) 

# 6. Making Helper Fuction Metrics

def print_metrics(name, y_true, y_pred) :
    
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    print(f"\n {name} Performance")
    print(f"R² : {r2:.3f}")
    print(f"mae : {mae:.0f}")
    print(f"mse : {mse:.0f}")
    print(f"rmse : {rmse:.0f}")
 
#  Showing the result

# print_metrics("Linear Regression", y_test, lr_pred)
# print_metrics("Random Forest", y_test, rf_pred)

i = 3
x_one_df = X_test.iloc[[i]]   # 1-row DataFrame (keeps feature names)
y_true   = y_test.iloc[i]     # scalar

p_lr_one = float(lr.predict(x_one_df)[0])
p_rf_one = float(rf.predict(x_one_df)[0])

print("\n Single Row Prediction")
print(f"Actual Rainfall is : {y_true:,.0f} MM")
print(f"Linear Rgression Predicts : {p_lr_one:,.0f} MM")
print(f"Random Forest Predicts : {p_rf_one:,.0f} MM")