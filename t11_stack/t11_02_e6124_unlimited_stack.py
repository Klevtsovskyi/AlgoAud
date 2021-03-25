

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.len = 0

    def empty(self):
        return self.top is None

    def push(self, n):
        node = Node(n)
        node.next = self.top
        self.top = node
        self.len += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self.top.item
        self.top = self.top.next
        self.len -= 1
        return item

    def back(self):
        if self.empty():
            return "error"
        return self.top.item

    def size(self):
        return self.len

    def clear(self):
        self.top = None
        self.len = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, line):
        method, *args = line.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as inp:
        stack = Stack()
        for line in inp:
            result = stack.execute(line)
            print(result)
            if result == "bye":
                break
