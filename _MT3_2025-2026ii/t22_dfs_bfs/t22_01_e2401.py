from collections import deque


def wave(graph, start, finish):
    queue = deque()
    queue.append(start)
    distances = {start: 0}
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
    n, f, s = map(int, file.readline().split())
    matrix = [
        list(map(int, file.readline().split()))
        for _ in range(n)
    ]
    print(wave(matrix, f - 1, s - 1))
    file.close()
