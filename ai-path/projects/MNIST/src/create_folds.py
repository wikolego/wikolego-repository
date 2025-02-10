import config

import pandas as pd
from sklearn import model_selection

def change(data: pd.DataFrame):
    data['kfold'] = -1

    # print(data)
    # print(data.columns)
    
    kf = model_selection.StratifiedKFold(n_splits=2)

    out = data['out'].values
    print(out)

    # for fold, (trn_, val_) in enumerate(kf.split(X=df)):
    #     df.loc[val_, 'kfold'] = fold

    for index, (trn_, val_) in enumerate(kf.split(X=df, y=out)):
        data.loc[val_, 'kfold'] = index
        # print(trn_, val_)
    
    # print(kf)
    # print(data)

df = pd.read_csv(config.TRAINING_FILE_TEST_IN)
print(df)
change(df)
df.to_csv(config.TRAINING_FILE_TEST_OUT, index=False)