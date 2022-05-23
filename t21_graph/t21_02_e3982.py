"""
https://www.eolymp.com/uk/submissions/11103891
"""


class Graph:

    def __init__(self, size):
        self.adjacency_list = {}
        for i in range(1, size + 1):
            self.adjacency_list[i] = []

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)

    def adjacency_matrix(self):
        size = len(self.adjacency_list)
        matrix = [
            [0 for j in range(size)]
            for i in range(size)
        ]
        for vertex in self.adjacency_list:
            for neighbour in self.adjacency_list[vertex]:
                i = vertex - 1
                j = neighbour - 1
                matrix[i][j] = 1

        return matrix


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        graph = Graph(n)
        for i in range(1, n + 1):
            vertices = [int(k) for k in f.readline().split()][1:]
            for j in vertices:
                graph.add_edge(i, j)

        for row in graph.adjacency_matrix():
            print(*row)
