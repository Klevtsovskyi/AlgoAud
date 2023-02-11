def diplomas(w, h, n):
    l = 0
    r = n * max(w, h)
    while l < r:
        m = l + (r - l) // 2
        wn = m // w
        hn = m // h
        # print(f"l: {l}, r: {r}, m: {m}, wn * hn: {wn * hn}")
        if wn * hn < n:
            l = m + 1
        else:
            r = m
    # print(f"l: {l}, r: {r}, m: {m}, wn * hn: {wn * hn}")
    return l


if __name__ == "__main__":
    w, h, n = map(int, input().split())
    a = diplomas(w, h, n)
    print(a)
