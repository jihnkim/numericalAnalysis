import scipy.linalg as la
import numpy as np

A = np.array([
    [0, 1, 1],
    [2, 1, 0],
    [3, 4, 5]
])

u, v = la.eig(A)

print(np.dot(v, np.dot(np.diag(u), la.inv(v))))
print(u)