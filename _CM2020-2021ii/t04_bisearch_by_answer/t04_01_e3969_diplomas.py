

def diplomas(w, h, n):
    l = 0
    r = max(w, h) * n
    while l < r:
        m = l + (r - l) // 2
        nw = m // w
        nh = m // h
        if nw * nh < n:
            l = m + 1
        else:
            r = m
    return l


if __name__ == '__main__':
    w, h, n = map(int, input().split())
    print(diplomas(w, h, n))
