min_value: int


def solve(value, matrix):
    # print(value, matrix)
    global min_value
    if value >= min_value:
        return
    elif len(matrix) == 0:
        min_value = value
        return

    for i in range(len(matrix)):
        next_matrix = [
            row[:i] + row[i+1:] for row in matrix[1:]
        ]
        next_value = value + matrix[0][i]
        solve(next_value, next_matrix)


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    matrix = [
        [int(s) for s in f.readline().split()]
        for _ in range(n)
    ]
    min_value = 1000000
    solve(0, matrix)
    print(min_value)
    f.close()
