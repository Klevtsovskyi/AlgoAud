def a(n, k):
    i = 0          # 2
    while i < n:   # 3 * (n + 1)
        k += 1     # 4 * n
        i += 1     # 4 * n

# k += 1 <-> k = k + 1

# n = 0: loop block: 0, while condition: 1
# n = 1: loop block: 1, while condition: 2
# n = 2: loop block: 2, while condition: 3
# n    : loop block: n, while condition: n + 1

# sum: 11n + 5


def b1(n):
    i = 1           # 2
    while i < n:    # 3 * (m + 1)
        i = i * 2   # 4 * m

# n = 2^m -> m = log2(n)

# m = 0, n = 1: loop block: 0
# m = 1, n = 2: loop block: 1
# m = 2, n = 4: loop block: 2
# m    , n    : loop block: m

# sum: 7m + 5 = 7log2(n) + 5

# n = 2^m + b, 0 < b < 2^m


def d(n, k):
    i = 0             # 2
    while i < n:      # 3 * (n + 1)
        j = n         # 2 * n
        while j > 0:  # 3 * n * (n + 1)
            k += 1    # 4 * n * n
            j -= 1    # 4 * n * n
        i += 1        # 4 * n

# sum: 11n^2 + 12n + 5


def e(n, k):
    i = 0             # 2
    while i < n:      # 3 * (n + 1)
        j = i         # 2 * n
        while j < n:  # 3 * (n + 1 + n + ... + 2) = 3 * (n + 3) * n / 2
            k += 1    # 4 * (n + ... + 1) = 4 * n * (n + 1) / 2
            j += 1    # 4 * (n + ... + 1) = 4 * n * (n + 1) / 2
        i += 1        # 4 * n

# sum: c * n^2 + ...


def f(n, k):
    i = 0              # 2
    while i < n:       # 3 * (n + 1)
        j = n          # 2 * n
        while j != 0:  # 3 * n * (m + 1)
            k += 1     # 4 * n * m
            j //= 3    # 4 * n * m
        i += 1         # 4 * n

# n = 3^m -> m = log3(n)

# sum: 11nm + 12n + 5 = 11nlog3(n) + 12n + 5
