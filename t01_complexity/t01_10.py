

from math import sqrt


def a(n):
    s = 0
    for i in range(n):
        s = sqrt(s + 2)
    return s


def b(x, n):
    s = 0
    p = x*x
    for i in range(1, n):
        s += p
        p *= p
    return s + 1
