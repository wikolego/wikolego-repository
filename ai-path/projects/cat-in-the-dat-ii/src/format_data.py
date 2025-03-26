import config

import pandas as pd
from sklearn import model_selection
from sklearn import preprocessing

def changeByOneHotEncoder(dt: pd.DataFrame, columns):
    ohe = preprocessing.OneHotEncoder()
    ohe.fit(dt.loc[:, columns])
    new_test_data = ohe.transform(dt.loc[:, columns]).toarray()
    # pd.concat(axis=1, )
    print(new_test_data)

def transformColumnToIntValues(dt: pd.DataFrame, column: str):
    lbl_enc = preprocessing.LabelEncoder()
    temp_values = dt[column].values.astype(str)
    # print(temp_values)
    dt[column] = lbl_enc.fit_transform(temp_values)

    # print(dt[column])
    # print(dt[column].value_counts())

def addNoneAndRare(dt: pd.DataFrame, column: str, cnt: int):
    # dt[column] = dt[column].fillna("NONE")
    dt.loc[dt.value_counts(column)[dt[column]].values < cnt, column] = "RARE"


df = pd.read_csv(config.TRAINING_FILE)
df = df.rename(columns={'target': 'label'})
df = df.fillna("NONE")

columns = [col for col in df.columns if col not in ("label", "id")]
df.loc[:, columns].fillna()

# print(columns)

# addNoneAndRare(df, "ord_4", 2000)

# test(df, ["ord_1", "ord_2", "ord_3"])
changeToOneHotEncoder(df, ["nom_0"])

# print(df)

# df.to_csv(config.TRAINING_FILE_FOLDS, index=False)