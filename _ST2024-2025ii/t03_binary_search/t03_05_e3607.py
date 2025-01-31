if __name__ == "__main__":
    f = open("input.txt")
    while f.readline():
        arr = [int(x) for x in f.readline().split()]
        a, b = [int(x) for x in f.readline().split()]
        print(arr, a, b)
    # solve(arr, a, b)
    f.close()
