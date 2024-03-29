import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense

class LSTM:
    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.history = None
        
    def load_data(self, file_path):
        #csv or json
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            data = pd.read_json(file_path)
        else:
            raise ValueError("Invalid file format")
    
    def clean_data(self):
        # Scale data
        self.scaler.fit(data)
        data = self.scaler.transform(data)
        
        # Split data
        X = data[:, :-1]
        y = data[:, -1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2)
        
    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(50, input_shape=(self.X_train.shape[1], self.X_train.shape[2])))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')
        
    def train_model(self):
        self.history = self.model.fit(self.X_train, self.y_train, epochs=100, batch_size=32, validation_data=(self.X_test, self.y_test))
    
    def predict(self, X):
        return self.model.predict(X)
    
    def save_model(self, file_path):
        self.model.save(file_path)
        
    def run(self, file_path):
        self.load_data(file_path)
        self.clean_data()
        self.build_model()
        self.train_model()                
        
        
