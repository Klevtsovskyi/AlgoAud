from collections import deque


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def bfs(self, start, finish):
        n = len(self.matrix)
        distances = [-1 for _ in range(n)]
        distances[start] = 0

        queue = deque()
        queue.append(start)
        while queue:
            i = queue.popleft()
            if i == finish:
                return distances[i]
            for j in range(n):
                if self.matrix[i][j] and distances[j] == -1:
                    queue.append(j)
                    distances[j] = distances[i] + 1
        return 0


if __name__ == '__main__':
    inp = open("input.txt")
    n, s, f = map(int, inp.readline().split())
    matrix = [
        [int(x) for x in inp.readline().split()]
        for _ in range(n)
    ]
    graph = Graph(matrix)
    print(graph.bfs(s - 1, f - 1))
    inp.close()
