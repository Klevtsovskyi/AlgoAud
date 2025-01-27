def bsearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        print(f"l:{l}, m:{m}, r:{r}, arr[m]:{arr[m]}")
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l


if __name__ == '__main__':
    array = [0, 1, 1, 4, 4, 6, 6, 6, 7, 9, 11, 11, 11, 13]
    x = 10
    i = bsearch(array, x)
    print(i)
