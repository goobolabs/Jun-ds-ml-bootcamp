import pandas as pd
import numpy as np
from pathlib import Path

print("\n========= PART ZERO SETUP ============")
ROOT_DIR=Path(__file__).parent.parent.parent.parent
DATASET_DIR = f"{ROOT_DIR}/dataset"
CSV_FILE=f"{DATASET_DIR}/raw_car_dataset.csv"

print(ROOT_DIR)
print(DATASET_DIR)
print(CSV_FILE)

print(pd.__version__)
print(np.__version__)

print("\n========= PART ONE LOADING AND EDA ============")

df = pd.read_csv(CSV_FILE)
 
print(df)
print("Dataset Shape (Rows,Columns):",df.shape)
columns = df.columns.to_list()
print('Column names:',columns)
print('==== Dataset information =====')
print(df.info())
print('====== Sum of each column missing values ======\n',df.isna().sum())
categorical_columns = ['Location']
print('==== Categorical columns value counts =====\n',df[categorical_columns].value_counts())