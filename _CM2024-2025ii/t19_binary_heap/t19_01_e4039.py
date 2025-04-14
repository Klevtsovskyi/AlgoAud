class Heap:

    def __init__(self):
        self._items = [0]

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def insert(self, item):
        self._items.append(item)
        self._sift_up()

    def extract_max(self):
        self._swap(1, -1)
        item = self._items.pop()
        self._sift_down()
        return item

    def _sift_up(self):
        i = len(self._items) - 1
        while i > 1:
            parent = i // 2
            if self._items[i] <= self._items[parent]:
                break
            self._swap(i, parent)
            i = parent

    def _sift_down(self):
        i = 1
        while i * 2 < len(self._items):
            left = i * 2
            right = left + 1
            if right < len(self._items) and self._items[left] < self._items[right]:
                max_child = right
            else:
                max_child = left

            if self._items[max_child] <= self._items[i]:
                break

            self._swap(max_child, i)
            i = max_child


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    heap = Heap()
    for _ in range(n):
        c, *args = map(int, f.readline().split())
        if c == 0:
            heap.insert(*args)
        elif c == 1:
            print(heap.extract_max())
    f.close()
