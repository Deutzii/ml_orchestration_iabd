# Use official Python image from the Docker Hub
FROM apache/airflow:2.9.2

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Define environment variable
ENV MODEL_PATH=/app/weather_model.pkl
