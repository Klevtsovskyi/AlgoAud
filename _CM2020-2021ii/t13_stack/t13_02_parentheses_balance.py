

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None

    def push(self, n):
        node = Node(n)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.empty():
            raise RuntimeError
        item = self.top.item
        self.top = self.top.next
        return item


OPENING_BRACKETS = ("(", "[")
CLOSING_BRACKETS = (")", "]")


def check_brackets(bracket_sequence):
    stack = Stack()
    for bracket in bracket_sequence:
        if bracket in OPENING_BRACKETS:
            stack.push(bracket)
        elif not stack.empty():
            i = CLOSING_BRACKETS.index(bracket)
            opening_bracket = stack.pop()
            if opening_bracket != OPENING_BRACKETS[i]:
                return False
        else:
            return False

    if stack.empty():
        return True
    else:
        return False


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        for _ in range(n):
            sequence = inp.readline().rstrip()
            if check_brackets(sequence):
                print("Yes")
            else:
                print("No")
