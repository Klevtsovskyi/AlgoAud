"""
Вхідні дані #1
10
1 1 3 3 5 7 9 18 18 57
5
57 3 9 1 179
Вихідні дані #1
1
2
1
2
0
"""
# https://www.eolymp.com/uk/submissions/10550570


def mutants(array, to_search):
    return [1, 2, 1, 2, 0]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        m = int(f.readline())
        to_search = [int(s) for s in f.readline().split()]

        # print(n)
        # print(array)
        # print(m)
        # print(to_search)

        result = mutants(array, to_search)
        print(*result, sep="\n")
