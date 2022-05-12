# 사다리꼴 적분
import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

trap = (h/2) * (f[0] + 2 * sum(f[1:n-1]) + f[n-1])
er_trap = 2 - trap
print(trap)
print(er_trap)

# with package
from scipy.integrate import trapz

trap2 = trapz(f, x)
print(trap2)