import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn import svm, datasets
from sklearn.metrics import classification_report

iris = datasets.load_iris()

print(iris.feature_names)
print(set(iris.target))
print(iris.data)

X = iris.data[:, [0, 2]]
y = iris.target

clf = svm.SVC(kernel='linear')

clf.fit(X, y)

print(clf.predict(X))