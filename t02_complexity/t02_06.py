def A(n):
    return n * (n + 1) / 2


def B(n, a):  # O(log(n))
    return (1 - a**(n + 1)) / (1 - a)


def C(n, a):
    return 1 / (1 - a)

