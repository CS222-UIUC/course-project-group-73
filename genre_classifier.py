# load data
# split the data into train and test sets
# build the network architecture
# compile network
# train network

import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras

DATASET_PATH = './data.json'

def load_data(dataset_path):
    with open(dataset_path, "r") as fp:
        data = json.load(fp)
    
    # convert lists into numpy arrays
    inputs = np.array(data['mfcc'])
    targets = np.array(data['labels'])

    return (inputs, targets)


if __name__ == '__main__':
    inputs, targets = load_data(DATASET_PATH)

    # 30% of data for test set
    # 70% for train set
    inputs_train, inputs_test, targets_train, targets_test = train_test_split(inputs, targets, test_size=0.3)

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(inputs.shape[1], inputs.shape[2])),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(10, activation='softmax'),
    ])

    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary()

    history = model.fit(targets_train, targets_train, validation_data=(inputs_test, targets_test), batch_size=32, epochs=50)