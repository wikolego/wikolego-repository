import config

import pandas as pd
from sklearn import model_selection

df = pd.read_csv(config.TRAINING_FILE)

print(df)

df = df.drop(axis=1, labels=['PassengerId', 'Name', 'Ticket', 'Cabin', 'Age']) # dropping columns
df = df[df['Fare'].isna() == False]
df.reset_index(drop=True, inplace=True)

# df = df.drop(axis=0, index=df.) # dropping rows

# print(df)

print(df.isnull().sum())

df['kfold'] = -1

kf = model_selection.StratifiedKFold(n_splits=config.NO_FOLDS, shuffle=True)
label = df['Label'].values

for index, (trn_, val_) in enumerate(kf.split(X=df, y=label)):
    df.loc[val_, 'kfold'] = index

df.Sex = df.Sex.map({"male": 0, "female": 1})

df.Embarked = df.Embarked.map({"C": 0, "Q": 1, "S": 2})

print(df[df['Embarked'] == "C"])

# print(df.isnull().sum())

df.to_csv(config.TRAINING_FILE_FOLDS, index=False)

# print(df)