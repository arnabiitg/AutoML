import psycopg2
from configuration import configure
import json

sql_command = """
SELECT * FROM weather_pred
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

            cursor.close()
            db_connection.close()
        
        except(Exception, psycopg2.DatabaseError) as error :
            
            print(error)
        return data
    def makedata():
        response = {"time":[],"temperature":[],"humidity":[],"windspeed":[]}
        data = connect.connection()

        for row in data:
            response["time"].append(row[0].strftime("%Y-%m-%d %H:%M:%S"))
            response["temperature"].append(row[1])
            response["humidity"].append(row[2])
            response["windspeed"].append(row[3])
        # response["time"] = setresponse["time"]
        # response["temperature"] = response["temperature"]
        # response["humidity"] = response["humidity"]
        # response["windspeed"] = response["windspeed"]
        return json.dumps(response)

    
if __name__ == "__main__":
    print(connect.makedata())