

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


def convert(number: str, from_base=2, to_base=16):

    stack = Stack()

    for d in number:
        stack.push(d)

    decimal = 0
    base = 1
    while not stack.empty():
        d = stack.pop()
        decimal += int(d, base=from_base) * base
        base *= from_base

    while decimal > 0:
        d = decimal % to_base
        decimal //= to_base
        stack.push(d)

    converted = ""
    while not stack.empty():
        d = stack.pop()
        converted += get_char(d)

    return converted


def get_char(d):
    if d < 10:
        return str(d)
    else:
        return chr(ord("A") + d - 10)


if __name__ == '__main__':
    print(convert(input()))
