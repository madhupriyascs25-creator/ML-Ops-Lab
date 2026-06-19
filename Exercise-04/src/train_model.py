import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

df = pd.read_csv("data/delivery_data.csv")

X = df[[
    "distance_km",
    "items_count",
    "is_peak_hour",
    "traffic_level"
]]

y = df["delivery_time_min"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/delivery_time_model.pkl"
)

print("Model saved successfully")