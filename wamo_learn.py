from sklearn.neural_network import MLPClassifier as Classifier
import pandas as pd

df = pd.read_csv('training_data.csv')
# df = list(df.T.values[3])
list_of_data = df.close.tolist()
print(list_of_data)
# X = [[85, 86, 86, 87 ... ,88], [1., 1.], [87, 89, 86, 75], ...] n
# y = [0, 1, 0, 1, 1, 0, 0, 1 ... ] n
# clf = Classifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
# clf.fit(X, y)
#
# print(clf.predict([[86, 85, .. ],]))
#
#
# X = [[0,0], [0,1], [1,0], [1,1], [0,0]]
# y = [0, 1, 1, 0, 0]
# fit(X, y)
# predict([[0,1], [1,1]])
# [1, 0]
