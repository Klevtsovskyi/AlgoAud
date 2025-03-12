class Stack:

    def __init__(self, maxsize=100):
        self._maxsize = maxsize
        self._size = 0
        self._items = [0 for _ in range(maxsize)]
        self._top = 0

    def empty(self): return self._size == 0
    def size(self): return self._size

    def push(self, item):
        if not self.empty():
            self._top += 1
        self._items[self._top] = item
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            raise RuntimeError
        item = self._items[self._top]
        # self._items[self._top] = 0
        self._size -= 1
        if not self.empty():
            self._top -= 1
        return item

    def back(self):
        if self.empty():
            raise RuntimeError
        return self._items[self._top]

    def clear(self):
        self.__init__(self._maxsize)
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    stack = Stack(100)
    with open("input.txt") as f:
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break
