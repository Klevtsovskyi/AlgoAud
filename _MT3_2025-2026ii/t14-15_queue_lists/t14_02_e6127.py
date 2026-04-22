class Node:

    def __init__(self, item):
        self.item = item
        self.next: Node | None = None


class Queue:

    def __init__(self):
        self._front: Node | None = None
        self._back: Node | None = None
        self._size = 0

    def empty(self):
        return self._front is None

    def push(self, item):
        ...

    def pop(self):
        ...

    def front(self):
        if self.empty():
            return "error"


    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, cmd: str):
        method, *args = cmd.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    queue = Queue()
    f = open("input.txt")
    for line in f:
        result = queue.execute(line)
        print(result)
        if result == "bye":
            break
    f.close()