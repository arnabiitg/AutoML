from keras.saving import load_model
import numpy as np
from temp_model import temp_pred
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.callbacks import EarlyStopping

class evaluation:
    root_path  = "plugins//lib//mlpipeline//"
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
    
    def training():
        model = load_model(evaluation.root_path+"temperature//temp_model.keras")
        train_generator,  test_generator = evaluation.train_test_gen()
        callback = EarlyStopping(monitor = "val_loss",patience = 15)

        history = model.fit(train_generator,epochs = 100,validation_data = test_generator,shuffle = False, callbacks = [callback])
        return history 
    

    def monitor():
        history = evaluation.training()
        