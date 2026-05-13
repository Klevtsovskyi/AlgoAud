from collections import deque


class Graph:

    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def bfs(self, start, finish):
        queue = deque()
        queue.append(start)
        sources = {start: None}
        while queue:
            vertex = queue.popleft()
            if vertex == finish:
                break
            for neighbour in self.vertices[vertex]:
                if neighbour not in sources:
                    queue.append(neighbour)
                    sources[neighbour] = vertex
        else:
            return []

        v = finish
        path = []
        while v is not None:
            path.append(v)
            v = sources[v]

        path.reverse()
        return path


if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    a, b = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    path = graph.bfs(a, b)
    print(len(path) - 1)
    if path:
        print(*path)
    f.close()
