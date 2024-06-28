from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import os
import sys
import requests
import pandas as pd

# Add the path to the system's import paths
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from train import retrain_model  # Ensure that the train module exists and is correctly imported

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=45),
}

# Define the DAG
dag = DAG(
    'weather_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval='@daily',
    catchup=False,
)


def fetch_weather_data():
    print("Fetching weather data from Open Meteo API...")
    latitude = 52.52
    longitude = 13.41
    url = f'https://api.open-meteo.com/v1/meteofrance?latitude={latitude}&longitude={longitude}&hourly=' \
        'temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation,' \
        'rain,snowfall,weather_code,surface_pressure,wind_speed_10m&past_days=7'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        raise Exception("Error fetching data from Open Meteo API")
    data = response.json()
    hourly_data = data['hourly']

    print("Fetched data successfully, preparing DataFrame...")

    df = pd.DataFrame(hourly_data)

    current_date = datetime.now().strftime("%Y%m%d")
    output_dir = './data'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'weather_data_{current_date}.csv')
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")


def retrain_model_task():
    print("Retraining model with new data...")
    retrain_model()
    print("Model retraining completed.")


# Tasks
download_task = PythonOperator(
    task_id='download_weather_data',
    python_callable=fetch_weather_data,
    dag=dag,
)

train_task = PythonOperator(
    task_id='retrain_model',
    python_callable=retrain_model_task,
    dag=dag,
)

# Task dependencies
download_task >> train_task
