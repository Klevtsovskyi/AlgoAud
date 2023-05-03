class Graph:

    def __init__(self, size):
        self.vertices = {v: [] for v in range(1, size + 1)}

    def add_edge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)

    def is_connected(self):
        remaining = set(self.vertices)
        stack = [remaining.pop()]
        while stack:
            vertex = stack.pop()
            for neighbour in self.vertices[vertex]:
                if neighbour in remaining:
                    stack.append(neighbour)
                    remaining.remove(neighbour)
        return len(remaining) == 0


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)
        print("YES" if graph.is_connected() else "NO")
