

def assignment(salary, matrix):
    min_salary = float("inf")

    stack = [(salary, matrix)]
    while stack:
        salary, matrix = stack.pop()

        if salary > min_salary:
            continue
        if not matrix:
            if salary < min_salary:
                min_salary = salary
            continue

        for i in range(len(matrix)):
            sub_salary = salary + matrix[0][i]
            sub_matrix = tuple(
                row[:i] + row[i + 1:]
                for row in matrix[1:]
            )
            stack.append((sub_salary, sub_matrix))

    return min_salary


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        matrix = tuple(tuple(map(int, inp.readline().split()))
                       for _ in range(n))
        result = assignment(0, matrix)
        print(result)
