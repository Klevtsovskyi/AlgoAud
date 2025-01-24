import math


def a(n):
    s = 0
    for i in range(n):
        s = math.sqrt(2 + s)  # O(n)
    return s


def b(n, x):
    s = 1
    a = x * x
    for i in range(n):
        s += a
        a *= a
    return s


def c(n):
    p = 1
    for i in range(1, n + 1):
        p *= (1 + 1.0 / i**i)  # O(n log(n))
    return p


def d(n, x):
    sinx = math.sin(x)
    a = 1
    s = 1
    for i in range(n):
        a *= sinx
        s += a
    return s
