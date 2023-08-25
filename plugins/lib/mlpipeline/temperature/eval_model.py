from keras.saving import load_model
import numpy as np
from temp_model import temp_pred
from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import  MinMaxScaler
from keras.models import load_model
import pandas as pd
import pickle
from sklearn.metrics import *
# import airflow

class evaluation:
    root_path  = "plugins//lib//mlpipeline//"
    
    def evaluate():
        data = np.load(evaluation.root_path+"validation_data.npy")
        win_length = temp_pred.win_length
        batch_size = temp_pred.batch_size

        # Data Reading
        
        x_test = data
        y_test = data[:,0]

        test_generator = TimeseriesGenerator(x_test,y_test, win_length, batch_size = batch_size)

        # model loading
        lstm_model = load_model(evaluation.root_path+"temperature//temp_model.keras")
        with open(evaluation.root_path+"temperature//temp_arima_model.pkl","rb") as f:
            arima_model = pickle.load(f)  

        lstm_pred = lstm_model.predict(test_generator)
        arima_pred = arima_model.predict(n_periods = lstm_pred.shape[0])

        return lstm_pred, arima_pred

    def monitor(**kwargs):
        data = np.load(evaluation.root_path+"validation_data.npy")
        lstm_pred, arima_pred = evaluation.evaluate()
        lstm, base =0,0
        print(data.shape, lstm_pred.shape, arima_pred.shape)
        mse_curr = mean_squared_error(lstm_pred,data[:-10,0])
        mse_base = mean_squared_error(arima_pred,data[:-10,0])

        mae_curr = mean_absolute_error(lstm_pred,data[:-10,0])
        mae_base = mean_absolute_error(arima_pred,data[:-10,0])

        r2_curr = r2_score(lstm_pred,data[:-10,0])
        r2_base = r2_score(arima_pred,data[:-10,0])

        if (mse_curr < mse_base):
            lstm = lstm +1
        else:
            base = base +1

        if(mae_curr<mae_base):
            lstm = lstm +1
        else:
            base = base +1
        
        if(r2_curr>r2_base):
            lstm = lstm +1
        else:
            base = base +1
        print(lstm,base)
        # if(lstm<base):
        #     kwargs["ti"].xcom_push(key = "retraining_mode", value = 0)
        # else:
        #     kwargs["ti"].xcom_push(key = "retraining_mode", value = 1)

if __name__ == "__main__":
    evaluation.monitor()