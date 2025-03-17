# Вказівка: реалізацію стеку здійсніть на базі вбудованого списку або масиву

class Stack:

    def __init__(self, maxsize=100):
        self._items = [0 for _ in range(maxsize)]
        self._top = -1

    def push(self, item):
        self._top += 1
        self._items[self._top] = item
        return "ok"

    def pop(self):
        item = self._items[self._top]
        self._top -= 1
        return item

    def size(self):
        return self._top + 1

    def back(self):
        return self._items[self._top]

    def clear(self):
        self.__init__(len(self._items))
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break
