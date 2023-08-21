import example2 as example2
import psycopg2
from configuration import configure



sql_command = """
INSERT INTO weather_data(time,temperature,humidity,windspeed)
VALUES (%s,%s,%s,%s)
"""
class connect:
    def connection():
        try:

            values = example2.request()
            db_connection = None
            # Provide the name of the config file and the section name if needed
            params = configure.config()
            # Connecting to the database
            db_connection = psycopg2.connect(**params)

            # create a cursor
            cursor = db_connection.cursor()

            # QUERY execution
            cursor.execute(sql_command, values)
            db_connection.commit()
            version = cursor.fetchone()
            print(version)
            cursor.close()
            db_connection.close()
        
        except(Exception, psycopg2.DatabaseError) as error :
            
            print(error)

if __name__ == "__main__":
    connect.connection()