from collections import deque


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def bfs(self, start):
        count = 0

        visited = set()
        visited.add(start)

        queue = deque()
        queue.append(start)
        while queue:
            i = queue.popleft()
            count += 1
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1 and j not in visited:
                    queue.append(j)
                    visited.add(j)
        return count


if __name__ == '__main__':
    f = open("input.txt")
    n, s = map(int, f.readline().split())
    matrix = [
        [int(x) for x in f.readline().split()]
        for _ in range(n)
    ]
    graph = Graph(matrix)
    print(graph.bfs(s - 1))
    f.close()
