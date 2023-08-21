import psycopg2
from configuration import configure
import pandas as pd


sql_command = """
INSERT INTO weather_pred(time,temperature,humidity,windspeed)
VALUES (%s,%s,%s,%s)
ON CONFLICT DO UPDATE
"""
class pred_connect:
    def connection():
        root_dir = "//opt//airflow//"
        try:
            
            db_connection = None
            # Provide the name of the config file and the section name if needed
            params = configure.config()
            # Connecting to the database
            db_connection = psycopg2.connect(**params)

            # create a cursor
            cursor = db_connection.cursor()

            # data reading
            df = pd.read_csv(root_dir+"plugins//lib//prediction//prediction_data_output.csv", header = None)
            values = list(df.itertuples(index= False, name = None))
            # print(values)
            # QUERY execution
            cursor.executemany(sql_command, values)
            db_connection.commit()

            cursor.close()
            db_connection.close()
        
        except(Exception, psycopg2.DatabaseError) as error :
            
            print(error)


if __name__ == "__main__":
    pred_connect.connection()