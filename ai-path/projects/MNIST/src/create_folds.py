import config

import pandas as pd
from sklearn import model_selection

def change(df: pd.DataFrame):
    df['kfold'] = -1
    
    kf = model_selection.StratifiedKFold(n_splits=config.NO_FOLDS, shuffle=True)
    label = df['label'].values

    for index, (trn_, val_) in enumerate(kf.split(X=df, y=label)):
        df.loc[val_, 'kfold'] = index

df = pd.read_csv(config.TRAINING_FILE)

print(df)
change(df)

df.to_csv(config.TRAINING_FILE_FOLDS, index=False)
