from pmdarima.arima import auto_arima
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import  MinMaxScaler
class basemodel:
    root_path = "plugins//lib//mlpipeline//"
    def make_arima_model():
        data_1 = np.load(basemodel.root_path+"temperature//x_train_temp.npy")
        data_2 = np.load(basemodel.root_path+"temperature//x_test_temp.npy")
        data = np.concatenate([data_1,data_2])
        model = auto_arima(data[0], start_p=1, start_q=0 ,
                      test='adf',       
                      max_p= 30, max_q=30, 
                      m= 7,              
                      d= 1,
                      seasonal = False,     
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)
        with open(basemodel.root_path+"temperature//temp_arima_model.pkl","wb") as f:
            pickle.dump(model,f)

if __name__ == "__main__":
    basemodel.make_arima_model()