from scipy.interpolate import interp1d, lagrange, CubicSpline
import matplotlib.pyplot as plt


x = [0, 1, 2]
y = [1, 3, 2]

f = interp1d(x, y)
f2 = lagrange(x, y)
f3 = CubicSpline(x, y)

y_hat = f(1.5)
y_hat2 = f2(1.5)
y_hat3 = f3(1.5)

print(y_hat)
print(y_hat2)
print(y_hat3)