from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'meoflaxz',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG (
    dag_id='first_dags_v5',
    default_args=default_args,
    description='This is our first DAG',
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily',
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "Hello World from Task 1"',
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo "Hello World from Task 2"',
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo "Hello World from Task 3"',
    )

# task1 >> task2
# task1 >> task3

task1 >> [task2, task3]