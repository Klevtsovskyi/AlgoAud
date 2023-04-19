def sift_down(array, curr, end):
    while True:
        left = curr * 2 + 1
        right = left + 1

        largest = curr
        if left < end and array[largest] < array[left]:
            largest = left
        if right < end and array[largest] < array[right]:
            largest = right

        if largest == curr:
            break

        array[curr], array[largest] = array[largest], array[curr]
        curr = largest


def heapsort(array):
    n = len(array)
    for i in range((n - 1) // 2, -1, -1):
        sift_down(array, i, n)
    for i in range(1, n):
        array[0], array[n - i] = array[n - i], array[0]
        sift_down(array, 0, n - i)


if __name__ == "__main__":
    with open("input.txt") as f:
        a = list(map(int, f.readline().split()))
        heapsort(a)
        print(*a)
