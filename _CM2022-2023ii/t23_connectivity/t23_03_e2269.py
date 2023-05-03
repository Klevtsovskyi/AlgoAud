class Graph:

    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)

    def components_count(self):
        remaining = set(range(self.n))
        stack = []
        count = 0
        while remaining or stack:
            if stack:
                i = stack.pop()
                # print("stack", stack, i)
            else:
                i = remaining.pop()
                # print("remaining", remaining, i)
                count += 1

            for j in range(self.n):
                if matrix[i][j] == 1 and j in remaining:
                    stack.append(j)
                    remaining.remove(j)
        return count


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = []
        for _ in range(n):
            matrix.append(
                [int(a) for a in f.readline().split()]
            )
        graph = Graph(matrix)
        print(graph.components_count())
