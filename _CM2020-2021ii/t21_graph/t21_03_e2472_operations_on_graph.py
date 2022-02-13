"""
https://www.e-olymp.com/uk/problems/2472
"""


class Graph:

    def __init__(self, n):
        self.vertices = {}
        for i in range(1, n + 1):
            self.vertices[i] = []

    def add_edge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)

    def vertex(self, u):
        return self.vertices[u]


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        graph = Graph(n)
        k = int(inp.readline())
        for _ in range(k):
            command, *args = map(int, inp.readline().split())
            if command == 1:
                graph.add_edge(*args)
            elif command == 2:
                print(*graph.vertex(*args))
