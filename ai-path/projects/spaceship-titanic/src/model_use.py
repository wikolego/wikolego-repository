import os
import config
import joblib
import pandas as pd
import model_dispatcher

def train_model(df_train: pd.DataFrame, model):
    # Format train data
    x_train = df_train.drop(axis=1, columns=["label"]).values
    y_train = df_train["label"].values

    # Fit model
    model.fit(x_train, y_train)

    return model

def test_model(df_test: pd.DataFrame, model):
    # Format test data
    x_test = df_test.drop(axis=1, columns=["id"]).values

    # Fit model
    predicted = model.predict(x_test)

    return predicted

def save_model(model, file_name):
    joblib.dump(
        model,
        os.path.join(config.MODEL_OUTPUT, f"{file_name}.bin")
    )

if __name__ == "__main__":
    df_train = pd.read_csv(config.TRAINING_FILE_FOLDS)
    df_train = df_train.drop(axis=1, columns=["id", "kfold"]).reset_index(drop=True)

    df_test = pd.read_csv(config.TEST_FILE_FOLDS)

    for model_name in model_dispatcher.model_names:
        model = model_dispatcher.models[model_name]
        train_model(df_train, model)
        predicted = test_model(df_test, model)
        save_model(model, f"{model_name}_FULL")

        to_save = pd.concat(axis=1, objs=[df_test, pd.DataFrame(data=predicted, columns=["label"])]).loc[:, ["id", "label"]].reset_index(drop=True)
        to_save = to_save.rename(columns={"id": "PassengerId", "label": "Transported"})
        to_save["Transported"] = to_save["Transported"].astype(bool)

        to_save.to_csv(config.OUTPUT_FOLDER + model_name + ".csv", index=False)
        
        print(f"{model_name} trained and saved")