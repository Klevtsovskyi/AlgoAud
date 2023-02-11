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
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        _sorted = True
        for i in range(pass_num):
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
            if array[maxpos] < array[i]:
                maxpos = i
        array[maxpos], array[i] = array[i], array[maxpos]


def insertion_sort(array):
    """ Сортування вставкою
    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(1, n):
        cur = array[i]
        pos = i
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
    # print("Splitting:", left, right)
    merge_sort(left)
    merge_sort(right)
    # print("Sorted:", left, right)
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


def _merge_sort(array, a, b):
    # print("Sorting:", array[a: b + 1])
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
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
    # print(pivot)
    # print("Splitting:", array[a: right + 1], array[right + 1: b + 1])
    _merge_sort(array, a, right)
    _merge_sort(array, right + 1, b)


def merge_sort_optimized(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    _merge_sort(array, 0, len(array) - 1)


def _quick_sort(array, a, b):

    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
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

    _quick_sort(array, a, right)
    _quick_sort(array, right + 1, b)


def quick_sort(array):
    """ Швидке сортування
        :param array: Масив (список однотипових елементів)
        :return: None
        """
    _quick_sort(array, 0, len(array) - 1)
