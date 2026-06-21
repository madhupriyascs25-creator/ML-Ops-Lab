# Exercise 09 – Retraining Pipeline

## Objective

The objective of this exercise is to build a retraining pipeline that automatically evaluates whether a newly trained model performs better than the current champion model before promoting it to production.

## Tools and Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* MLflow
* Joblib

## Project Structure

Exercise-09/

* data/

  * delivery_times.csv
  * delivery_times_new.csv
* models/
* src/

  * retrain.py
* requirements.txt
* README.md
* .gitignore

## Methodology

1. Load the original training dataset.
2. Load the newly collected production dataset.
3. Combine both datasets.
4. Split the combined dataset into training and testing sets.
5. Load the current champion model from the MLflow Model Registry.
6. Evaluate the champion model on the new test dataset.
7. Train a new Gradient Boosting model on the combined dataset.
8. Evaluate the retrained model.
9. Compare champion and retrained model metrics.
10. Promote the retrained model only if it performs better.

## Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

## Results

Champion Model:

* MAE: 3.754
* RMSE: 4.758
* R²: 0.968

Retrained Model:

* MAE: 3.754
* RMSE: 4.758
* R²: 0.968

MAE Improvement:

* 0.000 minutes

## Observation

The retrained model and the current champion model achieved identical performance metrics on the evaluation dataset. Since the retrained model did not demonstrate any measurable improvement, the automated promotion logic prevented unnecessary model replacement.

## Result

The retraining pipeline was successfully implemented and executed. The champion model was evaluated against a newly trained model using combined historical and recent delivery data. As no performance improvement was observed, the existing champion model was retained.

## Conclusion

This exercise demonstrated a complete MLOps retraining workflow consisting of data ingestion, model training, evaluation, model comparison, registry integration, and automated promotion decision-making. The workflow ensures that only models with proven performance improvements are deployed to production.
