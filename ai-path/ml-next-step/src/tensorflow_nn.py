# Import required libraries and packages
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

import config

print(tf.__version__)

# Load MNIST data
dataframe = pd.read_csv(config.NEW_DATA_PATH)

# initialize training data
df = dataframe.drop(columns=["id"])

df_train = df.loc[df["kfold"] != 1, :]
df_test = df.loc[df["kfold"] == 1, :]

df_train = df_train.drop(columns=["kfold"])
df_test = df_test.drop(columns=["kfold"])

# Initialize model
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(28 * 28), # input layer
#     tf.keras.layers.Dense(64, activation="relu"),
#     tf.keras.layers.Dense(64, activation="relu"),
#     tf.keras.layers.Dense(10) # output layer
# ])

model = tf.keras.models.Sequential([
    # tf.keras.Input(shape=(None, None, 28 * 28)), # input layer
    tf.keras.layers.Dense(64, activation="relu", input_shape=(28 * 28, )), # input layer
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10) # output layer
])

# Compile model
model.compile(
    optimizer="Adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# X_data = df_train.drop(columns=["label"])

# print(len(X_data.columns))

# exit()

# Fit model
result = model.fit(
    df_train.drop(columns=["label"]).values,
    df_train.loc[:, "label"].values,
    epochs=10
)

# Predict and print predictions
predictions = max(result.history["accuracy"])
print(predictions)

plt.plot(result.history["accuracy"])
plt.show()