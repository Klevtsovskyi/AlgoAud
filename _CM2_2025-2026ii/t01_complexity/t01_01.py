def a(n, k):
    i = 0          # 2
    while i < n:   # 3 * (n + 1)
        k += 1     # 4 * n
        i += 1     # 4 * n

# k += 1 <=> k = k + 1

# n = 0 -> while condition: 1,     loop block: 0
# n = 1 -> while condition: 2,     loop block: 1
# n = 2 -> while condition: 3,     loop block: 2
# n     -> while condition: n + 1, loop block: n

# sum = 11n + 5


def b1(n):
    i = 1           # 2
    while i < n:    # 3 * (m + 1)
        i = i * 2   # 4 * m

# 1) n = 2^m -> m = log2(n)

# n = 1, m = 0 -> loop block: 0
# n = 2, m = 1 -> loop block: 1
# n = 4, m = 2 -> loop block: 2
# n = 8, m = 3 -> loop block: 3
# n    , m     -> loop block: m

# sum = 7m + 5 = 7 log2(n) + 5

# 2) n = 2^m + b, 0 < b < 2^m -> m = log2(n - b) = floor(log2(n))

def b2(n):
    i = 1           # 2
    while i < n:    # 3 * (m + 2)
        i = i * 2   # 4 * (m + 1)

# n = 3, m = 1 -> loop block: 2
# n = 5, m = 2 -> loop block: 3
# n = 9, m = 3 -> loop block: 4
# n    , m     -> loop block: m + 1

# sum = 7m + 12 = 7 floor(log2(n)) + 12 = 7 (floor(log2(n)) + 1) + 5 = 7 ceil(log2(n)) + 5

# 1) + 2): sum = 7 ceil(log2(n)) + 5


def c(n, k):
    i = 0               # 2
    while i < n:        # 3 * (n + 1)
        if i % 2 == 0:  # 5 * n
            k += 1      # 4 * (n / 2)
        i += 1          # 4 * n

# sum = 14n + 5


def d(n, k):
    i = 0             # 2
    while i < n:      # 3 * (n + 1)
        j = n         # 2 * n
        while j > 0:  # 3 * n * (n + 1)
            k += 1    # 4 * n * n
            j -= 1    # 4 * n * n
        i += 1        # 4 * n

# sum = 11n^2 + 12n + 5


def e(n, k):
    i = 0             # 2
    while i < n:      # 3 * (n + 1)
        j = i         # 2 * n
        while j < n:  # 3 * ((n + 1) + n + ... + 2) = 3 * n + 3 * (n + ... + 2 + 1) = 3 * n + 3 * n * (n + 1) / 2
            k += 1    # 4 * (n + (n - 1) + ... + 1) = 4 * n * (n + 1) / 2 = 2 * n * (n + 1)
            j += 1    # 4 * (n + (n - 1) + ... + 1) = 4 * n * (n + 1) / 2 = 2 * n * (n + 1)
        i += 1        # 4 * n

# sum = (5 + 1/2) * n^2 + (17 + 1/2) * n + 5


def f(n, k):
    i = 0              # 2
    while i < n:       # 3 * (n + 1)
        j = n          # 2 * n
        while j != 0:  # 3 * n * (m + 1)
            k += 1     # 4 * n * m
            j //= 3    # 4 * n * m
        i += 1         # 4 * n

# n = 3^m -> m = log3(n)

# sum = 11nm + 12n + 5 = 11 n log3(n) + 12 n + 5
