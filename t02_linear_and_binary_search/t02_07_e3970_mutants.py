

if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        array = list(map(int, inp.readline().split()))
        m = int(inp.readline())
        to_search = list(map(int, inp.readline().split()))

    print(n)
    print(array)
    print(m)
    print(to_search)
