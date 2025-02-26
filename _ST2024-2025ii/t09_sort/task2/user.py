
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
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a + 1) // 2]
    left = a
    right = b
    # print(array[a: b + 1], a, b, "pivot:", pivot)
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
    _quick_sort(array, a, left - 1)
    _quick_sort(array, left, b)
    # print("Sorted:", array[a: b + 1])


# [6, 7] <- 0, 1
# pivot = 6
# left = 0, right = 0
#
# [6] <- 0
# [7] <- 1

# pivot = 7
# left = 1, right = 1
#
# [6, 7] <- 0, 1
# [] <- 2, 1


if __name__ == "__main__":
    arr = [-1, 7, 1, 19, 5, 10, 9, 17, 23]
    print(arr)
    sort(arr)
    print(arr)
