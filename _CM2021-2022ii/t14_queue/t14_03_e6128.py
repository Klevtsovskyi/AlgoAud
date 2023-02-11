"""
https://www.eolymp.com/uk/submissions/10976329
"""


class Deque:

    def __init__(self):
        self._items = []

    def push_front(self, item):
        self._items.insert(0, item)
        return "ok"

    def push_back(self, item):
        self._items.append(item)
        return "ok"

    def pop_front(self):
        return self._items.pop(0)

    def pop_back(self):
        return self._items.pop()

    def front(self):
        return self._items[0]

    def back(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

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
        queue = Deque()
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break