"""
https://www.e-olymp.com/uk/problems/4001
"""


from collections import deque


DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
WALL = "*"
EMPTY = "."


def area(maze, i, j):
    wave = [
        [0 for __ in range(len(maze))]
        for _ in range(len(maze))
    ]
    wave[i][j] = 1
    count = 0
    queue = deque()
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        count += 1
        for di, dj in DIRECTIONS:
            ii, jj = i + di, j + dj
            if maze[ii][jj] != WALL and not wave[ii][jj]:
                queue.append((ii, jj))
                wave[ii][jj] = wave[i][j] + 1
    return count


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(inp.readline().rstrip()))
        I, J = map(int, inp.readline().split())
        print(area(matrix, I - 1, J - 1))
