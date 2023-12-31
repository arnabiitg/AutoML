from airflow import DAG
from datetime import timedelta, datetime, timezone
from airflow.operators.python import PythonOperator
from ingestion import connect
import pytz

default_args = {
    "owner" : "arnab",
    "start_date" : datetime(2023,8,16,0,26, tzinfo= pytz.timezone('Asia/Kolkata')),
    "email" : "arnanbrohan2001@gmail.com",
    "email_on_failure" : True,
    "timezone" : "Asia/Kolkata"
}   

with DAG(
    dag_id = "mydag",
    default_args= default_args,
    catchup = False,
    schedule_interval =  "*/10 * * * *",
    
):
    execute =  PythonOperator(
        task_id= "data_ingestion",
        python_callable = connect.connection
    )
