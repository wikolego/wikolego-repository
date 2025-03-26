import os
import config
import joblib
import pandas as pd
import model_dispatcher
from sklearn import metrics

def train_model(df_train: pd.DataFrame, model):
    # Format train data
    x_train = df_train.drop(axis=1, columns=["id", "label"]).values
    y_train = df_train["label"].values

    # Fit model
    model.fit(x_train, y_train)

    return model

def test_model(df_test: pd.DataFrame, model):
    # Format test data
    x_test = df_test.drop(axis=1, columns=["id", "label"]).values

    # Fit model
    predicted = model.predict(x_test)

    # Calculate and print accuracy
    y_test = df_test["label"].values
    acc = metrics.accuracy_score(y_test, predicted)
    print(acc)

def save_model(model, file_name):
    joblib.dump(
        model,
        os.path.join(config.MODEL_OUTPUT, f"{file_name}.bin")
    )

if __name__ == "__main__":
    df = pd.read_csv(config.TRAINING_FILE_FOLDS)

    for model_name in model_dispatcher.model_names:
        for i in range(config.NO_FOLDS):

            df_train = df[df.kfold != i].reset_index(drop=True)
            df_test = df[df.kfold == i].reset_index(drop=True)

            # print(df_test["label"])

            # run(i, model_dispatcher.models[model_name], model_name)
            model = model_dispatcher.models[model_name]
            train_model(df_train, model)
            print(f"Model={model_name}, Fold={i}, Accuracy=", end="")
            predicted = test_model(df_test, model)
            save_model(model, f"{model_name}_{i}")

            # print(predicted)