# ml_orchestration_iabd


# Weather Prediction Project

## Description

This project downloads and processes weather data daily, trains a machine learning model, and packages the model along with an API in a Docker image. The API renders predictions on a `/GET` endpoint and caches the prediction using Redis.

## Setup and Installation

1. Clone the repository:

```sh
git clone https://github.com/Deutzii/ml_orchestration_iabd.git
cd ml_orchestration_iabd/



history

PS P:\SEMESTRE FINAL IABD\orchestration ml\ml_orchestration_iabd> history

  Id     Duration CommandLine
  --     -------- -----------
   1        1.420 try { . "c:\Users\hp\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\browser\… 
   2        5.829 docker-compose restart postgres
   3     1:17.700 docker-compose exec airflow-webserver airflow webserver
   4       18.634 docker-compose exec airflow-webserver airflow db init
   5        6.241 docker-compose logs -f api
   6       23.175 docker-compose down
   7     2:45.525 docker-compose up --build -d
   8       25.610 docker-compose exec airflow-webserver airflow db init
   9        1.052 docker-compose logs -f api
  10       17.834 docker-compose down
  11     3:43.789 docker-compose up --build -d
  12       35.813 docker-compose exec airflow-webserver airflow db init
  13       25.942 tree
  14        4.155 ls -r
  15       15.827 wsl
  16       14.313 wsl
  17       25.995 docker-compose down
  18     3:48.522 docker-compose up --build -d
  19       38.929 docker-compose exec airflow-webserver airflow db init
  20       24.511 docker-compose down
  21     3:04.496 docker-compose up --build -d
  22       32.287 docker-compose exec airflow-webserver airflow db init
  23       43.342 /§…
  24        1.094 +0O£
  25       14.793 git status
  26        4.427 git checkout -b branche_beta
  27        0.523 git status
  28        1.146 git branch -v
  29        2.405 git add .
  30        1.137 git commit -m "first commit on beta branch, debugging api on docker"
  31        0.080 git push
  32       12.325 git push origin branche_beta
  33        3.988 git status
  34        2.568 git add .
  35        6.224 git commit -m "formatting all .py"
  36        6.164 git push origin branche_beta
  37       37.441 git status
  38       44.009 docker-compose down
  39        1.931 docker ps
  40        0.257 git status
  41     5:19.166 wsl
  42        3.868 python3 "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/streamlit.py"
  43        0.244 python3 "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  44       25.394 pip install streamlit
  45        0.216 python3 "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  46        0.404 python3 "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  47        0.657 python3 "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  48     1:47.968 wsl
  49        1.752 python -c "import streamlit as st; print(st.__version__)"
  50        1.255 python3 "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  51        2.120 python "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  52        1.250 streamlit run app_streamlit.py
  53    19:02.081 streamlit run "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  54     2:24.705 streamlit run "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  55     1:18.570 streamlit run "p:/SEMESTRE FINAL IABD/orchestration ml/ml_orchestration_iabd/dags/src/app_streamlit.py"
  56     5:53.551 docker-compose build
  57     1:45.250 docker-compose up -d
  58     1:38.010 docker-compose exec airflow-scheduler airflow celery status
  59       10.211 docker network ls
  60        0.468 docker network inspect <network_name>
  61        0.784 docker network inspect c3efb41f8cf7
  62       14.876 git status

PS P:\SEMESTRE FINAL IABD\orchestration ml\ml_orchestration_iabd> 



hitory command wsl


PS P:\SEMESTRE FINAL IABD\orchestration ml\ml_orchestration_iabd> wsl
root@DESKTOP-1OH4S87:/mnt/wsl/docker-desktop-bind-mounts/Ubuntu/80565ae3631399f683ca8012668b2b3ffdc153d450a8ad029b7b5319243982aa# history
    1  ls
    2  docker ls
    3  docker ps
    4  quit
    5  Quit() exit()
    6  exit() ex
    7  q
    8  wsl -- unregister docker-desktop-data
    9  docker-desktop --register
   10  docker ps
   11  curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'
   12  docker ps
   13  cd ..
   14  cd Users/
   15  ls
   16  cd hp/
   17  ls
   18  cd
   19  cd /mnt/p/SEMESTRE\ FINAL\ IABD/orchestration\ ml/
   20  ls
   21  ls -a
   22  cd tp_orchestration/
   23  git status
   24  mkdir -p ./dags ./logs ./plugins ./config
   25  ls
   26  mkdir -p ./dags ./logs ./plugins ./config
   27  echo -e "AIRFLOW_UID=$(id -u)" > .env
   28  docker compose up airlflow-init
   29  curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'
   30  cd
   31  cd /mnt/c/Windows
   32  cd System32/
   33  rm -f docker-compose.yaml
   34  cd
   35  cd /mnt/p/SEMESTRE\ FINAL\ IABD/orchestration\ ml/tp_orchestration/
   36  ls
   37  git status
   38  docker compose up airlflow-init
   39  ls
   40  docker compose up airflow-init
   41  ls
   42  docker ps
   43  cd
   44  cd !
   45  cd /mnt/p/SEMESTRE\ FINAL\ IABD/orchestration\ ml/tp_orchestration/
   46  ls
   47  code .
   48  quit
   49  exit
   50  pip install -r requirements.txt
   51  apt install python3-pip
   52  pip install -r requirements.txt
   53  python dags/src/api.py
   54  python3 dags/src/api.py
   55  git status
   56  git pull
   57  git status
   58  git log
   59  python3 dags/src/api.py
   60  tree
   61  apt  install tree
   62  tree
   63  docker-compose up --build
   64  systemctl status docker
   65  sudo systemctl start docker
   66  sudo chmod 666 /var/run/docker.sock
   67  sudo systemctl restart docker
   68  docker ps
   69  wsl --set-default-version 2
   70  docker --version
   71  cd /mnt/p/SEMESTRE_FINAL_IABD/orchestration_ml/ml_orchestration_iabd
   72  ls
   73  wsl --list --verbose
   74  exit
   75  docker ps
   76  wsl --shutdown
   77  exit
   78  ls
   79  exit
   80  tree
   81  exit
   82  python3 dags/src/streamlit.py
   83  desactiv
   84  desactive
   85  stop
   86  exit
   87  python3 dags/src/streamlit.py
   88  pip install -r requirements.txt
   89  python -c "import streamlit as st; print(st.__version__)"
   90  exit
   91  history
root@DESKTOP-1OH4S87:/mnt/wsl/docker-desktop-bind-mounts/Ubuntu/80565ae3631399f683ca8012668b2b3ffdc153d450a8ad029b7b5319243982aa# 