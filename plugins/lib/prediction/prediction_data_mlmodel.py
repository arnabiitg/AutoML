import pandas as pd
import os
import keras as keras
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from datetime import datetime, timedelta

# data reading

scaler = MinMaxScaler()
# print(df.head())

class prediction:
    def prediction():
        root_dir = "//opt//airflow//"
        # data reading 
        df = pd.read_csv(root_dir+"plugins//lib//prediction//prediction_data_input.csv", names = ["0","1","a","b","c"], header= None)
        df.drop("0",inplace= True, axis =1)

        df.set_index("1",inplace=True)
        # model loading
        model_temp = keras.models.load_model(root_dir+"plugins//lib//prediction//model_temp.keras")
        model_humid = keras.models.load_model(root_dir+"plugins//lib//prediction//model_humidity.keras")
        model_windspeed = keras.models.load_model(root_dir+"plugins//lib//prediction//model_windspeed.keras")


        for i in range(10):
            # data changing
            data = scaler.fit_transform(df)
            data = data.reshape(-1,10,3)

            # prdict data generation

            temp = model_temp.predict(data)
            humid = model_humid.predict(data)
            windspeed = model_windspeed.predict(data)

            pred = scaler.inverse_transform([[temp[0][0],humid[0][0],windspeed[0][0]]])[0]
            df.drop(index=df.index[0], axis =0, inplace = True)
            curr = datetime.now()
            curr = curr.replace(minute=0,second=0,microsecond=0)
            df = pd.concat([df,pd.DataFrame(pred.reshape(1,-1), index = pd.Index([curr+timedelta(hours=i)]), columns = ["a","b","c"])], axis = 0)
            

        df.to_csv(root_dir+"plugins//lib//prediction//prediction_data_output.csv",header= False)

if __name__ == "__main__":
    prediction.prediction()