
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

        pivot = array[a + (b - a + 1) // 2]
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

        stack.append((left, b))
        stack.append((a, left - 1))


if __name__ == "__main__":
    arr = [-1, 7, 1, 19, 5, 10, 9, 17, 23]
    print(arr)
    sort(arr)
    print(arr)
