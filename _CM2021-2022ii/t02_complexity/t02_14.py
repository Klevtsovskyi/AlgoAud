def A(n):
    s = 0                   # O(1)
    for i in range(n + 1):  # O(n)
        s += i              # O(n)
    return s                # O(1)
