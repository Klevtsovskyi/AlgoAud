class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1
        return "ok"

    def pop(self):
        if self._top is None:
            return "error"

        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def back(self):
        if self._top is None:
            return "error"
        return self._top.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    f = open("input.txt")
    stack = Stack()
    for line in f:
        res = stack.execute(line)
        print(res)
        if res == "bye":
            break
    f.close()
