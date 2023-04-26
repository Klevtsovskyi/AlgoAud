with open("input.txt") as f:
    n = int(f.readline())
    count = 0
    for _ in range(n):
        count += sum(int(a) for a in f.readline().split())
    print(count)
