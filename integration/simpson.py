import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

simp = (h/3) * (f[0] + 2 * sum(f[:n-2:2]) + 4 * sum(f[1:n-1:2]) + f[n-1])
er_simp = 2 - simp

print(er_simp)