# Use official Python image from the Docker Hub
FROM apache/airflow:2.9.2

# Use official Airflow image from the Docker Hub
FROM apache/airflow:2.9.2

# Set the working directory
WORKDIR /opt/app

# Copy the current directory contents into the container at /opt/airflow
COPY . /opt/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Define environment variable
ENV MODEL_PATH=/opt/app/weather_model.pkl

