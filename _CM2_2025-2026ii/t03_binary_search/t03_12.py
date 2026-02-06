def bisearch(arr, x):
    return _bisearch(arr, x, 0, len(arr) - 1)


def _bisearch(arr, x, l, r):
    if l >= r:
        return r

    m = l + (r - l) // 2
    if arr[m] < x:
        return _bisearch(arr, x, m + 1, r)
    else:
        return _bisearch(arr, x, l, m)


if __name__ == '__main__':
    arr = [2, 2, 4, 6, 6, 6, 8, 11, 13, 15]
    x = 5
    i = bisearch(arr, x)
    print(i)