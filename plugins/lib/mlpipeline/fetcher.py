import psycopg2
from configuration import configure
import pandas as pd
import logging
sql_command = """
SELECT * FROM weather_data
WHERE time in (
        SELECT time FROM weather_data
        ORDER BY time DESC
        LIMIT 96
)
"""
class connect:
    def connection():
        try:

            db_connection = None
            # Provide the name of the config file and the section name if needed
            params = configure.config()
            # Connecting to the database
            db_connection = psycopg2.connect(**params)

            # create a cursor
            cursor = db_connection.cursor()

            # QUERY execution
            cursor.execute(sql_command)
            db_connection.commit()
            
            data = cursor.fetchall()

            # csv creation
            connect.csvcreator(data)

            cursor.close()
            db_connection.close()
        
        except(Exception, psycopg2.DatabaseError) as error :
            
            print(error)
    def csvcreator(data):
        df = pd.DataFrame(data,columns = ["1","2","3","4"])
        # df.drop("0", inplace = True, axis=1)
        print(df)
        df.to_csv("plugins//lib//mlpipeline//model_data_input.csv",header = None,index=False)
        logger = logging.getLogger(__name__)
        logger.info("Data is fetched for model retraining")

if __name__ == "__main__":
    connect.connection()