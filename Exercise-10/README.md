# QuickFoods MLOps End-to-End Pipeline

## Overview

This project demonstrates a complete MLOps lifecycle for the QuickFoods delivery time prediction system.

The pipeline covers:

- Model Training
- Experiment Tracking with MLflow
- Multi-Model Comparison
- Hyperparameter Tuning
- Model Registry
- Champion-Challenger Promotion
- FastAPI Model Serving
- Prediction Logging
- Data Drift Monitoring
- Retraining Pipeline
- End-to-End Orchestration

---

## Project Structure

```
Exercise-10/
│
├── data/
│   ├── delivery_times.csv
│   └── delivery_times_new.csv
│
├── logs/
│   └── predictions.jsonl
│
├── models/
│   └── *.pkl
│
├── src/
│   ├── train.py
│   ├── train_with_mlflow.py
│   ├── train_multi_metrics_with_mlflow.py
│   ├── train_hyperparameter_tuning.py
│   ├── register_best_model.py
│   ├── promote_model.py
│   ├── api.py
│   ├── monitor.py
│   ├── retrain.py
│   └── run_full_pipeline.py
│
├── requirements.txt
├── mlflow.db
├── README.md
└── .gitignore
```

---

## Environment Setup

### Create Virtual Environment

```bash
python -m venv venv311
```

### Activate Environment

Windows:

```bash
venv311\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## MLflow Setup

This project uses SQLite as the MLflow backend.

Tracking URI:

```python
mlflow.set_tracking_uri("sqlite:///mlflow.db")
```

Start MLflow UI:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Open:

http://127.0.0.1:5000

---

## Run Individual Exercises

### Exercise 01

```bash
python src/train.py
```

### Exercise 02

```bash
python src/train_with_mlflow.py
```

### Exercise 03

```bash
python src/train_multi_metrics_with_mlflow.py
```

### Exercise 05

```bash
python src/train_hyperparameter_tuning.py
```

### Exercise 08

```bash
python src/register_best_model.py
python src/promote_model.py
```

### Exercise 09

```bash
python src/retrain.py
```

---

## FastAPI Model Serving

Start API:

```bash
uvicorn src.api:app --reload
```

Health Check:

```bash
http://127.0.0.1:8000/health
```

Prediction Endpoint:

```bash
POST /predict
```

---

## Run Complete MLOps Lifecycle

```bash
python src/run_full_pipeline.py
```

Pipeline Stages:

1. Baseline Training
2. MLflow Tracking
3. Model Comparison
4. Hyperparameter Tuning
5. Model Registration
6. Champion Promotion
7. API Serving
8. Prediction Logging
9. Monitoring
10. Retraining and Promotion

---

## Technologies Used

- Python 3.11
- Scikit-Learn
- MLflow
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Joblib

---

## Author

Madhu Priya

M.Tech CSE
BMS College of Engineering