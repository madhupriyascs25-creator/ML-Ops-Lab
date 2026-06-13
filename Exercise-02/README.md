# Exercise 02 - Experiment Tracking with MLflow

## Objective

Track machine learning experiments and compare model runs using MLflow.

## Tools Used

* Python
* Pandas
* Scikit-learn
* Joblib
* MLflow

## Dataset Features

### Input Features

* distance_km
* items_count
* is_peak_hour
* traffic_level

### Target Variable

* delivery_time_min

## Implementation

* Trained a Linear Regression model.
* Integrated MLflow experiment tracking.
* Logged parameters such as model type, test size, and random state.
* Logged evaluation metrics including MAE and MSE.
* Stored trained model artifacts.
* Compared multiple experiment runs through the MLflow UI.

## Results

Successfully created and tracked multiple experiment runs in MLflow. Parameters, metrics, and model artifacts were recorded for comparison.

## Learning Outcomes

* Experiment tracking.
* Model versioning.
* Artifact management.
* Performance comparison across runs.
* Reproducible MLOps workflows.
