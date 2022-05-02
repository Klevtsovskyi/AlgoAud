"""
https://www.eolymp.com/uk/submissions/10976397
"""


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

        item = self._front.item
        self._front = self._front.next
        if self._size == 1:
            self._back = None

        self._size -= 1
        return item

    def size(self):
        return self._size


def josephus(n, k):
    queue = Queue()
    for i in range(1, n + 1):
        queue.push(i)

    while queue.size() != 1:
        for _ in range(k - 1):
            queue.push(queue.pop())
        queue.pop()

    return queue.pop()


if __name__ == "__main__":
    print(josephus(*map(int, input().split())))
