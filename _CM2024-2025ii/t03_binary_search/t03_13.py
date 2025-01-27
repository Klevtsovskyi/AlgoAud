def bsearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l + 1) // 2
        # print(f"l:{l}, m:{m}, r:{r}, arr[m]:{arr[m]}")
        if arr[m] < x:
            r = m - 1
        else:
            l = m
    return l


if __name__ == '__main__':
    array = [13, 11, 11, 11, 9, 7, 6, 6, 6, 4, 4, 1, 1, 0, 0]
    x = 0
    i = bsearch(array, x)
    print(i)
