

def a(n):
    s = 0  # O(1)
    for i in range(n + 1):  # O(n)
        s += i  # O(n)
    return s  # O(1)


def b(n):
    s = 0  # O(1)
    for i in range(n + 1):  # O(n)
        s += i * i  # O(n)
    return s  # O(1)
# O(n) = O(n^2)


def d(n, a):
    s = 0  # O(1)
    p = 1  # O(1)
    for i in range(n + 1):  # O(n)
        s += p  # O(n)
        p *= a  # O(n)
    return s  # O(1)


def e(n):
    p = 1  # O(1)
    for i in range(1, n + 1):  # O(n)
        p *= 1 / (1 + i)  # O(n)
    return p  # O(1)


def g(n):
    p = 1  # O(1)
    fact = 1  # O(1)
    for i in range(1, n + 1):  # O(n)
        fact *= i  # O(n)
        p *= 1 / (1 + fact)  # O(n)
    return p  # O(1)


def h(n, m):
    p = 1  # O(1)
    for i in range(1, n + 1):  # O(n)
        im = i  # O(n)
        for j in range(m):   # O(nm)
            im *= i  # O(nm)
        p *= 1 / (1 + im)  # O(n)
    return p   # O(1)

