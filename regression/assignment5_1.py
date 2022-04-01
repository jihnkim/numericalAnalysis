"""
1. 2개의 함수를 optimize.curve.fit 코딩을 사용하여 회귀 plot 하시오. (60점)
 5주차 강의안에  과제 내용 참고. 
"""
# 패키지 임포트
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 구간과 함수 선언
x = np.linspace(0, 1, 1000)
y = 2 * np.exp(-0.5 * x) + 0.25 * np.random.random(len(x))

# 회귀식 정의
def y_hat(x, a, b):
    return a * x + b

def y_hat2(x, a, b):
    return a * np.exp(b * x)

# scipy 패키지 메서드를 통해 회귀식 계수 추정
alpha = curve_fit(y_hat, xdata=x, ydata=y)[0]
alpha2, beta = curve_fit(y_hat2, xdata=x, ydata=y)[0]

# 구한 계수값으로 회귀선 시각화
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0] * x + alpha[1], 'r', label='Linear eq')
plt.plot(x, alpha2 * np.exp(beta*x), 'y', label='exp eq')
plt.legend()
plt.grid()
plt.savefig('regression/5_1.png')
plt.show()
