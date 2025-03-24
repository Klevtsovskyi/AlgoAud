class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._size = 0
        self._front = None
        self._back = None

    def push(self, n):
        node = Node(n)
        if self._size == 0:
            self._front = node
        else:
            self._back.next = node
        self._back = node
        self._size += 1
        return 'ok'

    def pop(self):
        node = self._front
        if self._size == 0:
            return 'error'
        elif self._size == 1:
            self._back = None
        self._front = self._front.next
        self._size -= 1
        return node.item

    def front(self):
        if self._size == 0:
            return 'error'
        return self._front.item

    def size(self):
        return self._size

    def clear(self):
        self._size = 0
        self._front = self._back = None
        return 'ok'

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    queue = Queue()
    with open("input.txt") as f:
        for line in f:
            res = queue.execute(line)
            print(res)
            if res == "bye":
                break
