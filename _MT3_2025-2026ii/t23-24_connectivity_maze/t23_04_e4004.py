WHITE = 0
GREY = 1
BLACK = 2

class HasCycle(RuntimeError):
    pass


def has_cycle(graph):
    vertices = [WHITE for _ in range(len(graph))]
    try:
        for i in range(len(graph)):
            __dfs(graph, vertices, i)
    except HasCycle:
        return True
    else:
        return False


def __dfs(graph, vertices, i):
    if vertices[i] == BLACK:
        return
    if vertices[i] == GREY:
        raise HasCycle

    vertices[i] = GREY
    for j in range(len(graph[i])):
        if graph[i][j]:
            __dfs(graph, vertices, j)
    vertices[i] = BLACK


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    matrix = [
        [int(x) for x in f.readline().split()]
        for _ in range(n)
    ]
    print(int(has_cycle(matrix)))
    f.close()
