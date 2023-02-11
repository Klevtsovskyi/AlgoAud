"""
https://www.eolymp.com/uk/submissions/10976287
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

    def push(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
        else:
            self._back.next = node

        self._back = node
        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"

        item = self._front.item
        self._front = self._front.next
        if self._size == 1:
            self._back = None

        self._size -= 1
        return item

    def front(self):
        if self._size == 0:
            return "error"
        else:
            return self._front.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"

    @staticmethod
    def exit():
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        queue = Queue()
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
