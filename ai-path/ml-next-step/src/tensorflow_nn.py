# Import required libraries and packages
import pandas as pd
import tensorflow as tf

import config

# Main function
if __name__ == "__main__":

    # Load MNIST data
    df = pd.read_csv(config.NEW_DATA_PATH)
    df = df.drop(columns=["id"])

    # Go through all folds
    for fold in range(config.FOLDS_CNT):

        # initialize training and test data
        df_train = df.loc[df["kfold"] != fold, :]
        df_test = df.loc[df["kfold"] == fold, :]

        df_train = df_train.drop(columns=["kfold"])
        df_test = df_test.drop(columns=["kfold"])

        x_train = df_train.drop(columns=["label"]).values
        y_train = df_train.loc[:, "label"].values
        
        x_test = df_test.drop(columns=["label"]).values
        y_test = df_test.loc[:, "label"].values

        # Initialize model
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(64, activation="relu", input_shape=(len(x_train[1]), )), # input layer
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation="softmax") # output layer
        ])

        # Compile model
        model.compile(
            optimizer="Adam",
            loss="SparseCategoricalCrossentropy",
            metrics=["SparseCategoricalAccuracy"]
        )

        # Fit model
        result = model.fit(
            x=x_train,
            y=y_train,
            epochs=config.EPOCHS_CNT,
            validation_data=(x_test, y_test),
            # verbose=0
        )

        # Predict and print predictions
        model_accuracy = max(result.history["sparse_categorical_accuracy"])
        print(f"accuracy: {model_accuracy}")
        # print(result.history)