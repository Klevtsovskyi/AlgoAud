"""
Проведіть аналіз швидкодії реалізованих алгоритмів сортування
для різних типів та розмірів масивів (не відсортований масив
згенерований випадковим чином, масив відсортований за зростанням,
масив відсортований за спаданням елементів).
"""

N = 10000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for j in range(1, n):
        for i in range(n - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for j in range(1, n):
        _sorted = True
        for i in range(n - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                _sorted = False

        if _sorted:
            return


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for j in range(n - 1):
        maxpos = 0
        for i in range(1, n - j):
            if array[i] > array[maxpos]:
                maxpos = i
        array[i], array[maxpos] = array[maxpos], array[i]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(1, n):
        pos = i
        cur = array[i]
        while pos > 0:
            if array[pos - 1] > cur:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1

        array[pos] = cur


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) <= 1:
        return

    m = len(array) // 2
    left = array[:m]
    right = array[m:]

    # print(f"Splitting: {array} = {left} {right}")
    merge_sort(left)
    merge_sort(right)

    # print(f"Merging: {left} {right}")
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    # print(f"Merged: {array}")


def merge_sort_optimized(array):
    _merge_sort(array, 0, len(array) - 1)


def _merge_sort(array, a, b):
    if a >= b:
        return

    m = a + (b - a) // 2
    # print(f"Splitting: {array[a: b + 1]} = {array[a: m + 1]} {array[m + 1: b + 1]}")
    _merge_sort(array, a, m)
    _merge_sort(array, m + 1, b)

    # print(f"Merging: {array[a: m + 1]} {array[m + 1: b + 1]}")
    left = array[a: m + 1]
    i = 0
    j = m + 1
    k = a
    while i < len(left) and j <= b:
        if left[i] < array[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    # print(f"Merged: {array[a: b + 1]}")


def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    # print(array[a: b + 1], pivot)
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
    _quick_sort(array, a, right)
    # print("Sorted left:", array[a: right + 1])
    _quick_sort(array, right + 1, b)
    # print("Sorted right:", array[right + 1: b + 1])
