# Exercise 05 - Hyperparameter Tuning with MLflow

## Objective

Perform hyperparameter tuning using MLflow nested runs and register the best-performing model.

## Technologies Used

* Python
* Scikit-Learn
* MLflow
* Pandas
* NumPy
* Joblib

## Tasks Performed

1. Created hyperparameter tuning workflow.
2. Performed Grid Search on RandomForestRegressor.
3. Performed Random Search on GradientBoostingRegressor.
4. Logged all runs as MLflow nested runs.
5. Compared metrics including MAE, RMSE, MSE, CV_MAE, and R².
6. Identified the best-performing model.
7. Registered the best model in the MLflow Model Registry.

## Best Model

Model: GradientBoostingRegressor

Parameters:

* learning_rate = 0.1
* max_depth = 3
* n_estimators = 200

MAE: 5.751 minutes

Registered Model:

* quickfoods-delivery-predictor
* Version 1

## Result

Hyperparameter tuning and model registration were successfully completed using MLflow.
