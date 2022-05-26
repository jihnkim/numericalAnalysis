import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sp
import seaborn as sns
import pandas as pd

from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples=200, centers=4, n_features=2, random_state=1)
points = pd.DataFrame(x, y).reset_index(drop=True)
points.columns = ["x", "y"]
print(points.head())

sns.scatterplot(x="x", y="y", data=points)
# plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)
kmeans.fit(points)

res = points.copy()
res['cluster'] = kmeans.labels_
print(res.head())