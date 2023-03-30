OPENING_BRACKETS = ("(", "[")
CLOSING_BRACKETS = (")", "]")


def check_brackets(sequence):
    stack = []
    for bracket in sequence:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif stack:
            i = CLOSING_BRACKETS.index(bracket)
            if stack.pop() != OPENING_BRACKETS[i]:
                return False
        else:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            string = f.readline().strip()
            if check_brackets(string):
                print("Yes")
            else:
                print("No")
