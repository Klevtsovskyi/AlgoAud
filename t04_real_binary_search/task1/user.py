"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""

eps = 1e-10


def _argument(l, r, m, f, eps):
    return abs(r - l) > eps


def _value(l, r, m, f, eps):
    return abs(f(r) - f(l)) > eps


def _neighbourhood(l, r, m, f, eps):
    return l != m and r != m


condition = _neighbourhood


def solve(f, c, a, b):
    """ Для неспадної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    l = a
    r = b
    m = (l + r) / 2
    while condition(l, r, m, f, eps):
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2
    return l


def solve_decreasing(f, c, a, b):
    """ Для незростаючої на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    l = a
    r = b
    m = (l + r) / 2
    while condition(l, r, m, f, eps):
        if f(m) > c:
            l = m
        else:
            r = m
        m = (l + r) / 2
    return l
