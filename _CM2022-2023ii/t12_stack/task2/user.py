
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
    stack = [(0, len(array) - 1)]
    while stack:
        a, b = stack.pop()
        if a >= b:
            continue

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

        stack.append((right + 1, b))
        stack.append((a, right))


if __name__ == "__main__":
    arr = [9, -5, -1, 5, 8, -2, 4, 3, 12, 0, 15]
    sort(arr)
    print(arr)
