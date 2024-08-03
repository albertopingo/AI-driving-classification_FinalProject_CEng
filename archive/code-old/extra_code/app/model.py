from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense
from config import Config

# Load the configuration
config = Config()

# Data Preprocessing
scaler = MinMaxScaler()

# Scale the features
x_scaled = scaler.fit_transform(x)

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Define the LSTM model 
model = Sequential()
model.add(LSTM(units=config.HIDDEN_UNITS, input_shape=(config.TIMESTEPS, config.NUM_FEATURES)))
model.add(Dropout(0.2))  
model.add(Dense(units=config.HIDDEN_UNITS, activation='relu'))  
model.add(Dropout(0.2))  
model.add(Dense(units=config.NUM_CLASSES, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=config.EPOCHS, batch_size=config.BATCH_SIZE)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")
