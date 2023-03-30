class Queue:

    def __init__(self, maxsize):
        self._items = [None for _ in range(maxsize)]
        self._front = 0
        self._back = 0
        self._size = 0

    def push(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % len(self._items)
        self._items[self._back] = item
        self._size += 1
        return "ok"

    def pop(self):
        item = self._items[self._front]
        self._items[self._front] = None
        if self._size > 1:
            self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return item

    def size(self):
        return self._size


def solve(n, k):
    queue = Queue(n)
    for i in range(1, n + 1):
        queue.push(i)
    while queue.size() > 1:
        for j in range(k - 1):
            queue.push(queue.pop())
        queue.pop()
    return queue.pop()


if __name__ == "__main__":
    N, k = map(int, input().split())
    print(solve(N, k))
