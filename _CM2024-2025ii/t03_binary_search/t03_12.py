def bsearch(arr, x):
    return _bsearch(arr, 0, len(arr) - 1, x)


def _bsearch(arr, l, r, x):
    if l == r:
        return l

    m = l + (r - l) // 2
    if arr[m] < x:
        return _bsearch(arr, m + 1, r, x)
    else:
        return _bsearch(arr, l, m, x)


if __name__ == '__main__':
    array = [0, 1, 1, 4, 4, 6, 6, 6, 7, 9, 11, 11, 11, 13]
    x = 6
    i = bsearch(array, x)
    print(i)
