
def newton(f, df, x0, e, max_iter):

    xn = x0

    for n in range(max_iter):
        fxn = f(xn)

        if abs(fxn) < e:
            print(f'{n} 번째 에서 root 구함')
            return xn

        dfxn = df(xn)

        if dfxn == 0:
            print('미분값이 0, 해를 구할 수 없음')
            return

        xn = xn - fxn / dfxn

    print('제한 횟수 초과')
    return

if __name__ == '__main__':
    p = lambda x: x**3 - x**2 - 1
    dp = lambda x: 3 * x**2 - 2 * x

    approx = newton(p, dp, 1, 1e-10, 10)
    print(approx)