def f(n):
    k = 0               # O(1)
    i = n - 1           # O(1)
    while i != 0:       # O(log(n))
        k += 1.0 / i    # O(log(n))
        i = i // 2      # O(log(n))
    return k            # O(1)

# res: O(log(n))

# n - 1 = 2^m -> m = log(n - 1)
#   1 / 2^m + 1 / 2^m / 2 + 1 / 2^m / 2^2 + ... + 1 / 2^m / 2^m =
# = 2^{-m} sum_{j=0}^{m} 2^j = 2^{-m} (2^{m+1} - 1) =
# = 2 - 2^{-m} = 2 - 1 / (n - 1)


