"""
https://www.eolymp.com/uk/submissions/11113537
"""


from collections import deque


class Graph:

    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)

    def get_distance(self, start, finish):
        distances = {start: 0}
        queue = deque()
        queue.append(start)
        while len(queue) > 0:
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
            matrix.append([int(k) for k in inp.readline().split()])

        graph = Graph(matrix)
        print(graph.get_distance(s - 1, f - 1))
