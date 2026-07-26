# app.py — Goobo Classifier API (same shape as house deployment/app.py)
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from utils import prepare_features_from_raw

app = Flask(__name__)
CORS(app)

MODELS = {
    "lr": joblib.load("models/lr_model.joblib"),
    "rf": joblib.load("models/rf_model.joblib"),
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Goobo Classifier API",
        "endpoints": {
            "POST /predict?model=lr|rf": {
                "expects_json": {
                    "Income": "number",
                    "CreditScore": "number",
                    "EmploymentYears": "number",
                    "LoanAmount": "number",
                    "HasCollateral": "Yes|No or 1|0",
                    "PreviousDefaults": "Yes|No or 1|0",
                }
            }
        }
    })


@app.route("/predict", methods=["POST"])
def predict():
    choice = (request.args.get("model") or "rf").lower()
    if choice not in MODELS:
        return jsonify({"error": "Unknown model. Use model=lr or model=rf"}), 400
    model = MODELS[choice]

    data = request.get_json(silent=True) or {}
    required = [
        "Income",
        "CreditScore",
        "EmploymentYears",
        "LoanAmount",
        "HasCollateral",
        "PreviousDefaults",
    ]
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    try:
        x_new = prepare_features_from_raw(data)
        pred = int(model.predict(x_new)[0])
        label = "Approved" if pred == 1 else "Rejected"
        payload = {
            "model": "logistic_regression" if choice == "lr" else "random_forest",
            "input": {
                "Income": float(data["Income"]),
                "CreditScore": float(data["CreditScore"]),
                "EmploymentYears": float(data["EmploymentYears"]),
                "LoanAmount": float(data["LoanAmount"]),
                "HasCollateral": data["HasCollateral"],
                "PreviousDefaults": data["PreviousDefaults"],
            },
            "prediction": pred,
            "label": label,
        }
        if hasattr(model, "predict_proba"):
            # probs[0] = P(Rejected=0), probs[1] = P(Approved=1)
            # confidence = probability of the label we predicted (pred is 0 or 1)
            probs = model.predict_proba(x_new)[0]
            payload["confidence"] = round(float(probs[pred]), 3)
        return jsonify(payload)
    except Exception as e:
        return jsonify({"error": f"Failed to prepare/predict: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
