
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
    pivot = array[a + (b - a) // 2]
    # print(f"Sorting: {array[a: b + 1]}", pivot)
    left = a
    right = b
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

    # print(f"Split: {array[a: right + 1]} {array[right + 1: b + 1]}")
    _sort(array, a, right)
    _sort(array, right + 1, b)
    # print(f"Sorted: {array[a: b + 1]}")

if __name__ == '__main__':
    arr = [6, 10, -2, 4, -15, 15, 5, 1, 3]
    print(arr)
    sort(arr)
    print(arr)
