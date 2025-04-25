class Graph:

    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def dfs(self):
        visited = set()
        visited.add(1)

        stack = [1]
        while stack:
            u = stack.pop()
            for v in self.vertices[u]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)

        return len(visited) == len(self.vertices)


if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    print("YES" if graph.dfs() else "NO")
    f.close()