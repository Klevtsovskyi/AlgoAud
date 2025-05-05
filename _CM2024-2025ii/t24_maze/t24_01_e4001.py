from collections import deque

WALL = "*"
CELL = "."

VISITED = 1
EMPTY = 0

DIRECTIONS = ((0, -1), (-1, 0), (0, 1), (1, 0))

def wave(maze, n, si, sj):
    count = 0
    visited = [
        [EMPTY for __ in range(n)]
        for _ in range(n)
    ]
    visited[si][sj] = VISITED
    queue = deque()
    queue.append((si, sj))
    while queue:
        i, j = queue.popleft()
        count += 1
        for di, dj in DIRECTIONS:
            ni = i + di
            nj = j + dj
            if maze[ni][nj] == CELL and visited[ni][nj] == EMPTY:
                queue.append((ni, nj))
                visited[ni][nj] = VISITED
    return count


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    maze = [
        list(f.readline().rstrip())
        for _ in range(n)
    ]
    si, sj = map(int, f.readline().split())
    print(wave(maze, n, si - 1, sj - 1))
    f.close()
