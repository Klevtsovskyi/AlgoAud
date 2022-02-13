"""
Реалізуйте алгоритм сортування злиттям.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """

    def _sort(l, r):
        if l >= r:
            return

        m = l + (r - l) // 2

        _sort(l, m)
        _sort(m + 1, r)

        left_piece = array[l: m + 1]
        i = 0
        j = m + 1
        k = l
        while i < len(left_piece) and j <= r:
            if left_piece[i] < array[j]:
                array[k] = left_piece[i]
                i += 1
            else:
                array[k] = array[j]
                j += 1
            k += 1

        while i < len(left_piece):
            array[k] = left_piece[i]
            i += 1
            k += 1

    _sort(0, len(array) - 1)


if __name__ == '__main__':
    arr = [23, 24, 10, 9, 8, 45, 42, 90, 85, 1, 5, 6]
    sort(arr)
    # 10
