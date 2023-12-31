import numpy as np
from keras.preprocessing.sequence import TimeseriesGenerator
from configparser import ConfigParser
import keras_tuner as kt
from keras.layers import LSTM, Dropout, LeakyReLU, Dense
from keras import Sequential
from keras.models import clone_models
from keras.callbacks import EarlyStopping

class humid_pred:
    root_path = "plugins//lib//mlpipeline//"

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
    params = dataread("temp_data_shape")
    win_length = params["win_length"]
    batch_size = params["batch_size"]
    num_features = params["num_features"]

    def train_test_gen():
        win_length = humid_pred.win_length
        batch_size = humid_pred.batch_size

        # Data Reading
        x_train = np.load(humid_pred.root_path+"humidity//x_train_humid.npy") 
        y_train = np.load(humid_pred.root_path+"humidity//y_train_humid.npy")
        x_test = np.load(humid_pred.root_path+"humidity//x_test_humid.npy")
        y_test = np.load(humid_pred.root_path+"humidity//y_test_humid.npy")

        train_generator = TimeseriesGenerator(x_train,y_train, win_length, batch_size = batch_size)
        test_generator = TimeseriesGenerator(x_test,y_test, win_length, batch_size = batch_size)

        return train_generator, test_generator
    
    def old_model_generation():
        model = clone_models("plugins//lib//prediction//model_humidity.keras")
        train_generator,  test_generator = humid_pred.train_test_gen()
        callback = EarlyStopping(monitor = "val_loss",patience = 15)
        model.compile(loss = "mean_squared_error", metrics = "mean_squared_error")
        model.fit(train_generator,epochs = humid_pred.epochs,validation_data = test_generator,shuffle = False, callbacks = [callback])
        model.save(humid_pred.root_path+"humidity//model_temp.keras")

    def build_model(hp):
        model = Sequential()
        model.add(LSTM(hp.Choice("units",[64,128,256,512]),activation = "tanh", input_shape = (humid_pred.win_length, humid_pred.num_features), return_sequences = True))
        model.add(LeakyReLU(alpha = 0.2))
        model.add(LSTM(hp.Choice("units",[64,128,256,512]),activation = "tanh",  return_sequences = True))
        model.add(LeakyReLU(alpha = 0.2))
        model.add(Dropout(0.5))
        model.add(Dense(100,activation = "leaky_relu"))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.compile(loss = "mean_squared_error", metrics = "accuracy")
        return model
    
    def get_best_model():
        train, test =  humid_pred.train_test_gen()

        tuner = kt.GridSearch(
            humid_pred.build_model,
            objective="val_accuracy",
            max_trials=10,
            directory = 'mydir4')
        tuner.search(train, epochs=10, validation_data= test)
        best_model = tuner.get_best_models()[0]

        best_model.save(humid_pred.root_path+"humidity//temp_model.keras")


if  __name__ == "__main__":
    humid_pred.get_best_model()

