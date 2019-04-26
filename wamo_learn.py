from sklearn.neural_network import MLPClassifier as Classifier
import pandas as pd

df = pd.read_csv('training_data.csv')
df = list(df.T.values[3])
print(df)
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = Classifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)

print(clf.predict([[2., 2.], [-1., -2.]]))
