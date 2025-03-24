class Deque:

    def __init__(self, maxsize=100):
        self._items = [None for _ in range(maxsize)]
        self._front = 0
        self._back = 0
        self._size = 0

    def push_back(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % len(self._items)
        self._items[self._back] = item
        self._size += 1
        return "ok"

    def push_front(self, item):
        if self._size > 0:
            self._front = (self._front - 1) % len(self._items)
        self._items[self._front] = item
        self._size += 1
        return "ok"

    def pop_front(self):
        item = self._items[self._front]
        self._size -= 1
        if self._size > 0:
            self._front = (self._front + 1) % len(self._items)
        return item

    def pop_back(self):
        item = self._items[self._back]
        self._size -= 1
        if self._size > 0:
            self._back = (self._back - 1) % len(self._items)
        return item

    def front(self):
        return self._items[self._front]

    def back(self):
        return self._items[self._back]

    def size(self):
        return self._size

    def clear(self):
        self._back = self._front = self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    deque = Deque(100)
    with open("input.txt") as f:
        for line in f:
            res = deque.execute(line)
            # print(queue._items)
            print(res)
            if res == "bye":
                break