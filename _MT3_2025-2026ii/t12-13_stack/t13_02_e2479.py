BRACKETS = {
    ")": "(",
    "]": "["
}

def check_brackets(sequence: str):
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS.values():
            stack.append(bracket)
        elif len(stack) == 0:
            return False
        elif stack.pop() != BRACKETS[bracket]:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        line = input()
        print("Yes" if check_brackets(line) else "No")
