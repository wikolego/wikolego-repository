import config

import pandas as pd
from sklearn import model_selection
# from sklearn import 

# Function generating folds
def generateFolds(df: pd.DataFrame):
    df["kfold"] = -1
    kf = model_selection.StratifiedKFold(n_splits=config.NO_FOLDS)
    for index, (a, b) in enumerate(kf.split(X=df, y=df["label"].values)):
        df.loc[b, "kfold"] = index

# Function reading and concating databases (not tested)
def readAndConcatDatabases(sort: bool):
    df1 = pd.read_csv(config.TRAINING_FILE)
    df2 = pd.read_csv(config.TEST_FILE)
    df2["label"] = False
    return pd.concat([df1, df2], sort=sort)

# Basic begin steps
df = pd.read_csv(config.TRAINING_FILE)

df = df.rename(columns={"PassengerId": "id", "Transported": "label"})
df = df.drop(axis=1, columns=["Name"])

# Editing Cabin column
df[["Cabin_1", "Cabin_2", "Cabin_3"]] = df["Cabin"].str.split("/", expand=True)
df = pd.get_dummies(df, columns=["Cabin_1", "Cabin_3"])
# df["Cabin_3"] = df["Cabin_3"].replace({"P": 0, "S": 1})
df = df.drop(axis=1, columns=["Cabin"])

# Editing id column and filling empty HomePlanet
df[["id_1", "id_2"]] = df["id"].str.split("_", expand=True).astype(int)

groupsDestinations = {}

for row in df.loc[:,["HomePlanet", "id_1"]].itertuples(index=False):
    planet = row.HomePlanet
    groupId = row.id_1

    if pd.isna(planet) == True:
        continue

    if groupsDestinations.__contains__(groupId) == False:
        groupsDestinations[groupId] = planet
    # elif groupsDestinations[groupId] != planet:
    #     print("ERROR")
    #     break

df.loc[pd.isna(df["HomePlanet"]) & df["id_1"].isin(groupsDestinations), "HomePlanet"] = df["id_1"].map(groupsDestinations)
df.loc[pd.isna(df["HomePlanet"]) & (df["id_1"].isin(groupsDestinations) == False), "HomePlanet"] = "NULL"

df = df.drop(axis=1, columns=["id_1", "id_2"])

# Making hot encoding
df = pd.get_dummies(df, columns=["Destination", "HomePlanet"])

# Filling empty values
df = df.fillna("-1")

# Changing all boolean values to integer values
df = df.replace({False: 0, True: 1})

# Generating folds
generateFolds(df)

# Exporting modified data to csv 
df.to_csv(config.TRAINING_FILE_FOLDS, index=False)