# Exercise 03 - Multi-Metric MLflow Tracking and Model Selection

## Objective

Train multiple machine learning models, track experiments using MLflow, compare performance metrics, and select the best model based on MAE.

## Models Evaluated

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

## Metrics Logged

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)
* R² Score
* Model Size (KB)
* Average Inference Latency (ms)

## Results

| Model            | MAE   | RMSE   | R²    |
| ---------------- | ----- | ------ | ----- |
| LinearRegression | 5.724 | 6.103  | 0.920 |
| RandomForest     | 8.635 | 10.202 | 0.776 |
| GradientBoosting | 5.751 | 6.980  | 0.895 |

## Best Model

Linear Regression was selected as the best model because it achieved:

* Lowest MAE
* Lowest RMSE
* Highest R²
* Smallest model size
* Lowest inference latency

## Learning Outcomes

* Tracked multiple ML experiments using MLflow
* Logged parameters, metrics, and model artifacts
* Compared model performance using multiple evaluation metrics
* Selected the best model using business-friendly metrics
* Understood the trade-off between accuracy, latency, and model size
