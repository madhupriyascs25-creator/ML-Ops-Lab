# Exercise 04 – Docker for Model Packaging

## Objective

To containerize a Machine Learning model application using Docker, build a Docker image, execute the container with test inputs, and verify prediction outputs.

---

## Problem Statement

QuickFoods has developed a delivery time prediction model. The data science team can train models locally, but the organization requires a portable and consistent deployment package that can run across different environments such as local machines, cloud servers, and on-premise infrastructure.

The objective of this experiment is to package the trained model and prediction application into a Docker container and demonstrate its execution.

---

## Project Structure

```text
Exercise-04/
│
├── data/
│   └── delivery_data.csv
│
├── models/
│   └── delivery_time_model.pkl
│
├── src/
│   ├── train_model.py
│   └── predict_cli.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3.11
* Docker Desktop
* Scikit-Learn
* Pandas
* NumPy
* Joblib

---

## Steps Performed

### Step 1: Dataset Preparation

A sample delivery dataset containing the following features was created:

* distance_km
* items_count
* is_peak_hour
* traffic_level
* delivery_time_min

---

### Step 2: Model Training

A machine learning regression model was trained using Scikit-Learn and saved as:

```text
models/delivery_time_model.pkl
```

using Joblib.

---

### Step 3: CLI Prediction Application

A command-line application (`predict_cli.py`) was developed to:

* Load the trained model
* Accept user inputs
* Generate delivery time predictions
* Display results in JSON format

Example:

```bash
python src/predict_cli.py \
--distance_km 4.2 \
--items_count 3 \
--is_peak_hour 1 \
--traffic_level 2
```

---

### Step 4: Dockerfile Creation

A Dockerfile was created using the Python 3.11 Slim image.

The Docker image includes:

* Application source code
* Model artifact
* Required dependencies

---

### Step 5: Docker Image Build

The Docker image was built using:

```bash
docker build -t quickfoods-delivery-model:0.1 .
```

---

### Step 6: Container Execution

Test Case 1:

```bash
docker run --rm quickfoods-delivery-model:0.1 \
--distance_km 4.2 \
--items_count 3 \
--is_peak_hour 1 \
--traffic_level 2
```

Output:

```json
{
  "prediction": {
    "delivery_time_min": 41.25
  }
}
```

Test Case 2:

```bash
docker run --rm quickfoods-delivery-model:0.1 \
--distance_km 1.0 \
--items_count 1 \
--is_peak_hour 0 \
--traffic_level 1
```

Output:

```json
{
  "prediction": {
    "delivery_time_min": 14.26
  }
}
```

---

## Docker Commands Used

Build Image:

```bash
docker build -t quickfoods-delivery-model:0.1 .
```

Run Container:

```bash
docker run --rm quickfoods-delivery-model:0.1 \
--distance_km 4.2 \
--items_count 3 \
--is_peak_hour 1 \
--traffic_level 2
```

List Containers:

```bash
docker ps
docker ps -a
```

List Images:

```bash
docker images
```

Remove Image:

```bash
docker rmi quickfoods-delivery-model:0.1
```

---

## Observation

* Docker successfully packaged the machine learning model and application.
* The model artifact was loaded correctly inside the container.
* Prediction results generated inside the container matched expected outputs.
* Docker image versioning was demonstrated using image tags.
* Container lifecycle operations were successfully performed.

---

## Result

The delivery time prediction model was successfully containerized using Docker. The Docker image was built, tagged, executed with test inputs, and produced valid prediction outputs. The experiment demonstrated model portability and reproducible deployment using containerization.
