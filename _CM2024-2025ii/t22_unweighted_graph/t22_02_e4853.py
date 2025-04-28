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
        sources = {start: -1}
        queue = deque()
        queue.append(start)

        while queue:
            curr = queue.popleft()
            if curr == finish:
                break
            for neighbour in self.vertices[curr]:
                if neighbour not in sources:
                    queue.append(neighbour)
                    sources[neighbour] = curr
        else:
            return []

        path = []
        u = finish
        while u != -1:
            path.append(u)
            u = sources[u]

        path.reverse()
        return path


if __name__ == '__main__':
    f = open("../_CM2024-2025ii/t22_unweighted_graph/input.txt")
    n, m = map(int, f.readline().split())
    a, b = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    path = graph.bfs(a, b)
    print(len(path) - 1)
    print(*path)
    f.close()
