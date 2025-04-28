# Import required libraries
import pandas as pd
from sklearn import metrics

import config
import model_dispatcher

# Main function
if __name__ == "__main__":

    # Load and initialize data
    df = pd.read_csv(config.NEW_DATA_PATH)
    df.drop(columns=["id"])

    # Loop through all models
    for model_name in model_dispatcher.model_names:
        model = model_dispatcher.models[model_name]

        # Test single model on different folds
        for fold in range(config.FOLDS_CNT):
            
            # Initialize train dataframe and test dataframe
            df_train = df.loc[df["kfold"] != fold, :]
            df_test = df.loc[df["kfold"] == fold, :]

            df_train = df_train.drop(columns=["kfold"])
            df_test = df_test.drop(columns=["kfold"])

            x_train = df_train.drop(columns=["label"]).values
            y_train = df_train.loc[:, "label"].values
            
            x_test = df_test.drop(columns=["label"]).values
            y_test = df_test.loc[:, "label"].values

            # Fit model
            model.fit(x_train, y_train)

            # Test model and get results
            predicted_data = model.predict(x_test)

            # Calculate and print accuracy score
            accuracy = metrics.accuracy_score(
                y_true=y_test,
                y_pred=predicted_data
            )
            print(f"{model_name}: {fold} - {accuracy}")