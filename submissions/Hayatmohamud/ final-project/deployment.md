# 🛡️ JobShield AI | Fake Job Posting Detection System

**Name:** Hayat Mohamud Hassan

## Short Description

JobShield AI is an end-to-end Machine Learning application designed to detect fraudulent job advertisements and help protect job seekers from online scams.

The system analyzes job-posting text such as the job title, company profile, job description, requirements, and benefits. It then predicts whether the job posting is:

- ✅ Real Job
- ❌ Fake Job

The project uses Natural Language Processing techniques to convert text into numerical features using `TF-IDF Vectorization`.

A `Linear Support Vector Machine (Linear SVM)` classifier is used because it performs well with high-dimensional and sparse text data, making it suitable for fake-job text classification.

The trained model and TF-IDF vectorizer are deployed through a `FastAPI` REST API. The user interface is built with `Next.js` and deployed online, allowing users to analyze job advertisements in real time.

## Problem Being Solved

Fake job postings are becoming more common on online recruitment platforms.

These fraudulent advertisements may ask job seekers for registration or training fees, bank account information, passport copies, personal documents, or other sensitive information.

This can lead to financial loss, identity theft, loss of personal information, and wasted time.

JobShield AI provides an automated first screening tool that helps users identify suspicious job advertisements before submitting personal information or making payments.

## Machine Learning Model

### Model Used

`Linear Support Vector Machine (Linear SVM)`

### Why Linear SVM Was Selected

- Performs well in text classification tasks
- Works efficiently with TF-IDF features
- Handles high-dimensional sparse data
- Provides fast predictions
- Generalizes well to unseen job postings
- Requires less memory than many tree-based models for text data

## Machine Learning Pipeline

```text
Job Posting Dataset
        ↓
Data Cleaning
        ↓
Text Preprocessing
        ↓
Combine Text Features
        ↓
TF-IDF Vectorization
        ↓
Linear SVM Training
        ↓
Save Model and Vectorizer
        ↓
FastAPI Prediction Endpoint
        ↓
Next.js User Interface
```

## Main Features

- Fake and real job classification
- Job-post text analysis
- TF-IDF feature extraction
- Linear SVM prediction
- FastAPI REST API
- Responsive Next.js frontend
- Real-time prediction result
- Decision score display
- Cloud deployment

## Technologies Used

### Machine Learning and Backend

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Linear SVM
- FastAPI
- Uvicorn

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Deployment and Development Tools

- Git
- GitHub
- Render
- Vercel

## System Architecture

```text
User
  ↓
Next.js Frontend
  ↓
FastAPI Backend
  ↓
TF-IDF Vectorizer
  ↓
Linear SVM Model
  ↓
Real or Fake Prediction
  ↓
Result Displayed to User
```

## Project Structure

```text
jobshield-ai_ML/
│
├── api/
│   └── app.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── package.json
│
├── models/
│   ├── linear_svm_balanced.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

## Live Application

Frontend: https://jobshield-ai-ml-coral.vercel.app/

Backend API: https://jobshield-ai-ml.onrender.com/

## GitHub Repository

https://github.com/Hayatmohamud/jobshield-ai_ML

## Future Improvements

- BERT and Transformer models
- Explainable AI
- User authentication
- Prediction history
- Admin dashboard
- Mobile application
- Multi-language support
- Improved confidence scoring
- Larger and more diverse training data

## Acknowledgement

I would like to express my sincere appreciation to **https://github.com/goobolabs**, the instructors, mentors, and everyone who supported me throughout this Machine Learning learning journey.

Their guidance and encouragement helped me complete this end-to-end Machine Learning capstone project.

## Author

**Hayat Mohamud**

- GitHub: https://github.com/Hayatmohamud
- Email: hayadmohamudhassan@gmail.com

---

⭐ If you find this project useful, please consider giving the repository a star.