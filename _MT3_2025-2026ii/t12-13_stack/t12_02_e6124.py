class Node:

    def __init__(self, item):
        self.item = item
        self.next: Node | None = None


class Stack:

    def __init__(self):
        self._top: Node | None = None
        self._size = 0

    def empty(self):
        return self._top is None

    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def back(self):
        if self.empty():
            return "error"
        return self._top.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, cmd: str):
        method, *args = cmd.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    stack = Stack()
    f = open("input.txt")
    for line in f:
        result = stack.execute(line)
        print(result)
        if result == "bye":
            break
    f.close()
