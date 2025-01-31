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
    arr = [1, 1, 2, 4, 4, 6, 7, 7, 7, 9, 9, 11]
    x = 8
    i = bsearch(arr, x)
    print(i)
