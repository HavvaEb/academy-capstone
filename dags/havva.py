import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from conveyor.operators import ConveyorSparkSubmitOperatorV2


dag = DAG(
    dag_id='havva',
    schedule_interval='*/5 0 * * *',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=10),
    tags=['learning', 'having fun'],
)


ConveyorSparkSubmitOperatorV2(
    dag=dag,
    spark_main_version=3,
    task_id="migrate",
    num_executors=1,
    driver_instance_type="mx.small",
    executor_instance_type="mx.small",
    aws_role="havva-conveyor-{{ macros.conveyor.env() }}",
    application="local:///app/main.py",
)