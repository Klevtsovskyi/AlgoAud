
"""
Реалізуйте швидкий алгоритм сортування QuickSort.
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
    _sort(array, 0, len(array) - 1)


def _sort(array, a, b):
    if a >= b:
        return
    pivot = array[a + (b - a + 1) // 2]
    left = a
    right = b
    # print(array[a: b + 1], a, b, f"pivot: {pivot}")
    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    # print(array[a: right + 1], array[right + 1: b + 1])
    _sort(array, a, left - 1)
    _sort(array, left, b)


if __name__ == '__main__':
    arr = [9, 1, -1, 20, 19, 10, -5, 13, 7]
    print(arr)
    sort(arr)
    print(arr)
