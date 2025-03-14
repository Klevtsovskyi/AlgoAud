BRACKETS = {"(": ")", "[": "]"}

def check(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        elif len(stack) == 0:
            return False
        elif BRACKETS[stack.pop()] != bracket:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            print("Yes" if check(f.readline().rstrip()) else "No")
