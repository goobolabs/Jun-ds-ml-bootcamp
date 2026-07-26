# utils.py — prepare raw form input for the loan API (same idea as house serve utils)
import json

import joblib
import pandas as pd

TRAIN_COLUMNS = json.load(open("models/train_columns.json"))
SCALER = joblib.load("models/loan_scaler.pkl")
SCALE_COLS = joblib.load("models/scale_cols.joblib")


def _to_binary(value) -> int:
    """Map Yes/No / 1/0 style inputs to 0/1."""
    if isinstance(value, (int, float)):
        return int(value)
    s = str(value).strip().lower()
    if s in {"yes", "y", "1", "true"}:
        return 1
    if s in {"no", "n", "0", "false"}:
        return 0
    raise ValueError(f"Cannot map binary value: {value}")


def prepare_features_from_raw(record: dict) -> pd.DataFrame:
    """
    Convert raw applicant input into the engineered, scaled feature row
    that matches training (columns == TRAIN_COLUMNS).
    """
    income = float(record["Income"])
    credit = float(record["CreditScore"])
    years = float(record["EmploymentYears"])
    loan = float(record["LoanAmount"])
    has_collateral = _to_binary(record["HasCollateral"])
    previous_defaults = _to_binary(record["PreviousDefaults"])

    debt_to_income = loan / income if income else 0.0
    income_per_year = income / (years + 1)

    row = {col: 0.0 for col in TRAIN_COLUMNS}
    values = {
        "Income": income,
        "CreditScore": credit,
        "EmploymentYears": years,
        "LoanAmount": loan,
        "HasCollateral": has_collateral,
        "PreviousDefaults": previous_defaults,
        "DebtToIncome": debt_to_income,
        "IncomePerYearEmployed": income_per_year,
    }
    for name, val in values.items():
        if name in row:
            row[name] = float(val)

    df_one = pd.DataFrame([row], columns=TRAIN_COLUMNS)

    cols_to_scale = [c for c in SCALE_COLS if c in df_one.columns]
    df_one[cols_to_scale] = SCALER.transform(df_one[cols_to_scale])

    return df_one
