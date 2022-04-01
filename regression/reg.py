import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.linspace(0, 1, 101)
# 이때 y는 실측값(관측값)
y = 1 + x + x * np.random.random(len(x))

plt.plot(x, y, 'ko')
plt.show()

# 추정선
def y_hat(x, a, b):
    return a * x + b

# optimize curve_fit은 회귀선의 계수 뿐만이 아니라 잔차(d)도 표현하기 때문에
# 0번째 인덱스인 계수만 가져온다.
alpha = optimize.curve_fit(y_hat, xdata=x, ydata=y)[0]
print(alpha)

# 구한 계수값으로 회귀선 그려보기
# plt.figure(figsize=(10, 8))
# plt.plot(x, y, 'b.')
# plt.plot(x, alpha[0] * x + alpha[1], 'r')
# plt.show()
