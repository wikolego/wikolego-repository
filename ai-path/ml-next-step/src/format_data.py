# Import required libraries
import pandas as pd
from sklearn import model_selection

import config

# Load MNIST data
df = pd.read_csv(config.BASIC_DATA_PATH)

df = df.drop(columns=["id"])

# Initialize kfold column
df["kfold"] = -1

# Make k-folds
folds_model = model_selection.StratifiedKFold(
    n_splits=config.FOLDS_CNT,
    shuffle=config.RANDOMIZE_DATA
)

for fold, (rest, selected) in enumerate(folds_model.split(X=df, y=df["label"])):
    # print(f"{x}. {fir} - {sec}")
    # print(len(fir), len(sec))
    df.loc[selected, "kfold"] = fold

# save MNIST data
df.to_csv(config.NEW_DATA_PATH, index=False)