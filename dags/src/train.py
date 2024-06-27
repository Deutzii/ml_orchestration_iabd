import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import glob
import os

def compute_regression_metrics(y_true, y_pred):
    return {
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
        "r2": r2_score(y_true, y_pred)
    }

def save_model(model, file_path):
    joblib.dump(model, file_path)

def load_latest_data(data_dir):
    list_of_files = glob.glob(os.path.join(data_dir, 'weather_data_*.csv'))
    latest_file = max(list_of_files, key=os.path.getctime)
    return pd.read_csv(latest_file)

def train_model():
    data_dir = "data"
    data = load_latest_data(data_dir).dropna()

    # Define target and features based on the latest API response
    target = "temperature_2m"
    features = [
        "relative_humidity_2m", "dew_point_2m", "apparent_temperature",
        "precipitation", "rain", "snowfall", "weather_code", "surface_pressure", "wind_speed_10m"
    ]

    X = data[features]
    y = data[target]
    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_validation)
    metrics = compute_regression_metrics(y_validation, y_pred)
    print(metrics)

    save_model(model, 'weather_model.pkl')

def retrain_model():
    # This function can be expanded if additional logic is needed during retraining
    train_model()
