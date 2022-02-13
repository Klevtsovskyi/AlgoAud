"""
https://www.e-olymp.com/uk/problems/6127
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def empty(self):
        return self._front is None

    def push(self, n):
        node = Node(n)
        if self._back is not None:
            self._back.next = node
        else:
            self._front = node
        self._back = node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        self._size -= 1
        return item

    def front(self):
        return "error" if self.empty() else self._front.item

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


if __name__ == '__main__':
    with open("input.txt") as inp:
        queue = Queue()
        for line in inp:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
