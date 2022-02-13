"""
https://www.e-olymp.com/uk/problems/2269
"""


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def count_of_components_v1(self):
        remaining = set(range(len(self.matrix)))
        stack = []
        count = 0
        while remaining or stack:
            if stack:
                i = stack.pop()
            else:
                i = remaining.pop()
                count += 1
            for j in range(len(self.matrix)):
                if matrix[i][j] == 1:
                    if j in remaining:
                        stack.append(j)
                        remaining.remove(j)
        return count

    def _dfs(self, i, colors):
        colors[i] = 1
        for j in range(len(self.matrix)):
            if self.matrix[i][j] == 1:
                if colors[j] == 0:
                    self._dfs(j, colors)

    def count_of_components_v2(self):
        count = 0
        colors = [0 for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            if colors[i] == 0:
                count += 1
                self._dfs(i, colors)
        return count


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(graph.count_of_components_v2())
