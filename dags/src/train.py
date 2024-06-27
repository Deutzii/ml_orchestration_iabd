import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

def compute_regression_metrics(y_true, y_pred):
    return {
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
        "r2": r2_score(y_true, y_pred)
    }

def save_model(model, file_path):
    joblib.dump(model, file_path)

def train_model():
    data = pd.read_csv("data/weather_data.csv").dropna()
    target = ["temperature"]  # Change to your target variable
    features = ["humidity", "pressure", "wind_speed", "temperature"]  # Include new feature

    x = data[features]
    y = data[target]
    x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.3)
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_validation)
    metrics = compute_regression_metrics(y_validation, y_pred)
    print(metrics)
    save_model(model, 'weather_model.pkl')


