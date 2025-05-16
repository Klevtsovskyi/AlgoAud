def floyd(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == '__main__':
    n = int(input())
    graph = [
        [int(x) for x in input().split()]
        for _ in range(n)
    ]
    floyd(graph, n)
    for row in graph:
        print(*row)
