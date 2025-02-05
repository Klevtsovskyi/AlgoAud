def bsearch(w, h, n):
    l = max(w, h)
    r = n * max(w, h)
    while l < r:
        m = l + (r - l) // 2
        count = (m // w) * (m // h)
        if count < n:
            l = m + 1
        else:
            r = m
    return l


if __name__ == "__main__":
    w, h, n = map(int, input().split())
    print(bsearch(w, h, n))
