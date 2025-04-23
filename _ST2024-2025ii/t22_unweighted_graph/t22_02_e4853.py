from collections import deque


class Graph:

    def __init__(self, n):
        self.vertices = {
            v: set() for v in range(1, n + 1)
        }

    def add_edge(self, v, u):
        self.vertices[v].add(u)
        self.vertices[u].add(v)

    def bfs(self, start, finish):
        sources = {start: -1}
        queue = deque()
        queue.append(start)
        while queue:
            vertex = queue.popleft()
            if vertex == finish:
                break
            for neighbour in self.vertices[vertex]:
                if neighbour not in sources:
                    queue.append(neighbour)
                    sources[neighbour] = vertex

        if finish not in sources:
            return []

        path = []
        vertex = finish
        while vertex != -1:
            path.append(vertex)
            vertex = sources[vertex]
        path.reverse()
        return path


if __name__ == '__main__':
    inp = open("input.txt")
    n, m = map(int, inp.readline().split())
    a, b = map(int, inp.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, inp.readline().split())
        graph.add_edge(u, v)

    path = graph.bfs(a, b)

    print(len(path) - 1)
    print(*path)

    inp.close()
