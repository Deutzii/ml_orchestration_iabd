from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import joblib
import redis
import requests
import json
import os
import streamlit as st

app = FastAPI()

# Redis setup
r = redis.Redis(host='redis', port=6379, db=0)

# Load model function
def load_model(file_path):
    print(f"Loading model from {file_path}")
    model = joblib.load(file_path)
    print("Model loaded successfully")
    return model

# Define input data model
class InputData(BaseModel):
    humidity: float
    pressure: float
    wind_speed: float

# Fetch data from Open Meteo API
def fetch_weather_data(latitude: float, longitude: float):
    print(f"Fetching weather data for latitude {latitude} and longitude {longitude}")
    url = f"https://api.open-meteo.com/v1/meteofrance?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&past_days=7"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from Open Meteo API")
    data = response.json()
    temperature = data['hourly']['temperature_2m'][-1]  # Use the latest data point
    print(f"Latest temperature data fetched: {temperature}°C")
    return temperature

# Function to fetch and save weather data
def fetch_and_save_weather_data():
    try:
        st.write("Fetching weather data from Open Meteo API...")
        latitude = 52.52
        longitude = 13.41
        url = f'https://api.open-meteo.com/v1/meteofrance?latitude={latitude}&longitude={longitude}&hourly='\
              'temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation,rain,snowfall,'\
              'weather_code,surface_pressure,wind_speed_10m&past_days=7'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        hourly_data = data['hourly']

        st.write("Fetched data successfully, preparing DataFrame...")

        df = pd.DataFrame(hourly_data)
        
        current_date = datetime.now().strftime("%Y%m%d")
        output_dir = './data'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f'weather_data-{current_date}.csv')
        df.to_csv(output_file, index=False)
        st.write(f"Data saved to {output_file}")
    except Exception as e:
        st.error(f"An error occurred: {e}")


@app.get("/predict/")
async def predict(humidity: float, pressure: float, wind_speed: float, latitude: float, longitude: float):
    print(f"Received request with params - Humidity: {humidity}, Pressure: {pressure}, Wind Speed: {wind_speed}, Latitude: {latitude}, Longitude: {longitude}")
    
    # Check cache first
    cache_key = f"{humidity}-{pressure}-{wind_speed}-{latitude}-{longitude}"
    if r.exists(cache_key):
        print("Cache hit, returning cached prediction")
        prediction = r.get(cache_key)
        return json.loads(prediction)
    
    print("Cache miss, fetching additional weather data and making prediction")
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
    print("Input data prepared for prediction:", input_dict)
    
    # Load model and make prediction
    model = load_model(os.path.join(os.path.dirname(__file__), 'weather_model.pkl'))
    prediction = model.predict(input_df)
    prediction = {"prediction": prediction[0][0]}
    print("Prediction made:", prediction)
    
    # Cache the prediction
    r.set(cache_key, json.dumps(prediction))
    print("Prediction cached")
    return prediction

# Test functions
def test_fetch_weather_data():
    print("---------------------------------------")
    print("Testing fetch_weather_data function...")
    temperature = fetch_weather_data(52.52, 13.41)
    print(f"Fetched temperature: {temperature}°C")

def test_predict():
    print("---------------------------------------")
    print("Testing predict function...")
    result = predict(65.0, 1013.0, 5.0, 52.52, 13.41)
    print("Prediction result:", result)

if __name__ == "__main__":
    test_fetch_weather_data()
    #fetch_and_save_weather_data()
    #test_predict()
    # Streamlit app
    st.title("Weather Data Fetcher")
    st.write("Click the button below to fetch and save weather data.")
    if st.button("Fetch Weather Data"):
        fetch_and_save_weather_data()
        