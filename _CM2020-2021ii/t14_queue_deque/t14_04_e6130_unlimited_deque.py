"""
https://www.e-olymp.com/uk/problems/6130
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, n):
        node = Node(n)
        node.next = self._front
        if self._front is not None:
            self._front.prev = node
        else:
            self._back = node
        self._front = node
        self._size += 1
        return "ok"

    def push_back(self, n):
        node = Node(n)
        node.prev = self._back
        if self._back is not None:
            self._back.next = node
        else:
            self._front = node
        self._back = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._front is None:
            return "error"
        item = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        else:
            self._front.prev = None
        self._size -= 1
        return item

    def pop_back(self):
        if self._back is None:
            return "error"
        item = self._back.item
        self._back = self._back.prev
        if self._back is None:
            self._front = None
        else:
            self._back.next = None
        self._size -= 1
        return item

    def front(self):
        return "error" if self._front is None else self._front.item

    def back(self):
        return "error" if self._back is None else self._back.item

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
        deque = Deque()
        for line in inp:
            result = deque.execute(line)
            print(result)
            if result == "bye":
                break
