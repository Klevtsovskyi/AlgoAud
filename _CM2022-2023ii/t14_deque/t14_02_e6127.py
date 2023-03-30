class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
        else:
            self._back.next = node
        self._back = node
        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"
        node = self._front
        self._front = self._front.next
        if self._size == 1:
            self._back = None
        self._size -= 1
        return node.item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front.item

    def size(self):
        return self._size

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
    queue = Queue()
    with open("input.txt") as f:
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
            