from argparse import ArgumentParser
import os
import csv

from config import Config
from dataprocessing import *

import numpy as np

def main(args):    
    config = Config()
    
    print("Repository directory: ", config.REPO_DIR)
    print("Data directory: ", config.DATA_DIR)
    print("Acceleration directory: ", config.ACCEL_DIR)
    
    # Data preprocessing
    dataset, dataset_labels, data_bmw, data_honda = load_raw_data(config.ACCEL_DIR)
    
    sequences_full, labels = sequenced_data(dataset, config.WINDOW_SIZE, config.WINDOW_OFFSET)
    sequences_bmw, labels_bmw = sequenced_data(data_bmw, config.WINDOW_SIZE, config.WINDOW_OFFSET)
    sequences_honda, labels_honda = sequenced_data(data_honda, config.WINDOW_SIZE, config.WINDOW_OFFSET)
          
    headers = ['AccelerometerX', 'AccelerometerY', 'AccelerometerZ', 'Speed', 'Label']

    save_only_natural_csv(data_bmw, 'bmw')
    save_only_natural_csv(data_honda, 'honda')

    
    # Load the preprocessed dataset
    preprocessed_dataset_bmw = load_preprocessed_data('datasets_tratados/bmw_onlynatural.csv')
    sum_values(preprocessed_dataset_bmw,dataset_name='bmw') 

    preprocessed_dataset_honda = load_preprocessed_data('datasets_tratados/honda_onlynatural.csv')
    sum_values(preprocessed_dataset_honda,dataset_name='honda') 

    preprocessed_dataset_bmw_somatorio = load_preprocessed_data('somatorios/bmw_sum_values.csv')
    preprocessed_dataset_honda_somatorio = load_preprocessed_data('somatorios/honda_sum_values.csv')

    # create_sequences(preprocessed_dataset_bmw_somatorio,dataset_name='bmw')
    # create_sequences(preprocessed_dataset_honda_somatorio,dataset_name='honda')

    max_values(preprocessed_dataset_bmw)

    classify_agressive(preprocessed_dataset_bmw,preprocessed_dataset_bmw_somatorio,dataset_name='bmw')
    classify_agressive(preprocessed_dataset_honda,preprocessed_dataset_honda_somatorio,dataset_name='honda')


    with open('sequences_bmw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(headers)
        writer.writerows(sequences_bmw)
    
    with open('sequences_honda.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(headers)
        writer.writerows(sequences_honda)
        


    

if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--save_dir', '-s',
                        help='Directory to save the model in.',
                        default= 'saves')
    parser.add_argument('--dataset', '-d',
                        help='Which dataset to train/test the model on?',
                        default= 'full')
    args = parser.parse_args()
    main(args)
