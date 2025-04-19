from sklearn import tree
from sklearn import ensemble
from sklearn import neural_network

model_names = [
    "decision_tree_gini",
    "decision_tree_entropy",
    "random_forest",
    # "neural_network"
]

models = {
    "decision_tree_gini": tree.DecisionTreeClassifier(
        criterion="gini"
    ),
    "decision_tree_entropy": tree.DecisionTreeClassifier(
        criterion="entropy"
    ),
    "random_forest": ensemble.RandomForestClassifier(),
    "neural_network": neural_network.MLPClassifier()
}