import requests
import pprint



def api_call():
    url = "https://api.data.gov.my/data-catalogue \
        ?id=hies_district&limit=3"
    response_json = requests.get(url=url).json()
    return response_json

def print_result(**context):
    response_json = context['task_instance'].xcom_pull(task_ids='api_call')
    pprint.pprint(response_json)

with DAG(
    default_args=default_args,
    dag_id='demo_api_call',
    description='API call demo',
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='api_call',
        python_callable=api_call,
    )

    task2 = PythonOperator(
        task_id='print_result',
        python_callable=print_result,
    )

    task1 >> task2