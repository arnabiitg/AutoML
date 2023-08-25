from configparser import ConfigParser
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import logging

class datagen:
    root_path = "plugins//lib//mlpipeline//"
    # data reading
    df = pd.read_csv("plugins//lib//mlpipeline//model_data_input.csv",header= None, names = ["0","1","2","3"])
    df.drop("0", axis  = 1, inplace = True)
    
    def dataread(section, filename = root_path+"hyperparams.ini", ):
        parser = ConfigParser()
        parser.read(filename)
        if parser.has_section(section):
            objs = parser.items(section)
            db ={}
            for obj in objs:
                db[obj[0]] = obj[1]
        else:
            raise(Exception(f"{section} not available"))
        return db
    def train_test_gen_temp():
        params = datagen.dataread("temp_data_shape")

        # data scaling
        scaler = MinMaxScaler()
        data = scaler.fit_transform(datagen.df)
        row_num = data.shape[0]


        # train test split
        x_train_temp, x_test_temp, y_train_temp, y_test_temp = train_test_split(data[:int(0.8*row_num),:], data[:int(0.8*row_num),0],train_size= float(params["train_size"]), shuffle = False)
        validation = data[int(0.8*row_num):,:]
        np.save(datagen.root_path+"temperature//x_train_temp.npy",x_train_temp)
        np.save(datagen.root_path+"temperature//x_test_temp.npy",x_test_temp)
        np.save(datagen.root_path+"temperature//y_train_temp.npy",y_train_temp)
        np.save(datagen.root_path+"temperature//y_test_temp.npy",y_test_temp)
        np.save(datagen.root_path+"validation_data.npy",validation)
        
        logger = logging.getLogger(__name__)
        logger.info("temperature data is ready for model retraining")

    
    def train_test_gen_humid():
        params = datagen.dataread("humid_data_shape")

        # data scaling
        scaler = MinMaxScaler()
        data = scaler.fit_transform(datagen.df)
        row_num = data.shape[0]
        # train test split
        x_train_humid, x_test_humid, y_train_humid, y_test_humid = train_test_split(data[:int(0.8*row_num),:], data[:int(0.8*row_num),1],train_size= float(params["train_size"]), shuffle = False)
        validation = data[int(0.8*row_num):,:]
        np.save(datagen.root_path+"humidity//x_train_humid.npy",x_train_humid)
        np.save(datagen.root_path+"humidity//x_test_humid.npy",x_test_humid)
        np.save(datagen.root_path+"humidity//y_train_humid.npy",y_train_humid)
        np.save(datagen.root_path+"humidity//y_test_humid.npy",y_test_humid)
        np.save(datagen.root_path+"validation_data.npy",validation)
        
        logger = logging.getLogger(__name__)
        logger.info("humidty data is ready for model retraining")

    

    def train_test_gen_speed():
        params = datagen.dataread("windspeed_data_shape")

        # data scaling
        scaler = MinMaxScaler()
        data = scaler.fit_transform(datagen.df)
        row_num = data.shape[0]

        # train test split
        x_train_speed, x_test_speed, y_train_speed, y_test_speed = train_test_split(data[:int(0.8*row_num),:], data[:int(0.8*row_num),1],train_size= float(params["train_size"]), shuffle = False)
        validation = data[int(0.8*row_num):,:]
        np.save(datagen.root_path+"windspeed//x_train_speed.npy",x_train_speed)
        np.save(datagen.root_path+"windspeed//x_test_speed.npy",x_test_speed)
        np.save(datagen.root_path+"windspeed//y_train_speed.npy",y_train_speed)
        np.save(datagen.root_path+"windspeed//y_test_speed.npy",y_test_speed)
        np.save(datagen.root_path+"validation_data.npy",validation)

        logger = logging.getLogger(__name__)
        logger.info("windspeed data is ready for model retraining")


if __name__ == "__main__":
    datagen.train_test_gen_temp()
    datagen.train_test_gen_humid()
    datagen.train_test_gen_speed()