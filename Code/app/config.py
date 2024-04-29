import os

class Config(object):
    
    def __init__(self):
        
        # Directories
        self.REPO_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir))
        self.DATA_DIR = os.path.abspath(os.path.join(self.REPO_DIR, 'datasets'))
        self.ACCEL_DIR = os.path.abspath(os.path.join(self.DATA_DIR, 'Acceleration'))
        
        # Data preprocessing
        self.WINDOW_SIZE = 4
        self.WINDOW_OFFSET = int((self.WINDOW_SIZE) / 2)
        
        # Training
        self.EPOCHS = 100
        self.BATCH_SIZE = 32
        
        # LSTM