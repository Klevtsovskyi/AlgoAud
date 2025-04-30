
WHITE = 0
GREY = 1
BLACK = 2


def topor(graph):
    n = len(graph)
    colors = [WHITE for _ in range(n)]
    for i in range(n):
        if _dfs(graph, i, colors, n):
            return True
    return False


def _dfs(graph, i, colors, n):
    if colors[i] == BLACK:
        return False
    if colors[i] == GREY:
        return True

    colors[i] = GREY
    for j in range(n):
        if graph[i][j] and _dfs(graph, j, colors, n):
            return True
    colors[i] = BLACK
    return False


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    matrix = [
        [int(x) for x in f.readline().split()]
        for _ in range(n)
    ]
    print(int(topor(matrix)))
    f.close()
