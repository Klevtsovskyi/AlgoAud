"""
https://www.e-olymp.com/uk/problems/2401
"""


from collections import deque


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def shortest_distance(self, start, finish):
        n = len(self.matrix)
        start -= 1
        finish -= 1
        distances = {start: 0}
        queue = deque()
        queue.append(start)
        while queue:
            i = queue.popleft()
            if i == finish:
                return distances[finish]
            for j in range(n):
                if matrix[i][j] == 1 and j not in distances:
                    queue.append(j)
                    distances[j] = distances[i] + 1
        return 0


if __name__ == '__main__':
    with open("input.txt") as inp:
        n, s, f = map(int, inp.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append([int(k) for k in inp.readline().split()])
        graph = Graph(matrix)
        print(graph.shortest_distance(s, f))
