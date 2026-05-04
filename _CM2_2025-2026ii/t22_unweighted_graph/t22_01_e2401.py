from collections import deque


def bfs(graph, start, finish):
    distances = {start: 0}
    queue = deque()
    queue.append(start)
    while queue:
        i = queue.popleft()
        if i == finish:
            return distances[i]
        for j in range(len(graph)):
            if graph[i][j] and j not in distances:
                queue.append(j)
                distances[j] = distances[i] + 1
    return 0


if __name__ == '__main__':
    file = open("input.txt")
    n, s, f = map(int, file.readline().split())
    matrix = [
        list(map(int, file.readline().split()))
        for _ in range(n)
    ]
    # print(*matrix, sep="\n")
    print(bfs(matrix, s - 1, f - 1))
    file.close()
