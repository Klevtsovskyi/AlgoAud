"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""


def argument(f, m, l, r, eps):
    return r - l > eps


def value(f, m, l, r, eps):
    return abs(f(r) - f(l)) > eps


def neighbours(f, m, l, r, eps):
    return l != m and r != m


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
    m = (a + b) / 2.0
    while condition(f, m, l, r, eps):
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
    m = (a + b) / 2.0
    while condition(f, m, l, r, eps):
        count += 1
        if f(m) > c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(count)
    return m
