# Airflow Project: Orchestration of Jobs


## Description
This school project orchestrates jobs on Apache Airflow. In this repository, we have orchestrated a data collector job and a model trainer job.

Jobs Orchestrated:
- **Data Collector Job**: This job calls an API daily, collects its response, and converts it to a CSV file.
- **Model Trainer Job**: This job trains a model using the new data collected every day.

The Model Trainer Job depends on the Data Collector Job.

## How to use
To activate Airflow using Docker, follow these steps:

1. Initialize Airflow: 

    ```docker compose up airflow-init```

2. Start Airflow:

    ```docker compose up```

3. Open the webserver to see your jobs in Airflow

To clean up Docker resources, execute:

```docker compose down --volumes --remove-orphans```

