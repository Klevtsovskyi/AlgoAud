def sift_down(array, i, end):
    while True:
        left = i * 2 + 1
        right = left + 1

        largest = i
        if left < end and array[largest] < array[left]:
            largest = left
        if right < end and array[largest] < array[right]:
            largest = right

        if largest == i:
            break
        array[i], array[largest] = array[largest], array[i]
        i = largest


def heapsort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i)


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    heapsort(arr)
    print(*arr)
