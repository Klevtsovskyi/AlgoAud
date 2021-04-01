"""
https://www.e-olymp.com/uk/problems/6

Туристична фірма не встигла через великі морози продати n (n < 15)
путівок на гірськолижні бази, термін дії яких вже настав. Щоб зменшити
втрати, було вирішено з 1 лютого всі такі путівки, яким
залишилось d_k (d_k ≤ 30) днів, продавати за номінальною вартістю –
по c_k (c_k ≤ 100) грн за день лише за ті дні, які залишились з дня
продажу (k = 1..n).

На яку найбільшу суму можна реалізувати ці путівки, якщо кожного
дня продавати по одній путівці?

Вхідні дані:
Перший рядок містить кількість путівок n. Кожний з наступних n
рядків містить два числа – кількість днів d_k і вартість дня c_k.

Вихідні дані:
Найбільша сума прибутку.

Вхідні дані #10
4
2 37
3 45
1 46
4 30
Вихідні дані #10
232
"""


def the_vouchers(lst):
    """
    :param lst: впорядкований за зростанням список путівок
                кортежів (кількість днів, ціна за день)
    :return: максимальний прибуток
    """

    max_income = 0  # максимальний прибуток

    def _vou(lst, income, m):
        """
        :param lst: впорядкований за зростанням підсписок путівок
                    кортежів (кількість днів, ціна за день)
        :param income: поточний прибуток
        :param m: поточний день продажу
        """
        nonlocal max_income

        while lst and lst[0][0] < m:
            del lst[0]
        if not lst and income > max_income:
            max_income = income
            return

        for i in range(len(lst)):
            sub_lst = lst[:i] + lst[i + 1:]
            sub_income = income + lst[i][1] * (lst[i][0] - m)
            _vou(sub_lst, sub_income, m + 1)

    _vou(lst, 0, 0)
    return max_income


if __name__ == "__main__":
    with open("input.txt") as inp:
        n = int(inp.readline())
        lst = [
            tuple(map(int, inp.readline().split()))
            for _ in range(n)
        ]
        lst.sort()
    print(the_vouchers(lst))
