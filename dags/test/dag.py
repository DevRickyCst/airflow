from airflow.decorators import task
from _dag import ricky_dag
from _aws import AwsApiClient


aws = AwsApiClient()

@task
def hello():


@ricky_dag(
    dag_id="hello",
    schedule='@daily',
)
def test():

    ma_task = hello()


test()
