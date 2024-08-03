import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import json

class LSTM:
    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.history = None
        
    
    def prep_data(self, file_path):
        # CSV file
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path, header=None)
            print("Raw data: ")
            print(data)
            
            # Drop the first 2 rows
            data = data.iloc[2:]
            
            # Set the first row as the header and drop it
            data.columns = data.iloc[0]
            data = data.iloc[1:]     
            
            # Select specific columns
            desired_columns = ['accelerometerXAxis', 'accelerometerYAxis', 'accelerometerZAxis', 'gyroscopeXAxis', 'gyroscopeYAxis', 'gyroscopeZAxis', 'speedKmh']
            data = data.loc[:, desired_columns]
            
            # Drop empty columns
            data = data.dropna(axis=1, how='all')
            
            # Drop rows with all NaN values
            data = data.dropna(how='all')
                        
            print("Final data: ")
            print(data)
            
            # scale the data
            scaledData = self.scaler.fit_transform(data)
            
        # JSON file
        elif file_path.endswith('.json'):
            with open(file_path) as file:
                data = json.load(file)
            print("Raw data: ")
            print(data)
            
            # Extract the captured data
            capturedData = data['capturedData']
            
            # Convert to dataframe
            capturedData = pd.DataFrame(capturedData)
            
            # Drop unnecessary columns
            capturedData = capturedData.drop(['id', 'Latitude', 'Longitude', 'createdAt'], axis=1)
            print("Final data: ")
            print(capturedData)
                        
            scaledData = self.scaler.fit_transform(capturedData)
            
            
        else:
            raise ValueError("Invalid file format")     
        
        print("Scaled data: ")
        print(scaledData)
        
        
        
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
        self.prep_data(file_path)
        # self.build_model()
        # self.train_model()                
        
        
