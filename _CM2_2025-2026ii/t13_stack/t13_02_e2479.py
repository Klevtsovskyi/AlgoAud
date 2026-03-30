BRACKETS = {
    ")": "(", "]": "["
}


def solve(sequence):
    stack = []
    for b in sequence:
        if b in BRACKETS.values():
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            if stack.pop() != BRACKETS[b]:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        seq = input().strip()
        if solve(seq):
            print("Yes")
        else:
            print("No")