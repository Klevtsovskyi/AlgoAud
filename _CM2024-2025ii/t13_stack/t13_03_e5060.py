OPERATORS = "+-*/"


def calculate(sequence: str) -> int:
    tokens = sequence.split()
    stack = []
    for token in tokens:
        if token in OPERATORS:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a // b)
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == '__main__':
    s = input()
    print(calculate(s))
