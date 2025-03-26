from sklearn import ensemble
from sklearn import tree

model_names = ["decision_tree_gini", "decision_tree_entropy", "rf"]

models = {
    "decision_tree_gini": tree.DecisionTreeClassifier(
        criterion="gini"
    ),
    "decision_tree_entropy": tree.DecisionTreeClassifier(
        criterion="entropy"
    ),
    "rf": ensemble.RandomForestClassifier(),
}