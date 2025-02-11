def bsearch(array, x):
    l = 0
    r = len(array) - 1
    while l < r:
        m = l + (r - l) // 2
        print(f"l:{l}, m:{m}, r:{r}, array[m]:{array[m]}")
        if array[m] < x:
            l = m + 1
        else:
            r = m
    return l


if __name__ == "__main__":
    arr = [3, 3, 5, 6, 6, 6, 9, 9, 11, 12, 12, 12, 15]
    x = 8
    i = bsearch(arr, x)
    print(i)
