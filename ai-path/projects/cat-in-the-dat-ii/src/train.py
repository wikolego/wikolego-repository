import config

import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing

def func(df: pd.DataFrame, fold: int):

    df_train = df[df["kfold"] != fold]
    df_test = df[df["kfold"] == fold]

    print(df_train.count())
    print(df_test.count())


df = pd.read_csv(config.TRAINING_FILE_FOLDS)

func(df, 0)