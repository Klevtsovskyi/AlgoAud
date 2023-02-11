def ones(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count


if __name__ == "__main__":
    n = int(input())
    print(ones(n))
