class Graph:

    def __init__(self, size):
        self.vertices = {
            v: [] for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source].append(destination)
        self.vertices[destination].append(source)

    def vertex(self, u):
        return self.vertices[u]


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
                print(*graph.vertex(*args))

