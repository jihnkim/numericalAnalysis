def myAdder(a, b, c):
    c = a + b + c
    return c

f = lambda x: x**2

if __name__ == '__main__':
    print(myAdder(1, 2, 3))
    print(f(2))