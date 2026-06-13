# Exercise 01 - Reproducible ML Project Setup

## Objective

Build a reproducible machine learning project that trains a baseline regression model for predicting food delivery time.

## Project Structure

```text
Exercise-01/
├── data/
│   └── delivery_times.csv
├── models/
│   └── delivery_time_model.pkl
├── src/
│   ├── __init__.py
│   └── train.py
├── view_pkl.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Features

* distance_km
* items_count
* is_peak_hour
* traffic_level

## Target

* delivery_time_min

## Steps Performed

1. Created a virtual environment.
2. Installed required dependencies.
3. Loaded dataset using pandas.
4. Trained a Linear Regression model.
5. Evaluated the model using MAE and MSE.
6. Saved the trained model as a `.pkl` artifact.
7. Verified the model artifact using `view_pkl.py`.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Git

## Output

The trained model is stored in:

```text
models/delivery_time_model.pkl
```

This artifact can be loaded later for prediction without retraining the model.
