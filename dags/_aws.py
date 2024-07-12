import boto3
from airflow.hooks.base import BaseHook

class AwsApiClient:
    def __init__(self, aws_conn_id = "aws_default"):
        self.aws_hook = BaseHook.get_connection(aws_conn_id)

        self.session = boto3.Session(
            aws_access_key_id=self.aws_hook.login,
            aws_secret_access_key=self.aws_hook.password,
            region_name='eu-central-1'
        )
