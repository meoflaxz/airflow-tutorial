from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'meoflaxz',
    'retry': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
        dag_id='run_scrape_script',
        start_date=datetime(2023, 6, 8),
        schedule_interval='@daily',
) as dag:
    task1 = BashOperator(
        task_id='run_scrape_script',
        bash_command='python /opt/airflow/dags/scrape.py'
    )

task1