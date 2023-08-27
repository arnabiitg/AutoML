from configparser import ConfigParser
import os
# //opt//airflow//
class configure:
    def config (filename = 'data.ini', section= "postgresql"):
        #Create a Parser
        parser = ConfigParser()
        #Read the config file
        parser.read(filename)
        db ={}
        try:
            objs = parser.items(section)
            for obj in objs:
                db[obj[0]] = obj[1]
        except Exception as e:
            # raise Exception(f"{section} isn't available in the given {filename}")
            raise e
        return db

if __name__ == "__main__":
    print(configure.config())