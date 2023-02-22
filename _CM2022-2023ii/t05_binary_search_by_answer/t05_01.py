"""
https://www.eolymp.com/uk/submissions/13000277
"""


def binary_search(w, h, n):
    l = 1
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
    w, h, n = [int(s) for s in input().split()]
    print(binary_search(w, h, n))
