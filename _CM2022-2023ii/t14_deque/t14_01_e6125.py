class Queue:

    def __init__(self, maxsize):
        self._items = [None for _ in range(maxsize)]
        self._front = 0
        self._back = 0
        self._size = 0

    def push(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % len(self._items)
        self._items[self._back] = item
        self._size += 1
        return "ok"

    def pop(self):
        item = self._items[self._front]
        self._items[self._front] = None
        if self._size > 1:
            self._front = (self._front + 1) % len(self._items)
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
    queue = Queue(100)
    with open("input.txt") as f:
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
