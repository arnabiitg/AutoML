import numpy as np
from keras.preprocessing.sequence import TimeseriesGenerator
from configparser import ConfigParser
import keras_tuner as kt
from keras.layers import LSTM, Dropout, LeakyReLU, Dense
from keras import Sequential
from keras.models import clone_model, load_model
from keras.callbacks import EarlyStopping

class temp_pred:
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
    win_length = int(params["win_length"])
    batch_size = int(params["batch_size"])
    num_features = int(params["num_features"])
    epochs = int(params["epochs"])

    def train_test_gen():
        win_length = temp_pred.win_length
        batch_size = temp_pred.batch_size

        # Data Reading
        x_train = np.load(temp_pred.root_path+"temperature//x_train_temp.npy") 
        y_train = np.load(temp_pred.root_path+"temperature//y_train_temp.npy")
        x_test = np.load(temp_pred.root_path+"temperature//x_test_temp.npy")
        y_test = np.load(temp_pred.root_path+"temperature//y_test_temp.npy")

        train_generator = TimeseriesGenerator(x_train,y_train, win_length, batch_size = batch_size)
        test_generator = TimeseriesGenerator(x_test,y_test, win_length, batch_size = batch_size)

        return train_generator, test_generator
    
    def old_model_generation():
        model = load_model("plugins//lib//prediction//model_temp.keras")
        model = clone_model(model)
        train_generator,  test_generator = temp_pred.train_test_gen()
        callback = EarlyStopping(monitor = "val_loss",patience = 15)
        model.compile(loss = "mean_squared_error", metrics = "mean_squared_error")
        model.fit(train_generator,epochs = temp_pred.epochs,validation_data = test_generator,shuffle = False, callbacks = [callback])
        model.save(temp_pred.root_path+"temperature//temp_model.keras")

    def build_model(hp):
        model = Sequential()
        model.add(LSTM(hp.Choice("units",[10,20,30,35]),activation = "tanh", input_shape = (temp_pred.win_length, temp_pred.num_features), return_sequences = True))
        model.add(LeakyReLU(alpha = 0.2))
        model.add(Dropout(0.5))
        model.add(LSTM(hp.Choice("units",[10,20,30,35]),activation = "tanh",  return_sequences = True))
        model.add(LeakyReLU(alpha = 0.2))
        model.add(LSTM(24, return_sequences = False))
        model.add(LeakyReLU(alpha = 0.2))
        model.add(Dense(1))
        model.compile(loss = "mean_squared_error", metrics = "accuracy")
        return model
    
    def get_best_model():
        train, test =  temp_pred.train_test_gen()

        tuner = kt.GridSearch(
            temp_pred.build_model,
            objective="val_accuracy",
            max_trials=10,
            directory = 'mydir4')
        tuner.search(train, epochs=10, validation_data= test)
        best_model = tuner.get_best_models()[0]

        best_model.save(temp_pred.root_path+"temperature//temp_model.keras")



if __name__ == "__main__":
    temp_pred.old_model_generation()


