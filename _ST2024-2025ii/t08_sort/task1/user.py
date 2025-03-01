
"""
Реалізуйте алгоритм сортування обміном (бульбашкове сортування).
"""

N = 5000     # Кількість елементів масиву.
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
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        # print(array)


if __name__ == "__main__":
    arr = [-1, 7, 1, 19, 5, 10, 9, 17, 23]
    print(arr)
    sort(arr)
    # print(arr)
