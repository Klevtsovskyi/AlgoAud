"""
https://www.eolymp.com/uk/submissions/10951265
"""


def calculate_reverse_polish(sequence):
    stack = []
    for token in sequence:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(left // right)

        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    string = input().split()
    print(calculate_reverse_polish(string))
