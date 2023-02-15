def a(n):
    return n * (n + 1) / 2  # O(1)


def b(a, n):
    return (1 - a**(n + 1)) / (1 - a)  # log(n)


def c(a, n):
    return 1 / (1 - a)  # O(1)
