# 리만법 은 꼭 알아두자
import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

# 리만 left
ri = h * sum(f[:n-1])
er_ri = 2 - ri

print(er_ri)

# 리만 right
ri2 = h * sum(f[1::])
er_ri2 = 2 - ri2

print(er_ri2)

# 리만 평균
ri3 = h * sum(np.sin((x[:n-1] + x[1:]) / 2))
er_ri3 = 2 - ri3

print(er_ri3)