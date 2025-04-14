def sift_down(array, i, end):
    while i * 2 + 1 < end:
        left = i * 2 + 1
        right = left + 1
        if right < end and array[left] < array[right]:
            max_child = right
        else:
            max_child = left

        if array[max_child] <= array[i]:
            break

        array[max_child], array[i] = array[i], array[max_child]
        i = max_child


def heapsort(array):
    n = len(array)
    for i in range((n - 1) // 2, -1, -1):
        sift_down(array, i, n)
    for i in range(1, n):
        array[0], array[n - i] = array[n - i], array[0]
        sift_down(array, 0, n - i)


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    heapsort(arr)
    print(*arr)
