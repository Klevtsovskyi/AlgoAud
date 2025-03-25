min_salary: int = 100500


def solve(matr: list, salary: int):
    global min_salary
    if salary >= min_salary:
        return
    elif len(matr) == 0:
        min_salary = salary
        return

    for i in range(len(matr)):
        sub_matr = [
            row[:i] + row[i + 1:] for row in matr[1:]
        ]
        sub_salary = salary + matr[0][i]
        solve(sub_matr, sub_salary)


if __name__ == "__main__":
    f = open("input.txt")
    n = int(f.readline())
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in f.readline().split()])
    solve(matrix, 0)
    print(min_salary)
    f.close()