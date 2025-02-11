"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""

def argument(l, r, m, f, eps):
    return r - l > eps


def value(l, r, m, f, eps):
    return abs(f(r) - f(l)) > eps


def neighbours(l ,r, m, f, eps):
    return m != l and m != r


condition = neighbours


def solve(f, c, a, b):
    """ Для неспадної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    count = 0
    eps = 1e-10
    l = a
    r = b
    m = (l + r) / 2.0
    while condition(l, r, m, f, eps):
        count += 1
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(count)
    return m


def solve_decreasing(f, c, a, b):
    """ Для незростаючої на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    count = 0
    eps = 1e-10
    l = a
    r = b
    m = (l + r) / 2.0
    while condition(l, r, m, f, eps):
        count += 1
        if f(m) > c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(count)
    return m
