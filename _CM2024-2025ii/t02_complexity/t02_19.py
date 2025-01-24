import time


def trib(k):
    t0 = 0
    t1 = t2 = 1
    for i in range(k):
        t3 = t2 + t1 + t0
        t0 = t1
        t1 = t2
        t2 = t3
    return t0


def tribr(k):
    if k == 0:
        return 0
    if k == 1 or k == 2:
        return 1
    return tribr(k - 1) + tribr(k - 2) + tribr(k - 3)


if __name__ == "__main__":
    n = 35
    s = time.time()
    trib(n)
    print(time.time() - s)
    s = time.time()
    tribr(n)
    print(time.time() - s)
