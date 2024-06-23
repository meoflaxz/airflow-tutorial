from datetime import datetime, timedelta
from airflow.decorators import dag, task
import requests
import pprint

default_args = {
    'owner': 'meoflaxz',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

@dag(dag_id='callapi_taskflow_v5',
    default_args=default_args,
    description='testing',
    schedule_interval='@daily',
    start_date=datetime(2021, 1, 1),
    catchup=False)

def run_task():

    @task()
    def api_call():
        url = "https://api.data.gov.my/data-catalogue?id=hies_district&limit=3"
        response_json = requests.get(url=url).json()
        pprint.pprint(response_json)
        return response_json

    api_call()

run_dag = run_task()
