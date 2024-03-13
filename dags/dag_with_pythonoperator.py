from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'meoflaxz',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

def greet(age, ti):
    firstname = ti.xcom_pull(task_ids='get_firstname')
    lastname = ti.xcom_pull(task_ids='get_lastname')
    print(f'Hello my name is {firstname} {lastname} and I am {age} years old')

def get_firstname():
    return 'Atan'

def get_lastname():
    return 'Setan'

with DAG (
    default_args=default_args,
    dag_id='dag_with_pythonoperator_v6',
    description='First DAG with PythonOperator',
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily'
) as dag:

    task1=PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': '25'}
    )

    task2=PythonOperator(
        task_id='get_firstname',
        python_callable=get_firstname
    )

    task3=PythonOperator(
        task_id='get_lastname',
        python_callable=get_lastname
    )

task2 >> task3 >> task1