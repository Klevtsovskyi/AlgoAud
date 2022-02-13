# https://www.e-olymp.com/uk/submissions/8547242
# 100%

def ones(n):
    count = 0
    while n != 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count


if __name__ == '__main__':
    n = int(input())
    count = ones(n)
    print(count)
