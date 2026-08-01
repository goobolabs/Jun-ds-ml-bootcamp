# 🧠 WellMind AI

A complete Machine Learning capstone for **lifestyle wellness classification** — predict **Healthy**, **Average**, or **Poor** from sleep and lifestyle data, with **FastAPI**, **React**, and **Flutter**.

## 📌 Overview

WellMind AI analyzes sleep, stress, activity, and related habits, then returns a **lifestyle category**, **wellness score**, and **personalized recommendations** via a REST API.


## ✨ Features

- 3-class lifestyle prediction (Healthy / Average / Poor)
- 5 ML models compared on the same train/test split
- XGBoost production model + encoders/scaler
- FastAPI backend (`POST /predict`, Swagger docs)
- React dashboard (wellness check, scores, ML comparison)
- Flutter mobile app (optional)
- K-Means / clustering analysis (notebook 3)
- 3 sanity-check scripts for the API

## 📂 Dataset

**Sleep Health Data** (Kaggle) by Imaginative_Coder  
https://www.kaggle.com/datasets/imaginativecoder/sleep-health-data-sampled

| | |
|---|---|
| **File** | `notebook/data/raw/Sleep_Data_Sampled.csv` |
| **Rows** | 15,000 |
| **Columns** | 13 |
| **Target** | Lifestyle Category (engineered from wellness score) |

**Model inputs (10):** Age, Gender, Occupation, Sleep Duration, Quality of Sleep, Physical Activity Level, Stress Level, BMI Category, Daily Steps, Sleep Disorder.

## 🏆 Best Model

**XGBoost** (selected by highest test **Macro F1**)

| Metric | Score |
|--------|-------|
| Test accuracy | **0.839** |
| Macro F1 | **0.793** |

Full comparison: `notebook/outputs/model_comparison.csv` (from `2_train_models.ipynb`).

## 🛠 Tech Stack

- Python · Pandas · Scikit-learn · XGBoost
- Jupyter (preprocessing, training, clustering, inference)
- FastAPI · Uvicorn
- React · Vite · Tailwind CSS
- Flutter (mobile)

## 📁 Structure

```text
WellMind-AI/
├── api/                    # FastAPI (app.py, preprocess, multi-model predict)
├── notebook/
│   ├── 1_preprocessing.ipynb
│   ├── 2_train_models.ipynb
│   ├── 3_clustering.ipynb
│   ├── 4_inference.ipynb
│   ├── inference.py        # Production predict logic
│   ├── data/raw/           # Sleep_Data_Sampled.csv
│   ├── data/               # train/test processed CSVs
│   ├── outputs/            # model_comparison.csv
│   └── artifacts/          # best_model.pkl (run notebook 2 locally)
├── scripts/
│   └── run_sanity_checks.py
├── frontend/               # React web app
├── mobile/                 # Flutter app
├── project-proposal.md
├── project_paper.md
├── requirements.txt
└── README.md
```

## ⚙ Installation

```bash
git clone https://github.com/maryan-dev/WellMind-https://github.com/maryan-dev/WellMind-AI-prediction-AI.git
cd WellMind-AI
py -3 -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
py -3 -m pip install -r requirements.txt
```

**Train artifacts (required for live ML predict):** run notebooks in order `1_preprocessing` → `2_train_models` → (optional) `3_clustering`, `4_inference`.  
Without `notebook/artifacts/best_model.pkl`, `POST /predict` returns **503**.

## 🚀 Backend

```bash
py -3 -m uvicorn api.app:app --reload --host 127.0.0.1 --port 8000
```

- Swagger: http://127.0.0.1:8000/docs  
- Health: http://127.0.0.1:8000/health  

Production inference: **`notebook/inference.py`** (aligned with **`4_inference.ipynb`**).

## 🌐 Frontend (Web)

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 (API on port **8000**).

**Vercel (frontend only):** Settings → **Root Directory = `frontend`** · Framework **Vite** · set `VITE_API_URL` to your public API · no Python (avoids 500 MB errors). See `frontend/VERCEL.md` if deploy fails.

## 📱 Mobile (Flutter)

```bash
cd mobile
flutter pub get
flutter run
```

Android emulator API: `http://10.0.2.2:8000`

## 🧪 Testing

```bash
py -3 scripts/run_sanity_checks.py
```

(With API running — 3 sample payloads to `/predict`.)

## 📄 License

[MIT License](LICENSE) — educational / capstone use. Respect the [Kaggle dataset](https://www.kaggle.com/datasets/imaginativecoder/sleep-health-data-sampled) license.

## 🙏 Acknowledgements

I would like to sincerely thank **Goobo Labs** for providing the Data Science and Machine Learning (DS-ML) Bootcamp. The knowledge, guidance .

GitHub: https://github.com/goobolabs
## 👩‍💻 Author

**Maryan Mohamed Adam**
