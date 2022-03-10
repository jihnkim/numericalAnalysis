from math import *

# 나는 수치해석이 좋습니다 출력
s = "나는 수치해석이 좋습니다"

print(s)

# 점 (3, 4)와 (5, 9)의 거리와 기울기 계산
x1, x2, y1, y2 = 3, 5, 4, 9
d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
a = (y2 - y1) / (x2 - x1)

print('두 점 사이의 거리 : ', d, '\n두 점 사이의 기울기 : ', a)

# 자유주제
# 자동 판매기 시뮬레이션

cost = 10000
salePrice = 7000

change = cost - salePrice

coin500cnt = change // 500
coin100cnt = (change - coin500cnt * 500) // 100

print(f'500원 동전 수 : {coin500cnt}', f'\n100원 동전 수 : {coin100cnt}' )