"""
https://www.e-olymp.com/uk/problems/4004
"""


WHITE = 0
GREY = 1
BLACK = 2


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.has_cycle = False

    def _dfs(self, vertices, i):
        vertices[i] = GREY
        for j in range(self.n):
            if self.matrix[i][j] == 1:
                if vertices[j] == WHITE:
                    self._dfs(vertices, j)
                elif vertices[j] == GREY:
                    self.has_cycle = True
        vertices[i] = BLACK

    def check_cycle(self):
        vertices = [WHITE] * self.n
        for i in range(self.n):
            if vertices[i] == WHITE:
                self._dfs(vertices, i)


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append([int(k) for k in inp.readline().split()])
        graph = Graph(matrix)
        graph.check_cycle()
        print(1 if graph.has_cycle else 0)
