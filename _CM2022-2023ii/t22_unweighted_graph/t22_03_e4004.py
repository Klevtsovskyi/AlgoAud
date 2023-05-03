WHITE = 0  # Вершина, яку не було відвідано
GREY = 1   # Вершина, яка опрацьовується
BLACK = 2  # Опрацьована вершина


class Graph:

    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)

    def dfs(self, i, vertices):
        vertices[i] = GREY
        # print("entry", i + 1, vertices)
        for j in range(self.n):
            if self.matrix[i][j] == 1:
                if vertices[j] == WHITE and self.dfs(j, vertices):
                    return True
                elif vertices[j] == GREY:
                    # print("cycle", j + 1)
                    return True
        vertices[i] = BLACK
        # print("exit", i + 1, vertices)

    def has_cycle(self):
        vertices = [WHITE for _ in range(self.n)]
        for i in range(self.n):
            if vertices[i] == WHITE and self.dfs(i, vertices):
                return True
        return False


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = []
        for _ in range(n):
            matrix.append(
                [int(a) for a in f.readline().split()]
            )
        graph = Graph(matrix)
        print(int(graph.has_cycle()))
