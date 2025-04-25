class Graph:

    def __init__(self, matrix):
        self.matrix = matrix

    def dfs(self):
        count = 0
        remaining = set(range(len(self.matrix)))
        stack = []
        while remaining:
            if stack:
                i = stack.pop()
            else:
                i = remaining.pop()
                count += 1

            for j in range(len(self.matrix)):
                if self.matrix[i][j] and j in remaining:
                    stack.append(j)
                    remaining.remove(j)

        return count

if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    matrix = [
        [int(x) for x in f.readline().split()]
        for _ in range(n)
    ]
    graph = Graph(matrix)
    print(graph.dfs())
    f.close()
