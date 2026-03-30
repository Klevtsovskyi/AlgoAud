def solve(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            match token:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    stack.append(a // b)
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == '__main__':
    seq = input().split()
    print(solve(seq))
