"""
https://www.e-olymp.com/uk/problems/4853
"""


from collections import deque


class Graph:

    def __init__(self, n):
        self.vertices = {}
        for i in range(1, n + 1):
            self.vertices[i] = set()

    def add_edge(self, i, j):
        self.vertices[i].add(j)
        self.vertices[j].add(i)

    def shortest_path(self, start, finish):
        sources = {start: None}
        queue = deque()
        queue.append(start)
        while queue:
            current = queue.popleft()
            if current == finish:
                break
            for neighbour in self.vertices[current]:
                if neighbour not in sources:
                    queue.append(neighbour)
                    sources[neighbour] = current
        else:
            return -1

        path = []
        while current is not None:
            path.append(current)
            current = sources[current]
        path.reverse()
        return path


if __name__ == '__main__':
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        a, b = map(int, inp.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, inp.readline().split()))
        path = graph.shortest_path(a, b)
        if path == -1:
            print(-1)
        else:
            print(len(path) - 1)
            print(*path)
