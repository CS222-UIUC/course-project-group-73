# load data
# split the data into train and test sets
# build the network architecture
# compile network
# train network

import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt

DATASET_PATH = './data.json'
GLOBAL_HISTORY = None

def load_data(dataset_path):
    with open(dataset_path, "r") as fp:
        data = json.load(fp)
    
    # convert lists into numpy arrays
    inputs = np.array(data['mfcc'])
    targets = np.array(data['labels'])

    return (inputs, targets)

def plot_history(history):
    fig,axs = plt.subplots(2)
    
    #create the acurracy subplot
    axs[0].plot(history.history["accuracy"], label = "train accuracy")
    axs[0].plot(history.history["val_accuracy"], label = "test accuracy")
    axs[0].set_ylabel("accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy eval")
    

    #create the error subplot
    axs[1].plot(history.history["loss"], label = "train error")
    axs[1].plot(history.history["val_loss"], label = "test error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error eval")


    plt.savefig("error_accuracy.png")
    plt.show()





if __name__ == '__main__':
    inputs, targets = load_data(DATASET_PATH)

    # 30% of data for test set
    # 70% for train set
    inputs_train, inputs_test, targets_train, targets_test = train_test_split(inputs, targets, test_size=0.3)

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(inputs.shape[1], inputs.shape[2])),
        keras.layers.Dense(2048, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(1024, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(512, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(256, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation='softmax'),
    ])

    optimizer = keras.optimizers.Adam(learning_rate=0.00006)
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary()

    history = model.fit(inputs_train, targets_train, validation_data=(inputs_test, targets_test), batch_size=32, epochs=100)

    #plot the accuracy and error vs epoch
    plot_history(history)

def test_accuracy_change(history):
    training_accuracy = history.history["accuracy"]
    assert training_accuracy[0] < training_accuracy[-1]
    print(training_accuracy)

    val_accuracy = history.history["val_accuracy"]
    assert val_accuracy[0] < val_accuracy[-1]
    print(val_accuracy)


test_accuracy_change(GLOBAL_HISTORY)
print("All test cases passed - the model improved accuracy")