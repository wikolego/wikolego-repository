from sklearn import ensemble
from sklearn import tree
from sklearn import linear_model
import xgboost as xgb

model_names = ["decision_tree_gini", "decision_tree_entropy", "random_forest", "logistic_regression", "xgboost"]

models = {
    "decision_tree_gini": tree.DecisionTreeClassifier(
        criterion="gini"
    ),
    "decision_tree_entropy": tree.DecisionTreeClassifier(
        criterion="entropy"
    ),
    "random_forest": ensemble.RandomForestClassifier(),
    "logistic_regression": linear_model.LogisticRegression(
        max_iter=1600
    ),
    "xgboost": xgb.XGBClassifier(
        n_jobs=-1,
        max_depth=7,
        n_estimators=200
    )
}