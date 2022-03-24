import numpy as np

vec_row = np.array([[1, -5, 3, 2, 4]])
vec_col = np.array([
    [1],
    [2],
    [3],
    [4],
])

# print(vec_row.shape)
# print(vec_col.shape)

tmp = np.array([[2, 3, 4],
[4, 6, 7],
[8, 9, 0]])

# print(tmp)

#####
import matplotlib.pyplot as plt

p = lambda x: x**3 - x**2 - 1
x = np.linspace(-100, 100, 100)

plt.plot(x , p(x), color='blue', label='eq 1')
plt.legend()

plt.show()