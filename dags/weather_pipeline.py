from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import os
import sys
import requests
import pandas as pd

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.train import train_model

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@daily',
}

# Define the DAG
dag = DAG(
    'weather_pipeline',
    catchup=False,
    default_args=default_args,
)

def fetch_weather_data():
    url = 'https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&hourly=temperature_2m'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error fetching data from Open Meteo API")
    data = response.json()
    hourly_data = data['hourly']
    temperature_data = hourly_data['temperature_2m']
    
    # Assuming we store the data as a CSV for simplicity
    df = pd.DataFrame({
        'time': hourly_data['time'],
        'temperature_2m': temperature_data,
    })
    
    os.makedirs('/opt/airflow/data', exist_ok=True)
    df.to_csv('/opt/airflow/data/weather_data.csv', index=False)

def train_model_task():
    train_model()

# Tasks
download_task = PythonOperator(
    task_id='download_weather_data',
    python_callable=fetch_weather_data,
    dag=dag,
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model_task,
    dag=dag,
)

# Task dependencies
download_task >> train_task
