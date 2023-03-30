# Postfix
# 5 - 4       -> 5 4 -
# 5 - 4 / 2   -> 5 4 2 / -
# (5 - 1) / 2 -> 5 1 - 2 /

# Prefix
# 2 + 4       -> + 2 4     -> add(2, 4)
# 2 * 4 + 8   -> + * 2 4 8 -> add(multiply(2, 4), 8)
# 2 * (4 + 8) -> * 2 + 4 8 -> multiply(2, add(4, 8))


OPERATORS = "+-*/"


def calculate_postfix(sequence):
    stack = []
    for token in sequence:
        if token in OPERATORS:
            b = int(stack.pop())
            a = int(stack.pop())
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(a // b)
        else:
            stack.append(token)
    return stack.pop()


if __name__ == "__main__":
    print(calculate_postfix(input().split()))
