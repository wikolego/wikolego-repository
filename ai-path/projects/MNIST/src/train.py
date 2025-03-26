import os
import config
import joblib
import pandas as pd
import model_dispatcher
from sklearn import metrics
from sklearn import tree

def run(fold, model, model_name):
    # read the training data with folds
    df = pd.read_csv(config.TRAINING_FILE_FOLDS)

    # training data is where kfold is not equal to provided fold
    # also, note that we reset the index
    df_train = df[df.kfold != fold].reset_index(drop=True)

    # validation data is where kfold is equal to provided fold
    df_valid = df[df.kfold == fold].reset_index(drop=True)

    # drop the label column from dataframe and convert it to
    # a numpy array by using .values.
    # target is label column in the dataframe
    x_train = df_train.drop("label", axis=1).values
    y_train = df_train.label.values
    
    # similarly, for validation, we have
    x_valid = df_valid.drop("label", axis=1).values
    y_valid = df_valid.label.values
    
    # initialize simple decision tree classifier from sklearn
    clf = model

    # fit the model on training data
    clf.fit(x_train, y_train)
    
    # create predictions for validation samples
    preds = clf.predict(x_valid)
    
    # calculate & print accuracy
    accuracy = metrics.accuracy_score(y_valid, preds)

    print(f"Model={model_name}, Fold={fold}, Accuracy={accuracy}")
    
    joblib.dump(
        clf,
        os.path.join(config.MODEL_OUTPUT, f"{model_name}_{fold}.bin")
    )

if __name__ == "__main__":
    for model_name in model_dispatcher.model_names:
        for i in range(config.NO_FOLDS):
            run(fold=i, model=model_dispatcher.models[model_name], model_name=model_name)
