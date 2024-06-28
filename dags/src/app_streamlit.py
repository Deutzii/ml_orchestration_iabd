import streamlit as st
import requests
print(st.__version__)

st.title("Weather Prediction using FastAPI")

st.sidebar.header("User Input Parameters")

def user_input_features():
    humidity = st.sidebar.slider("Humidity", 0.0, 100.0, 50.0)
    pressure = st.sidebar.slider("Pressure", 950.0, 1050.0, 1013.0)
    wind_speed = st.sidebar.slider("Wind Speed", 0.0, 100.0, 5.0)
    latitude = st.sidebar.number_input("Latitude", value=52.52)
    longitude = st.sidebar.number_input("Longitude", value=13.41)
    data = {
        "humidity": humidity,
        "pressure": pressure,
        "wind_speed": wind_speed,
        "latitude": latitude,
        "longitude": longitude
    }
    return data

input_data = user_input_features()

if st.button("Predict"):
    try:
        url = "http://api-container:8000/predict/"  # Assurez-vous que c'est la bonne URL de votre API
        response = requests.get(url, params=input_data)
        response.raise_for_status()  # Assure qu'une erreur HTTP est levée pour les mauvaises réponses
        prediction = response.json()
        st.write(f"Prediction: {prediction['prediction']}")
    except requests.exceptions.RequestException as e:
        st.write(f"Error in fetching prediction: {e}")