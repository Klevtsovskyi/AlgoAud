min_salary: int = 100500


def solve(matr: list[list[int]], salary: int):
    global min_salary
    # print(matr, salary)
    if salary >= min_salary:
        return
    elif len(matr) == 0:
        min_salary = salary
        return

    for j in range(len(matr)):
        sub_matr = [
            row[:j] + row[j + 1:]
            for row in matr[1:]
        ]
        sub_salary = salary + matr[0][j]
        solve(sub_matr, sub_salary)


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    matrix = [
        [int(x) for x in f.readline().split()]
        for _ in range(n)
    ]
    solve(matrix, 0)
    print(min_salary)
    f.close()
