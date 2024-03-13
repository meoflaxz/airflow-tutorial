from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'meoflaxz',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

@dag(dag_id='taskflow_api_v1',
    default_args=default_args,
    description='First DAG with TaskFlow API',
    schedule_interval='@daily',
    start_date=datetime(2021, 1, 1)
    )
def hello_world_etl():

    @task()
    def get_name():
        return "Atan"

    @task()
    def get_age():
        return 19
    
    @task()
    def greet(name, age):
        print(f"Hello World! My name is {name}"
              f"and I am {age} years old!")

    name = get_name()
    age = get_age()
    greet(name=name, age=age)

greet_dag = hello_world_etl()