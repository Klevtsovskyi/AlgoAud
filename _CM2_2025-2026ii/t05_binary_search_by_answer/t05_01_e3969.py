def solve(w, h, n):
    l = 0
    r = n * max(w, h)
    while l < r:
        m = l + (r - l) // 2
        count = (m // w) * (m // h)
        if count < n:
            l = m + 1
        else:
            r = m
    return r


if __name__ == '__main__':
    w, h, n = map(int, input().split())
    print(solve(w, h, n))
