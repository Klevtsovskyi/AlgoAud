def calculate(sequence: list[str]) -> int:
    stack = []
    for token in sequence:
        if token in "+-*/":
            right = int(stack.pop())
            left = int(stack.pop())
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(left // right)
        else:
            stack.append(token)
    return stack.pop()


if __name__ == '__main__':
    seq = input().split()
    print(calculate(seq))
