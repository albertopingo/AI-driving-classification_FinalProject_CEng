import numpy as np
import os
import json
import pandas as pd


def load_preprocessed_data(path):
    # Load preprocessed data from a file
    preprocessed_data = []
    
    return preprocessed_data

def save_preprocessed_data(preprocessed_data):
    # Save the preprocessed data to a file
    
    np.save('preprocessed_data.npy', preprocessed_data)
    
    pass

def load_raw_data(path):
    data_bmw = []
    data_honda = []
    labels_bmw = []
    labels_honda = []
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                car = os.path.basename(root).split()[0].upper()            
                label = os.path.basename(os.path.dirname(root))
                # print(f'Processing {car} {label} {file}...')
                
                file_data = json.load(open(os.path.join(root, file)))
                file_data = file_data['capturedData']
                                        
                # Convert to dataframe
                file_data = pd.DataFrame(file_data)           
                
                # Drop unnecessary columns
                file_data = file_data.drop(['id', 'gyroscopeXAxis', 'gyroscopeYAxis', 'gyroscopeZAxis'], axis=1)
                
                # Rename speed Km/h to speed
                file_data.rename(columns={'speed Km/h': 'speed'}, inplace=True)
                file_data.rename(columns={'speedKmh': 'speed'}, inplace=True)
                
                # Drop timestamp
                file_data = file_data.drop(['createdAt'], axis=1, errors='ignore')
                file_data = file_data.drop(['timestamp'], axis=1, errors='ignore')                    
                
                if car == 'BMW':
                    data_bmw.append(file_data.copy())
                    labels_bmw.append(label)
                elif car == 'HONDA':
                    data_honda.append(file_data.copy())
                    labels_honda.append(label)            

    #check for NaNs
    if data_bmw[0].isnull().values.any() or data_honda[0].isnull().values.any():
        print('NaNs in data')
    else:
        print('NO NaNs in data')
        
    # add data_bmw and data_honda to dataset
    dataset = data_bmw + data_honda
    dataset_labels = labels_bmw + labels_honda
    
    return dataset, dataset_labels

def sequenced_data(data, window_size = 4, window_offset = 2):
    sequences = []
    labels = []

    for i in range(len(data)):
        for j in range(0, len(data[i]) - window_size + 1, window_offset):
            sequence = data[i].iloc[j:j+window_size].values
            sequences.append(sequence)
            
            # Calculate mean of accelerometerYAxis in the current window
            mean = np.mean(data[i][j:j+window_size]['accelerometerYAxis'])
            
            # Determine label based on the mean value
            if mean > 0.5:
                label = 'aggressive'
            elif mean > 0.2:
                label = 'normal'
            else:
                label = 'slow'
            
            labels.append(label)

    sequences = np.array(sequences)
    labels = np.array(labels)

    print('Sequences:')
    print(sequences)
    print('Labels:')
    print(labels)
    

def encode_labels(labels):
    # Encode the labels
    encoded_labels = []
    
    return encoded_labels

