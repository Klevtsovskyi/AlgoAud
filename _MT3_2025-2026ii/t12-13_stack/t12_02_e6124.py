class Stack:

    def __init__(self):
        ...

    def empty(self):
        return True

    def push(self, n):
        return "ok"

    def pop(self):
        return 0

    def back(self):
        return 0

    def size(self):
        return 0

    def clear(self):
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, cmd: str):
        method, *args = cmd.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    stack = Stack()
    f = open("input.txt")
    for line in f:
        result = stack.execute(line)
        print(result)
        if result == "bye":
            break
    f.close()
