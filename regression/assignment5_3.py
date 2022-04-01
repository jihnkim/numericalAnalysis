"""
2. 임의점 10 points  (x,y)를 정해서, 최적의 polyfit 를 보이시오. (40점)
"""
# 패키지 임포트
import numpy as np
import matplotlib.pyplot as plt

# 데이터 설정
np.random.seed(201612056)
x_d = np.arange(0, 11)
y_d = np.random.random(len(x_d))

DEGREE = 12

# 시각화
plt.figure(figsize=(16,9))
for i in range(1, DEGREE + 1):
    y_hat = np.polyfit(x_d, y_d, i)
    plt.subplot(3, 4, i)
    plt.plot(x_d, y_d, 'o')

    plt.plot(x_d, np.polyval(y_hat, x_d), 'r')
    plt.title(f'Polynomial order {i}')

plt.tight_layout()
plt.savefig('regression/5_3.png')
plt.show()

# 고차항이 될수록(매개변수가 늘어날수록) 당연하게도 실측값과 근사한 그래프가
# 만들어진다. 
# 즉, 10개의 입력데이터가 있으니 10차 이상의 다항회귀선은 실측값과 동일한 선을
# 그릴 수 있다. 
# 하지만 최적의 polyfit이라고는 단정할 수 없다. 
# 현 상황에서 최적의 회귀선은 10차 이상의 방정식이지만
# 추후 외삽을 고려한 회귀선을 만든다면 최적의 회귀선이 아닐 수 있다.(과적합)