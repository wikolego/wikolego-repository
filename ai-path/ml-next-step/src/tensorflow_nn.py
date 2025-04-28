# Import required libraries and packages
import pandas as pd
import tensorflow as tf

import config

# Load MNIST data
dataframe = pd.read_csv(config.NEW_DATA_PATH)

# initialize training data
df = dataframe.drop(columns=["id"])

df_train = df.loc[df["kfold"] != 1, :]
df_test = df.loc[df["kfold"] == 1, :]

df_train.drop(columns=["kfold"])
df_test.drop(columns=["kfold"])

# Initialize model
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(28 * 28), # input layer
#     tf.keras.layers.Dense(64, activation="relu"),
#     tf.keras.layers.Dense(64, activation="relu"),
#     tf.keras.layers.Dense(10) # output layer
# ])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(28 * 28), # input layer
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10) # output layer
])

# Compile model
model.compile(
    optimizer="Adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Fit model
result = model.fit(
    df_train.loc[:, df.columns != 'label'],
    df_train.loc[:, 'label'],
    epochs=100
)

# Predict and print predictions
predictions = max(result.history['accuracy'])
print(predictions)