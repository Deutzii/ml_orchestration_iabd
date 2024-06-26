from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import redis
import requests
import json


app = FastAPI()

# Redis setup
r = redis.Redis(host='localhost', port=6379, db=0)

# Load model function
def load_model(file_path):
    return joblib.load(file_path)

# Define input data model
class InputData(BaseModel):
    humidity: float
    pressure: float
    wind_speed: float

# Fetch data from Open Meteo API
def fetch_weather_data(latitude: float, longitude: float):
    url = f"https://api.open-meteo.com/v1/meteofrance?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from Open Meteo API")
    data = response.json()
    # Assuming we only need the latest data point
    temperature = data['hourly']['temperature_2m'][-1]
    return temperature

@app.get("/predict/")
async def predict(humidity: float, pressure: float, wind_speed: float, latitude: float, longitude: float):
    # Check cache first
    cache_key = f"{humidity}-{pressure}-{wind_speed}-{latitude}-{longitude}"
    if r.exists(cache_key):
        prediction = r.get(cache_key)
        return json.loads(prediction)
    
    # Fetch additional weather data
    temperature = fetch_weather_data(latitude, longitude)
    
    # Prepare input for model
    input_dict = {
        "humidity": humidity,
        "pressure": pressure,
        "wind_speed": wind_speed,
        "temperature": temperature  # Add temperature from Open Meteo API
    }
    input_df = pd.DataFrame([input_dict])
    
    # Load model and make prediction
    model = load_model('weather_model.pkl')
    prediction = model.predict(input_df)
    prediction = {"prediction": prediction[0][0]}
    
    # Cache the prediction
    r.set(cache_key, json.dumps(prediction))
    return prediction
