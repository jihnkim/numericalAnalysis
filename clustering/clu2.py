from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sp
import seaborn as sns
import pandas as pd

data = pd.read_csv('Mall_Customers.csv')

print(data.head())

from sklearn.cluster import KMeans

x = data.iloc[:, [3, 4]]
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

kmeans = KMeans(n_clusters=5, init="k-means++", max_iter=30, n_init=10, random_state=0)

y = kmeans.fit_predict(x)
x = np.array(x)

fig = plt.figure(figsize=(25, 10))
plt.scatter(x[y == 0, 0], x[y == 0, 1], s = 100, c= 'red', label = 'C 1')
plt.scatter(x[y == 1, 0], x[y == 1, 1], s = 100, c= 'blue', label = 'C 2')
plt.scatter(x[y == 2, 0], x[y == 2, 1], s = 100, c= 'green', label = 'C 3')
plt.scatter(x[y == 3, 0], x[y == 3, 1], s = 100, c= 'cyan', label = 'C 4')
plt.scatter(x[y == 4, 0], x[y == 4, 1], s = 100, c= 'magenta', label = 'C 5')

plt.legend()
plt.show()