"""
https://www.eolymp.com/uk/submissions/11113669
"""


WHITE = 0
GREY = 1
BLACK = 2


class Graph:

    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)

    def has_cycle(self):
        vertices = [WHITE] * self.n
        for i in range(self.n):
            if vertices[i] == WHITE and self.dfs(vertices, i):
                return True
        return False

    def dfs(self, vertices, i):
        vertices[i] = GREY
        for j in range(self.n):
            if self.matrix[i][j] == 1:
                if vertices[j] == GREY:
                    return True
                if vertices[j] == WHITE and self.dfs(vertices, j):
                    return True

        vertices[i] = BLACK


if __name__ == "__main__":
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append([int(k) for k in inp.readline().split()])
        graph = Graph(matrix)

        print(1 if graph.has_cycle() else 0)
