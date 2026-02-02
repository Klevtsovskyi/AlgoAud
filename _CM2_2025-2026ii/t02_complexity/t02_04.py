def f(n):
    i = n - 1           # O(1)
    while i != 0:       # O(log(n))
        j = 0           # O(log(n))
        while j < n:    # O(n log(n))
            j += 1      # O(n log(n))
        i = i // 2      # O(log(n))

# O(n log(n))
