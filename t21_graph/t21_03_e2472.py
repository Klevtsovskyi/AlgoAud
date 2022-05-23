"""
https://www.eolymp.com/uk/submissions/11104032
"""


class Graph:

    def __init__(self, size):
        self.adjacency_list = {}
        for i in range(1, size + 1):
            self.adjacency_list[i] = []

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def vertex(self, u):
        return self.adjacency_list[u]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        k = int(f.readline())
        graph = Graph(n)
        for _ in range(k):
            command, *args = map(int, f.readline().split())
            if command == 1:
                graph.add_edge(*args)
            elif command == 2:
                neighbours = graph.vertex(*args)
                print(*neighbours)
