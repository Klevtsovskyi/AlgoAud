class Graph:

    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix

    def edges(self):
        size = len(self.adjacency_matrix)
        result = []
        for i in range(size):
            for j in range(i + 1, size):
                if self.adjacency_matrix[i][j] == 1:
                    result.append((i + 1, j + 1))
        return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = []
        for _ in range(n):
            matrix.append(
                [int(a) for a in f.readline().split()]
            )
        graph = Graph(matrix)
        for edge in graph.edges():
            print(*edge)
