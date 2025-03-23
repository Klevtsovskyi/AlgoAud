BRACKETS = {"(": ")", "[": "]"}


def check(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        elif len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    with open("../../_a/input.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            s = f.readline().rstrip()
            print("Yes" if check(s) else "No")
