''' a18_02_e4848_quick_sort.py

https://www.e-olymp.com/uk/problems/4848

Відсортуйте заданую послідовність використовуючи алгоритм швидкого сортування Хоара.

Вхідні дані:
В одному рядку міститься послідовність з не більше ніж 100000 цілих чисел.

Вихідні дані:
В одному рядку вивести послідовність чисел у неспадному порядку.
Числа слід розділяти між собою одним пропуском.
'''


def heapsort(array):

    def sift_down(start, end):
        while True:
            left = start * 2 + 1
            right = left + 1

            largest = start
            if left < end and array[largest] < array[left]:
                largest = left
            if right < end and array[largest] < array[right]:
                largest = right
            if largest == start:
                break

            array[start], array[largest] = array[largest], array[start]
            start = largest

    size = len(array)
    for i in range(size // 2 - 1, -1, -1):
        sift_down(i, size)
    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(0, i)


if __name__ == '__main__':
    array = list(map(int, input().split()))
    heapsort(array)
    print(*array)
