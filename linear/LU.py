import numpy as np

u = np.array([[4, 3, -5],
[0, -2.5, 2.5],
[0, 0, 12]])

l = np.array([[1, 0, 0],
[-0.5, 1, 0],
[2, -0.8, 1]])

# print('LU = ', np.dot(l, u))
# print('cross', np.cross(l, u))

# 연립방정식 해 구하기
A = np.array([[4, 3, 5],
[-2, -4, 5], 
[8, 8, 0]])

y = np.array([[2], [5], [-3]])

x = np.linalg.solve(A, y)
print(x)
print(y)

# scipy 패키지 이용
from scipy.linalg import lu

P, L, U = lu(A)

print('P:\n', P)
print('L:\n', L)
print('U:\n', U)
print('LU:\n', np.dot(L, U))