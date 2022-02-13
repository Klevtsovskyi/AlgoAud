"""
https://www.e-olymp.com/uk/problems/5072
"""


def count_of_edges(matrix):
    count = 0
    for row in matrix:
        count += sum(row)
    return count


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append([int(k) for k in inp.readline().split()])
        print(count_of_edges(matrix))
