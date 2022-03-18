# 이분법 파이썬 코드 구현

def bisection(f, a, b, MAX_ITER):

    # 해당 구간 내 실근 존재 유무 확인
    if f(a) * f(b) >= 0:
        print('No Root in this equation')
        return [], []

    # 최소값 최대값 최대 제한 횟수 설정
    xl = a
    xu = b
    iter_limit = MAX_ITER

    # 최대 제한 횟수까지 loop를 돌며 실근 탐색
    while True:
        # 횟수가 모두 소모되면 loop 종료
        if iter_limit == 0:
            return (xl + xu) / 2, MAX_ITER - iter_limit

        iter_limit -= 1

        # 중간값 설정
        mid = (xl + xu) / 2

        # 최소값과 중간값의 해를 곱했을 때 음수인 경우(해당 구간에 실근이 있다)
        if f(xl) * f(mid) < 0:
            xu = mid

        # 최소값과 중간값의 해를 곱했을 때 양수인 경우(해당 구간에 실근이 없다)
        if f(xl) * f(mid) > 0:
            xl = mid

        # 중간값의 해가 0 인경우 (정확한 근을 구함)
        if f(mid) == 0:
            print('Exact Root')
            return mid, MAX_ITER - iter_limit

if __name__ == "__main__":
    f = lambda x: x**2 - x - 1
    f2 = lambda x: (2*x - 1) * (x - 3)
    root, cnt = bisection(f, 1, 2, 25)
    print(root, cnt)
