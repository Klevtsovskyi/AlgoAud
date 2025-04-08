BRACKETS = {"(": ")", "[": "]"}


def check_brackets(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        else:
            if len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    f = open("input.txt")
    n = int(f.readline())
    for _ in range(n):
        res = check_brackets(f.readline().rstrip())
        print("Yes" if res else "No")
    f.close()
