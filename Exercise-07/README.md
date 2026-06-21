# Exercise 07 – Prediction Logging and Monitoring

## Objective

Implement prediction logging and monitoring for the deployed QuickFoods delivery time prediction API. The goal is to record every prediction request, monitor model behavior in production, detect input drift, and generate alerts when data distributions change significantly.

---

## Technologies Used

* Python 3.11
* FastAPI
* Uvicorn
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Requests

---

## Project Structure

Exercise-07/

* data/

  * delivery_times.csv

* logs/

  * predictions.jsonl (generated automatically)

* models/

  * delivery_time_model.pkl

* src/

  * api.py
  * simulate_traffic.py
  * monitor.py

* requirements.txt

* README.md

---

## Tasks Performed

### 1. Prediction Logging

Modified the FastAPI prediction service to:

* Log every prediction request
* Store input features
* Store prediction output
* Record timestamp information

Logs are stored in:

logs/predictions.jsonl

---

### 2. Traffic Simulation

Implemented a traffic simulator that generates:

* 30 normal prediction requests
* 20 drifted prediction requests

This simulates production traffic and changing user behavior.

---

### 3. Monitoring

Implemented a monitoring script to:

* Read prediction logs
* Compute prediction statistics
* Compare live data distributions with training data
* Detect feature drift
* Generate business alerts

---

## API Endpoints

### GET /health

Returns service health information.

Sample Response:

{
"status": "healthy",
"model_loaded": true,
"model_path": "models/delivery_time_model.pkl",
"predictions_logged": 50
}

---

### POST /predict

Predicts food delivery time.

Sample Request:

{
"distance_km": 4.2,
"items_count": 3,
"is_peak_hour": 1,
"traffic_level": 2
}

Sample Response:

{
"delivery_time_min": 45.23
}

---

## Monitoring Metrics

The monitoring script computes:

* Total Predictions
* Mean Prediction
* Maximum Prediction
* Minimum Prediction
* Standard Deviation

Feature monitoring includes:

* distance_km
* items_count
* is_peak_hour
* traffic_level

---

## Drift Detection

Drift is detected by comparing live feature means against training dataset means.

Alert thresholds:

* Distance mean shift > 3 km
* Items mean shift > 2
* Average prediction > 60 minutes

---

## Sample Output

Prediction Statistics:

* Total Predictions: 50
* Mean Prediction: 85.0
* Maximum Prediction: 177.78
* Minimum Prediction: 25.79

Drift Alerts:

* Distance drift detected
* Items count drift detected
* Prediction threshold exceeded

---

## Observation

The deployed FastAPI service successfully logged all prediction requests and responses. Simulated production traffic generated both normal and drifted requests. The monitoring system analyzed logged predictions and detected significant drift in distance_km and items_count compared with training data. Alert thresholds were triggered when feature distributions shifted beyond acceptable limits and average prediction values increased substantially.

---

## Result

Prediction logging and monitoring were successfully implemented for the QuickFoods delivery time prediction API. The monitoring system identified data drift and generated alerts based on predefined thresholds. This experiment demonstrated how monitoring provides visibility into production model behavior and helps determine when investigation or retraining may be required.
