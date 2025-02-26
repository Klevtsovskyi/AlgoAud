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
    if len(array) == 1:
        return
    # print(f"Sorting {array}")
    m = len(array) // 2
    left = array[:m]
    right = array[m:]
    # print(f"Splitting: {left} {right}")
    sort(left)
    sort(right)
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


if __name__ == "__main__":
    arr = [-1, 7, 1, 19, 5, 10, 9, 17, 23]
    print(arr)
    sort(arr)
    print(arr)
