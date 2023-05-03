class Graph:

    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)

    def vertex_count(self, start):
        visited = {start}
        stack = [start]
        while stack:
            i = stack.pop()
            # print(i + 1)
            for j in range(self.n):
                if matrix[i][j] == 1 and j not in visited:
                    stack.append(j)
                    visited.add(j)
        return len(visited)


if __name__ == "__main__":
    with open("input.txt") as f:
        n, s = map(int, f.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append(
                [int(a) for a in f.readline().split()]
            )
        graph = Graph(matrix)
        print(graph.vertex_count(s - 1))
