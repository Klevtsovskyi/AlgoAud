def calculate(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(a // b)
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    t = input().split()
    print(calculate(t))
