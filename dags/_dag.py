from datetime import datetime, timedelta
from typing import Optional

from airflow.decorators import dag
from _utils import task_fail_alert_telegram

def ricky_dag(
        dag_id: str,
        schedule: str,
        start_date: Optional[datetime] = datetime(2020,1,1),
        tags: Optional[list] = ['test'],
        default_args: Optional[dict] = {},
        catchup: Optional[bool] = False,
        params: Optional[dict] = {},
        **kwargs
):
    

    DEFAULT_ARGS = {
        "owner":"dev.creusot.aymeric7@gmail.com",
        "depends_on_past": True,
        "start_date":datetime(2000,1,1),
        "retries":0,
        "retry_delay": timedelta(seconds=30),
        "on_failure_callback": task_fail_alert_telegram,
    }

    DEFAULT_ARGS.update(default_args)

    return dag(
        dag_id=dag_id,
        start_date=start_date,
        tags=tags,
        schedule=schedule,
        default_args=DEFAULT_ARGS,
        params=params,
        catchup=catchup,
        **kwargs
    )