

min_salary = float("inf")


def assignment(salary, matrix):
    global min_salary

    if salary > min_salary:
        return
    if not matrix:
        if salary < min_salary:
            min_salary = salary
        return

    for i in range(len(matrix)):
        sub_salary = salary + matrix[0][i]
        sub_matrix = tuple(
            row[:i] + row[i + 1:]
            for row in matrix[1:]
        )
        assignment(sub_salary, sub_matrix)


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = tuple(tuple(map(int, inp.readline().split()))
                       for _ in range(n))
        min_salary = float("inf")
        assignment(0, matrix)
        print(min_salary)
