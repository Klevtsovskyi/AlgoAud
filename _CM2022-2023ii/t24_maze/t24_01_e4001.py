from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
WALL = "*"
CELL = "."
EMPTY = 0
VISITED = 1


def square(maze, i, j):
    count = 0
    visited = [
        [EMPTY for _ in range(len(maze))]
        for __ in range(len(maze))
    ]
    visited[i][j] = VISITED
    queue = deque()
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        count += 1
        for di, dj in DIRECTIONS:
            ii = i + di
            jj = j + dj
            if maze[ii][jj] == CELL and visited[ii][jj] == EMPTY:
                queue.append((ii, jj))
                visited[ii][jj] = VISITED
    # print(*visited, sep="\n", end="\n\n")
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = [
            list(f.readline().rstrip()) for _ in range(n)
        ]
        start_i, start_j = map(int, f.readline().split())
        # print(*matrix, sep="\n", end="\n\n")
        print(square(matrix, start_i - 1, start_j - 1))
