from turtle import color
from matplotlib import scale
import numpy as np
from numpy.linalg import eig

a = np.array([
    [0, 2],
    [2, 3]
])

w, v = eig(a)

print('고유 값 : ', w)
print('고유 벡터 : ', v)

###########
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

def plot_vect(x, b, xlim, ylim):
    plt.figure(figsize=(10, 6))
    plt.quiver(0, 0, x[0], x[1], color='k', angles='xy', scale_units='xy', scale=1, label='org')
    plt.quiver(0, 0, b[0], b[1], color='g', angles='xy', scale_units='xy', scale=1, label='trs')
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    plt.show()

a = np.array([
    [2, 0],
    [0, 1]
])

x = np.array([
    [1],
    [1]
])

b = np.dot(a, x)

plot_vect(x, b, (0, 3), (0, 2))

