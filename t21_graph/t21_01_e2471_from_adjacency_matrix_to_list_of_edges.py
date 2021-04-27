"""
https://www.e-olymp.com/uk/problems/2471
"""


def list_of_edges(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges.append((i + 1, j + 1))
    return edges


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append([int(k) for k in inp.readline().split()])
        edges = list_of_edges(matrix)
        for edge in edges:
            print(*edge)
