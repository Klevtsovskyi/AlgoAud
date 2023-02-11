"""
https://www.eolymp.com/uk/submissions/10914596
"""


min_salary = float("inf")


def assignment(salary, matr):
    global min_salary
    # print(salary, matr)
    if salary >= min_salary:
        return
    elif len(matr) == 0:
        min_salary = salary

    for i in range(len(matr)):
        sub_salary = salary + matr[0][i]
        sub_matr = [
            row[:i] + row[i + 1:]
            for row in matr[1:]
        ]
        assignment(sub_salary, sub_matr)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = [
            [int(k) for k in f.readline().split()]
            for _ in range(n)
        ]

        assignment(0, matrix)
        # print("\n-> ", end="")
        print(min_salary)
