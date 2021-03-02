"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""


def _condition_argument(l, r, m, eps, f):
    return abs(r - l) >= eps


def _condition_value(l, r, m, eps, f):
    return abs(f(r) - f(l)) >= eps


def _condition_neighbourhood(l, r, m, eps, f):
    return l != m and r != m


CONDITION = _condition_neighbourhood


def solve(f, c, a, b):
    """ Для неспадної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    eps = 1e-10

    l = a
    r = b
    m = l + (r - l) / 2
    while CONDITION(l, r, m, eps, f):
        if f(m) < c:
            l = m
        else:
            r = m
        m = l + (r - l) / 2
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
    eps = 1e-10

    l = a
    r = b
    m = l + (r - l) / 2
    while CONDITION(l, r, m, eps, f):
        if f(m) > c:
            l = m
        else:
            r = m
        m = l + (r - l) / 2
    return m
