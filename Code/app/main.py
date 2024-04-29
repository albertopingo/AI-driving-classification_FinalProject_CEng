from argparse import ArgumentParser
import os

from config import Config
from dataprocessing import *

def main(args):    
    config = Config()
    
    print("Repository directory: ", config.REPO_DIR)
    print("Data directory: ", config.DATA_DIR)
    print("Acceleration directory: ", config.ACCEL_DIR)
    
    # Data preprocessing
    dataset, dataset_labels = load_raw_data(config.ACCEL_DIR)
    
    sequenced_data(dataset, config.WINDOW_SIZE, config.WINDOW_OFFSET)
    
    

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