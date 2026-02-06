def bisearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        print(f"l: {l}, m: {m}, r: {r}, arr[m]: {arr[m]}")
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return r


if __name__ == '__main__':
    arr = [2, 2, 4, 6, 6, 6, 8, 11, 13, 15]
    x = 5
    i = bisearch(arr, x)
    print(i)
