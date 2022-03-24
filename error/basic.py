"""
// 오차의 종류

절대 오차
: 실제값과 근삿값 사이의 절대값 (abs(x - x_hat))

상대 오차
: 계산된 오차를 실제값으로 나눈 뒤 절댓값을 적용 (abs((x - x_hat) / x))

numerical analysis == prediction model

// Linear Interpolation

선형 내삽법
: 두 점을 나타내는 함수로 그 두점을 잇는 직선을 선택

// Linear Regression

선형 회귀법
: 실제 데이터를 가장 잘 근사하는 직선을 구하는 방법이다.
  실제 데이터 값과 직선 상의 추정값의 차이를 제곱하여 모두 더한다. 이를 최소제곱법(least square)이라고 한다.
  실제 데이터 값이 근사하는 직선 상에 하나도 놓이지  않을 수도 있다.

// Polynomial Regression

다항 회귀
: 선형회귀법은 1차 다항식인 직선을 사용하여 방정식을 추정하는 것이다.
  직선의 방정식 대신에 차수가 높은 방정식을 사용하면 데이터와 더 잘 맞는 추정을 할 수 있다.
  매트랩은 같은 방식을 써서 선형회귀법과  다항식회귀법을 수행한다. 두 방법은 다항식의 차수만 차이가 날  뿐이다. 

// diff function

: 미분을 잘 몰라도 diff 함수의 사용법은 쉽게 이해할 수 있다.
  diff 함수는 배열에서 연속하는 두 원소 값의 차이  (이를 차분(difference)이라고 한다.)를 구해준다.

x, y의 관계를 수식으로 표현하는 함수를 알고 있는 경우
x값에 대응하는 y값을 알 수 있으므로 순서쌍 (x, y)을 만들 수 있다.
순서쌍 (x, y)의 값이 많을수록 더욱 정확하게 근사할 수 있다. 


// Numerical Integration, Trapezoid rule

수치 적분에서 사다리꼴 면적 구하기
: 직사각형을 잘라 붙이면 사다리꼴

// 미분 방정식의 수치 해법

상미분 방정식(ordinary differential equation, ODE)의 해를 수치해석기법으로 구해주는 많은 함수가 내장되어 있다.
고계 미분방정식이나 연립방정식은 여러 개의 1계 미분방정식으로 다시 써주어야 한다.

// 수치해석이 필요한 이유

컴퓨터가 처리하기 버거운 수식을 간단하게 표현 가능(모델을 심플하게)
"""