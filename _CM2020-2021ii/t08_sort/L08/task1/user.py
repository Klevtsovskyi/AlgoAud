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
    if len(array) > 1:
        m = len(array) // 2
        left_piece = array[:m]
        right_piece = array[m:]

        sort(left_piece)
        sort(right_piece)

        i = j = k = 0
        while i < len(left_piece) and j < len(right_piece):
            if left_piece[i] < right_piece[j]:
                array[k] = left_piece[i]
                i += 1
            else:
                array[k] = right_piece[j]
                j += 1
            k += 1

        while i < len(left_piece):
            array[k] = left_piece[i]
            i += 1
            k += 1

        while j < len(right_piece):
            array[k] = right_piece[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [23, 24, 10, 9, 8, 45, 42, 90, 85, 1, 5, 6]
    sort(arr)
    # 12
