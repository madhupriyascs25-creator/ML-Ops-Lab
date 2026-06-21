# Exercise 08 – Model Versioning and Promotion

## Objective

Implement model versioning and promotion using the MLflow Model Registry. The objective is to manage multiple model versions, assign aliases for production deployment, and update the FastAPI service to dynamically load models from the registry instead of a local model file.

---

## Technologies Used

* Python 3.11
* MLflow
* Scikit-Learn
* Pandas
* NumPy
* FastAPI
* Uvicorn
* Joblib

---

## Project Structure

Exercise-08/

* data/

  * delivery_times.csv

* models/

* src/

  * train_v2.py
  * promote_model.py
  * api.py

* mlflow.db

* requirements.txt

* README.md

* .gitignore

---

## Problem Statement

QuickFoods already has a deployed delivery-time prediction service. As new models are trained, the organization requires a controlled mechanism to:

* Manage multiple model versions
* Promote better-performing models to production
* Roll back to older versions if required
* Serve models dynamically without changing application code

MLflow Model Registry is used to solve this problem.

---

## Tasks Performed

### 1. Registered Multiple Model Versions

A new RandomForest model was trained using a different train-test split and hyperparameter configuration.

Model Details:

* Algorithm: RandomForestRegressor
* n_estimators = 200
* max_depth = 8
* min_samples_split = 3
* random_state = 99

The trained model was logged to MLflow and registered under:

quickfoods-delivery-predictor

Result:

* Version 1 created
* Version 2 created

---

### 2. Model Promotion Workflow

Implemented a promotion workflow using MLflow aliases.

Aliases used:

* champion → currently serving production traffic
* challenger → candidate model under evaluation

Workflow:

1. Assign Version 1 as champion
2. Assign Version 2 as challenger
3. Evaluate challenger performance
4. Promote Version 2 to champion
5. Remove challenger alias

This enables safe model deployment and rollback.

---

### 3. Registry-Based Model Loading

Modified the FastAPI service to load models directly from the MLflow Registry.

Model URI:

models:/quickfoods-delivery-predictor@champion

Benefits:

* No dependency on local .pkl files
* Centralized model management
* Seamless promotion and rollback
* Production-ready deployment workflow

---

## Health Endpoint Verification

Endpoint:

GET /health

Sample Response:

{
"status": "healthy",
"model": "quickfoods-delivery-predictor",
"alias": "champion",
"model_uri": "models:/quickfoods-delivery-predictor@champion"
}

This confirms that the API is serving the model through the MLflow Registry.

---

## Prediction Endpoint

Endpoint:

POST /predict

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

The exact prediction value depends on the active champion model.

---

## Rollback Strategy

If the promoted model performs poorly in production, rollback can be performed by moving the champion alias back to a previous version.

Example:

client.set_registered_model_alias(
"quickfoods-delivery-predictor",
"champion",
"1"
)

After restarting the API, Version 1 becomes active again.

No code changes are required.

---

## Advantages of Model Registry

* Centralized model management
* Version control for machine learning models
* Safe promotion workflow
* Easy rollback mechanism
* Improved reproducibility
* Production-grade deployment process

---

## Observation

Multiple versions of the QuickFoods delivery-time prediction model were successfully registered in the MLflow Model Registry. Aliases were used to manage model lifecycle and promotion workflows. The FastAPI application was modified to dynamically load the champion model from the registry. Health endpoint verification confirmed that the application was serving the registered model through the alias-based deployment mechanism.

---

## Result

Model versioning and promotion were successfully implemented using the MLflow Model Registry. Multiple model versions were registered, managed through champion and challenger aliases, and served through a FastAPI application. The implementation demonstrated safe model promotion, rollback capability, and production-ready model lifecycle management.
