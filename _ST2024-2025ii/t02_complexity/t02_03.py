def f(n):
    k = 0                   # O(1)
    i = n - 1               # O(1)
    while i != 0:           # O(log(n))
        k += 1.0 / i        # O(log(n))
        i = i // 2          # O(log(n))
    return k                # O(1)

# res: O(log(n))
