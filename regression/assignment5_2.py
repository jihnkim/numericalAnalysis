"""
1. 2개의 함수를 optimize.curve.fit 코딩을 사용하여 회귀 plot 하시오. (60점)
 5주차 강의안에  과제 내용 참고. 
"""
# 패키지 임포트
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 구간과 함수 선언
x = np.linspace(0, 2 * np.pi, 1000)
y = 3 * np.sin(x) - 2 * np.cos(x) + np.random.random(len(x))

# 회귀식 기본형 정의
def y_hat(x, a, b):
    return a * x + b

def y_hat2(x, a, b):
    return a * np.exp(b * x)

def y_hat3(x, a, b):
    return a * np.sin(x) - np.cos(x) + b

# 다항식 회귀
# 4차식 fitting 시 회귀선이 잘 나오긴 합니다.
y_hat4 = np.polyfit(x, y, 4)

# scipy 패키지 메서드를 통해 회귀식 계수 추정
alpha, beta = curve_fit(y_hat, xdata=x, ydata=y)[0]
alpha2, beta2 = curve_fit(y_hat2, xdata=x, ydata=y)[0]
alpha3, beta3 = curve_fit(y_hat, xdata=x, ydata=y)[0]

# 구한 계수값으로 회귀선 시각화
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b.')
plt.plot(x, alpha * x + beta, 'r', label='Linear eq')
plt.plot(x, alpha2 * np.exp(beta2*x), 'y', label='exp eq')
plt.plot(x, alpha3 * np.sin(x) - np.cos(x) + beta3, 'g', label='cir eq')
plt.plot(x, np.polyval(y_hat4, x), 'w', label='poly')
plt.legend()
plt.grid()
plt.savefig('regression/5_2.png')
plt.show()