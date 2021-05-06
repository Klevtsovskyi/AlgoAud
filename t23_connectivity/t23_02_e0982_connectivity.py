"""
https://www.e-olymp.com/uk/problems/982
"""


class Graph:

    def __init__(self, n):
        self.vertices = {}
        for i in range(1, n + 1):
            self.vertices[i] = []

    def add_edge(self, i, j):
        self.vertices[i].append(j)
        self.vertices[j].append(i)

    def is_connected(self):
        visited = {1}
        stack = [1]
        while stack:
            current = stack.pop()
            for neighbour in self.vertices[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        return len(self.vertices) == len(visited)


if __name__ == '__main__':
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, inp.readline().split()))
        print("YES" if graph.is_connected() else "NO")
