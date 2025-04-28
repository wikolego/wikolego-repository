# Import required libraries
import pandas as pd
from sklearn import model_selection

import config

# Load MNIST data
df = pd.read_csv(config.BASIC_DATA_PATH)

# If needed, randomize data
if config.RANDOMIZE_DATA == True:
    df = df.sample(frac=1).reset_index(drop=True)
    df["id"] = df.index

# Make k-folds
folds_model = model_selection.StratifiedKFold(n_splits=config.FOLDS_CNT)

for index, (rest, selected) in enumerate(folds_model.split(X=df, y=df["label"])):
    # print(f"{x}. {fir} - {sec}")
    # print(len(fir), len(sec))
    df.loc[selected, "kfold"] = index

# save MNIST data
df.to_csv(config.NEW_DATA_PATH, index=False)