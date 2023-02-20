"""
https://www.eolymp.com/uk/submissions/12974684
"""


def ones(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count


if __name__ == "__main__":
    n = int(input())
    res = ones(n)
    print(res)


# << >> & | ^ ~

# 100 & 101 = 100
# 100 | 101 = 101
# 100 ^ 101 = 001
# ~100 = 011
