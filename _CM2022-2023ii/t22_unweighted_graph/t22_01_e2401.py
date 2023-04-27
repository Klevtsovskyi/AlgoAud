from collections import deque


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def distance(self, start, finish):
        queue = deque([start])
        distances = {start: 0}
        while queue:
            i = queue.popleft()
            if i == finish:
                return distances[finish]
            for j in range(self.n):
                if matrix[i][j] == 1 and j not in distances:
                    queue.append(j)
                    distances[j] = distances[i] + 1
        return 0


if __name__ == "__main__":
    with open("input.txt") as inp:
        n, s, f = map(int, inp.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append(
                [int(a) for a in inp.readline().split()]
            )
        graph = Graph(matrix)
        print(graph.distance(s - 1, f - 1))
