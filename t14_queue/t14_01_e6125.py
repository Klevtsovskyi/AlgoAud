"""
https://www.eolymp.com/uk/submissions/10976103
"""


class Queue:

    def __init__(self, maxsize):
        self._items = [None for _ in range(maxsize)]
        self._front = 0
        self._back = 0
        self._size = 0

    def push(self, item):
        if self._size > 0:
            if self._back == len(self._items) - 1:
                self._back = 0
            else:
                self._back += 1

        self._items[self._back] = item
        self._size += 1
        return "ok"

    def pop(self):
        item = self._items[self._front]
        self._items[self._front] = None

        if self._size > 1:
            if self._front == len(self._items) - 1:
                self._front = 0
            else:
                self._front += 1

        self._size -= 1
        return item

    def front(self):
        return self._items[self._front]

    def size(self):
        return self._size

    def clear(self):
        self.__init__(len(self._items))
        return "ok"

    @staticmethod
    def exit():
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        queue = Queue(100)
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
