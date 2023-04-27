from collections import deque


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(1, size + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def get_path(self, start, finish):
        queue = deque([start])
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
            return - 1

        # print(sources)
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = sources[vertex]

        path.reverse()
        return path


if __name__ == "__main__":
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        a, b = map(int, inp.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, inp.readline().split())
            graph.add_edge(u, v)
        # print(graph.vertices)
        result = graph.get_path(a, b)
        if result == -1:
            print(-1)
        else:
            print(len(result) - 1)
            print(*result)
