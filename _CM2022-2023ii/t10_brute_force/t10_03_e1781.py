min_salary = float("inf")


def solve(matr, salary):
    global min_salary

    if salary > min_salary:
        return
    elif len(matr) == 0:
        min_salary = salary

    for j in range(len(matr)):
        sub_matr = [
            row[:j] + row[j + 1:] for row in matr[1:]
        ]
        sub_salary = salary + matr[0][j]
        solve(sub_matr, sub_salary)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matr = []
        for i in range(n):
            matr.append(
                list(map(int, f.readline().split()))
            )
        solve(matr, 0)
        print(min_salary)
