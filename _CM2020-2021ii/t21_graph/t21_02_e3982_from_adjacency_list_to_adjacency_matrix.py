"""
https://www.e-olymp.com/uk/problems/3982
"""


def to_adjacency_matrix(lst):
    n = len(lst)
    matrix = [
        [0 for j in range(n)]
        for i in range(n)
    ]
    for i in range(n):
        for j in lst[i]:
            matrix[i][j] = 1
    return matrix


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        adjacency_lst = [set() for _ in range(n)]
        for i in range(n):
            m, *vertices = map(int, inp.readline().split())
            for vertex in vertices:
                adjacency_lst[i].add(vertex - 1)
        matrix = to_adjacency_matrix(adjacency_lst)
        for row in matrix:
            print(*row)
