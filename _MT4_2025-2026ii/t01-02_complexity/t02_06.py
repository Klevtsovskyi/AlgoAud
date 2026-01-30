def a(n):
    return n * (n + 1) // 2  # O(1)


def b(n, a):
    return (a**(n + 1) - 1) / (a - 1)  # O(log(n))


def c(a):
    return 1 / (1 - a)  # O(1)

