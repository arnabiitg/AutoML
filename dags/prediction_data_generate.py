from airflow import DAG
from datetime import timedelta, datetime, timezone
from airflow.operators.python import PythonOperator
from airflow.models.baseoperator import chain
from prediction_data_ingestion import connect
from prediction_data_mlmodel import prediction
from prediction_export import pred_connect
import pytz


default_args = {
    "owner" : "arnab",
    "start_date" : datetime(2023,8,16,0,26, tzinfo= pytz.timezone('Asia/Kolkata')),
    "email" : "arnanbrohan2001@gmail.com",
    "email_on_failure" : True,
    "timezone" : "Asia/Kolkata"
}  


with DAG(
    dag_id = "prediction_dag",
    default_args= default_args,
    catchup = False,
    schedule_interval =  "@hourly",
    
):
    t1 =  PythonOperator(
        task_id= "data_ingestion",
        python_callable = connect.connection
    )

    t2 =  PythonOperator(
        task_id= "data_prediction",
        python_callable = prediction.prediction
    )

    t3 =  PythonOperator(
        task_id= "data_export",
        python_callable = pred_connect.connection
    )

    chain(t1,t2,t3) 
