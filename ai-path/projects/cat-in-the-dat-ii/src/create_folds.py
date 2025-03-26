import config

import pandas as pd
from sklearn import model_selection

df = pd.read_csv(config.TRAINING_FILE)

df = df.rename(columns={"target": "label"})

df["kfold"] = -1

kf = model_selection.StratifiedKFold(n_splits=config.NO_FOLDS)

for index, (t_, v_) in enumerate(kf.split(X=df, y=df["label"].values)):
    df.loc[v_, "kfold"] = index

df.to_csv(config.TRAINING_FILE_FOLDS, index=False)