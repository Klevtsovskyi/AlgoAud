"""
https://www.eolymp.com/uk/submissions/11062393
"""


def sift_down(arr, curr, end):
    while True:
        left = curr * 2 + 1
        right = left + 1

        largest = curr
        if left < end and arr[largest] < arr[left]:
            largest = left
        if right < end and arr[largest] < arr[right]:
            largest = right
        if largest == curr:
            break

        arr[curr], arr[largest] = arr[largest], arr[curr]
        curr = largest


def heapsort(arr):
    size = len(arr)
    for i in range((size - 1) // 2, -1, -1):
        sift_down(arr, i, size)
    for i in range(size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i)


if __name__ == "__main__":
    array = [int(n) for n in input().split()]
    heapsort(array)
    print(*array)
