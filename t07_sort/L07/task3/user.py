
"""
Реалізуйте алгоритм сортування вибором.
"""

N = 10000    # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for i in range(n, 1, -1):
        maxpos = 0
        for j in range(1, i):
            if array[maxpos] < array[j]:
                maxpos = j
        array[i - 1], array[maxpos] = array[maxpos], array[i - 1]
