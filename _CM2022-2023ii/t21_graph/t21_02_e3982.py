class Graph:

    def __init__(self, size):
        self.vertices = {
            v: [] for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source].append(destination)

    def adjacency_matrix(self):
        size = len(self.vertices)
        matrix = [
            [0 for j in range(size)] for i in range(size)
        ]
        for vertex in self.vertices:
            for neighbour in self.vertices[vertex]:
                i = vertex - 1
                j = neighbour - 1
                matrix[i][j] = 1
        return matrix


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        graph = Graph(n)
        for vertex in range(1, n + 1):
            count, *neighbours = map(int, f.readline().split())
            for neighbour in neighbours:
                graph.add_edge(vertex, neighbour)
    for row in graph.adjacency_matrix():
        print(*row)
