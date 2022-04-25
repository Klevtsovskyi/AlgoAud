"""
https://www.eolymp.com/uk/submissions/10940689
"""


class Stack:

    def __init__(self):
        self._array = []

    def push(self, item):
        self._array.append(item)
        return "ok"

    def pop(self):
        return self._array.pop()

    def back(self):
        return self._array[-1]

    def size(self):
        return len(self._array)

    def clear(self):
        self._array.clear()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            result = stack.execute(line)
            print(result)
            if result == "bye":
                break
