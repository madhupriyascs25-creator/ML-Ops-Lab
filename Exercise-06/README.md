# Exercise 06 – FastAPI Model Serving

## Objective

Deploy the trained QuickFoods delivery time prediction model as a REST API using FastAPI.

## Technologies Used

* Python 3.11
* FastAPI
* Uvicorn
* Scikit-Learn
* Pandas
* Joblib

## Project Structure

Exercise-06/

* data/
* models/

  * delivery_time_model.pkl
* src/

  * api.py
* requirements.txt
* README.md

## Endpoints Implemented

### GET /health

Checks whether the API service is running and the model is loaded.

Sample Response:

{
"status": "healthy",
"model_loaded": true,
"model_path": "models/delivery_time_model.pkl"
}

### POST /predict

Predicts food delivery time based on order details.

Sample Request:

{
"distance_km": 4.2,
"items_count": 3,
"is_peak_hour": 1,
"traffic_level": 2
}

Sample Response:

{
"delivery_time_min": 41.25
}

## Tasks Performed

1. Loaded trained model using Joblib.
2. Implemented FastAPI application.
3. Created health monitoring endpoint.
4. Created prediction endpoint.
5. Validated input using Pydantic.
6. Tested API using Swagger UI.
7. Verified JSON request and response handling.

## Result

The machine learning model was successfully deployed as a FastAPI service and made accessible through REST API endpoints.
