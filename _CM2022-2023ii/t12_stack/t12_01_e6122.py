class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return "ok"

    def pop(self):
        return self._items.pop()

    def back(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()
        return "ok"

    @staticmethod
    def exit():
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    stack = Stack()
    with open("input.txt") as f:
        for line in f:
            result = stack.execute(line)
            print(result)
            if result == "bye":
                break
