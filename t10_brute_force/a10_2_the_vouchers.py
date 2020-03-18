''' a10_2_the_vouchers.py

https://www.e-olymp.com/uk/problems/6

Туристична фірма не встигла через великі морози продати n (n < 15)
путівок на гірськолижні бази, термін дії яких вже настав. Щоб зменшити
втрати, було вирішено з 1 лютого всі такі путівки, яким
залишилось dk (dk ≤ 30) днів, продавати за номінальною вартістю –
по ck (ck ≤ 100) грн за день лише за ті дні, які залишились з дня
продажу (k = 1..n).

На яку найбільшу суму можна реалізувати ці путівки, якщо кожного
дня продавати по одній путівці?

Вхідні дані:
Перший рядок містить кількість путівок n. Кожний з наступних n
рядків містить два числа – кількість днів dk і вартість дня ck.

Вихідні дані:
Найбільша сума прибутку.
'''

def the_vouchers(lst):
    '''
    :param lst: впорядкований за зростанням список путівок
                кортежів (кількість днів, ціна за день)
    :return: максимальний прибуток
    '''

    max_income = 0

    def _vou(lst, income, m):
        '''
        :param lst: впорядкований за зростанням підсписок путівок
                    кортежів (кількість днів, ціна за день)
        :param income: поточний прибуток
        :param m: поточний день продажу
        '''
        nonlocal max_income

        while lst and lst[0][0] < m:
            del lst[0]
        if not lst and income > max_income:
            max_income = income
            return

        for i in range(len(lst)):
            sub_lst = lst[:]
            v = sub_lst.pop(i)
            sub_income = income + v[1] * (v[0] - m)
            _vou(sub_lst, sub_income, m + 1)

    _vou(lst, 0, 0)
    return max_income

if __name__ == '__main__':
    data = [[(1, 46), (2, 37), (3, 45), (4, 30),],
            [(1, 31), (1, 32), (4, 12), (5, 19),],
            [(4, 25), (4, 26),],
            [(1, 25), (3, 50), (3, 54), (4, 33), (6, 43), (8, 17), (10, 13)],]
    for t in data:
        print(the_vouchers(t))
    '''
    with open('input.txt') as f:
        from bisect import insort
        n = int(f.readline())
        lst = []
        for _ in range(n):
            insort(lst, tuple(map(int, f.readline().split())))

    with open('output.txt', 'w') as f:
        print(the_vouchers(lst), file=f)
    '''
