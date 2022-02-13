"""
https://www.e-olymp.com/uk/problems/4000
"""


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def count_of_vertices(self, start):
        start -= 1
        visited = {start}
        stack = [start]
        while stack:
            i = stack.pop()
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    if j not in visited:
                        stack.append(j)
                        visited.add(j)
        return len(visited)


if __name__ == '__main__':
    with open("input.txt") as inp:
        n, s = map(int, inp.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(graph.count_of_vertices(s))
