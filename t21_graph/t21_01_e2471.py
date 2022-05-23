"""
https://www.eolymp.com/uk/submissions/11103763
"""


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def adjacency_list(self):
        size = len(self.matrix)
        result = []
        for i in range(size):
            for j in range(i + 1, size):
                if self.matrix[i][j] == 1:
                    result.append((i + 1, j + 1))
        return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matr = []
        for _ in range(n):
            matr.append([int(k) for k in f.readline().split()])
        graph = Graph(matr)
        for row in graph.adjacency_list():
            print(*row)
