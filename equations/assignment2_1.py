#  1. 
# y = 3 + exp -xsin(6x) and y = 4 + exp(-x)cos(6x) 를 plot 으로 그려보자
# 단 구간은 0 <= x < = 5

# 패키지 임포트
import matplotlib.pyplot as plt
import numpy as np
from math import *

# 함수 정의
def y1(x):
    return 3 + exp(1) + (-1 *(x * sin(6 * x)))

def y2(x):
    return 4 + exp(-1 * x) * cos(6 * x)

# 구간 설정
f1 = np.vectorize(y1)
f2 = np.vectorize(y2)
x = np.linspace(0, 5, 100)


# pyplot 패키지의 메서드를 이용하여 원하는 plot 출력
fig, ax = plt.subplots()

ax.plot(x , f1(x), color='blue', label='eq 1')
ax.plot(x, f2(x), color='red', label='eq 2')

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.legend()
plt.savefig('assignment2_1.pdf')
plt.show()


# trouble shooting
# 1. exp 를 그냥 사용하고 싶으면 e^1 즉 exp(1) 을 이용한다
# 2. 함수에 스칼라값을 전달하여야 하는데 배열이 들어갈 경우 error 발생
# TypeError: only size-1 arrays can be converted to Python scalars
# 이럴 땐 선언한 x 값 자체 요소 하나 하나를 함수에 입력하여 for loop을 돌게함 그럼 해결