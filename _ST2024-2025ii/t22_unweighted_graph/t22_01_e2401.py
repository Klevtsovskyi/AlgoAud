from collections import deque


def bfs(graph, n, start, finish):
    distances = [-1 for _ in range(n)]
    distances[start] = 0

    queue = deque()
    queue.append(start)
    while queue:
        i = queue.popleft()
        if i == finish:
            return distances[finish]

        for j in range(n):
            if graph[i][j] == 1 and distances[j] == -1:
                queue.append(j)
                distances[j] = distances[i] + 1
    return 0


if __name__ == '__main__':
    inp = open("input.txt")
    n, s, f = map(int, inp.readline().split())

    graph = [
        [int(x) for x in inp.readline().split()]
        for _ in range(n)
    ]
    print(bfs(graph, n, s - 1, f - 1))

    inp.close()
