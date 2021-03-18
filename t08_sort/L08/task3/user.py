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
        sorted = True
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        if sorted:
            return


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n, 1, -1):
        maxpos = 0
        for j in range(1, i):
            if array[maxpos] < array[j]:
                maxpos = j
        array[i - 1], array[maxpos] = array[maxpos], array[i - 1]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n):
        item = array[i]
        while i > 0:
            if array[i - 1] > item:
                array[i] = array[i - 1]
            else:
                break
            i -= 1
        array[i] = item


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) > 1:
        m = len(array) // 2
        left_piece = array[:m]
        right_piece = array[m:]

        merge_sort(left_piece)
        merge_sort(right_piece)

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


def merge_sort_optimized(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
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


def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    def _sort(a, b):
        if a >= b:
            return

        pivot = array[a + (b - a) // 2]
        l = a
        r = b
        while True:
            while array[l] < pivot:
                l += 1
            while array[r] > pivot:
                r -= 1

            if l >= r:
                break

            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

        _sort(a, r)
        _sort(r + 1, b)

    _sort(0, len(array) - 1)
