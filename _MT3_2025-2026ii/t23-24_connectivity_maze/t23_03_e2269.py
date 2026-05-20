from collections import deque


def components_count(graph):
    remaining = set(range(len(graph)))
    queue = deque()
    count = 0
    while remaining or queue:
        if queue:
            i = queue.popleft()
        else:
            i = remaining.pop()
            count += 1
        for j in range(len(graph[i])):
            if graph[i][j] and j in remaining:
                queue.append(j)
                remaining.discard(j)
    return count


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    matrix = [
        [int(x) for x in f.readline().split()]
        for _ in range(n)
    ]
    print(components_count(matrix))
    f.close()
