"""
https://www.e-olymp.com/uk/problems/4848
"""


def sift_down(array, start, end):
    while True:
        left = start * 2 + 1
        right = left + 1
        largest = start
        if left < end and array[left] > array[largest]:
            largest = left
        if right < end and array[right] > array[largest]:
            largest = right
        if largest == start:
            break

        array[start], array[largest] = array[largest], array[start]
        start = largest


def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i)


if __name__ == '__main__':
    lst = [int(n) for n in input().split()]
    heap_sort(lst)
    print(*lst)
