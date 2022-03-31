import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.linspace(0, 1, 101)
# 이때 y는 실측값(관측값)
y = 1 + x + x * np.random.random(len(x))

# plt.plot(x, y, 'ko')
# plt.show()

# 추정선
def y_hat(x, a, b):
    return a * x + b

# optimize curve_fit은 회귀선의 계수 뿐만이 아니라 잔차(d)도 표현하기 때문에
# 0번째 인덱스인 계수만 가져온다.
alpha = optimize.curve_fit(y_hat, xdata=x, ydata=y)[0]
print(alpha)

# 구한 계수값으로 회귀선 그려보기
plt.figure(figsize=(10, 8))
# plt.plot(x, y, 'b.')
# plt.plot(x, alpha[0] * x + alpha[1], 'r')
# plt.show()

# 비선형 연습
x = np.linspace(0, 10, 101)
y = 0.1 * np.exp(0.3 * x) + 0.1 * np.random.random(len(x))

def y_hat2(x, a, b):
    return a * np.exp(b * x)

alpha, beta = optimize.curve_fit(y_hat2, xdata=x, ydata=y)[0]
print(f'alpha={alpha}, beta={beta}')

# 계수 plot 찍어보기
# plt.plot(x, y, 'b.')
# plt.plot(x, alpha * np.exp(beta*x), 'r')
# plt.show()

# 다항식 회귀(차수를 올려가며 비교)
x_d = np.arange(0, 9)
y_d = np.array([0, 0.8, 0.9, 0.1, -0.6, -0.8, -1, -0.9, -0.4])

plt.figure(figsize=(12,8))

for i in range(1, 7):
    y_est = np.polyfit(x_d, y_d, i)
    plt.subplot(2, 3, i)
    plt.plot(x_d, y_d, 'o')

    plt.plot(x_d, np.polyval(y_est, x_d))
    plt.title(f'Polynomial order {i}')

plt.tight_layout()
plt.show()