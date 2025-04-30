WALL = "*"
CELL = "."
EMPTY = 0
VISITED = 1

DIRECTIONS = [
    (0, -1), (-1, 0), (0, 1), (1, 0)
]

def slay(maze, n, si, sj):
    visited = [
        [EMPTY for __ in range(n)]
        for _ in range(n)
    ]
    visited[si][sj] = VISITED
    stack = [(si, sj)]
    count = 0
    while stack:
        i, j = stack.pop()
        count += 1
        for di, dj in DIRECTIONS:
            ii = i + di
            jj = j + dj
            if maze[ii][jj] != WALL and not visited[ii][jj]:
                stack.append((ii, jj))
                visited[ii][jj] = VISITED
    return count


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    maze = [list(f.readline().rstrip()) for _ in range(n)]
    # print(*maze, sep="\n")
    si, sj = map(int, f.readline().split())
    print(slay(maze, n, si - 1, sj - 1))
    f.close()
