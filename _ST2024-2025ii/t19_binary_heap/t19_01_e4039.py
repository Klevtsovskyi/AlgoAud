class Heap:

    def __init__(self):
        self._items = [None]

    def insert(self, item):
        self._items.append(item)
        # print(self._items)
        self.sift_up()

    def extract_max(self):
        self.swap(1, -1)
        item = self._items.pop()
        # print(self._items)
        self.sift_down()
        return item

    def sift_up(self):
        i = len(self._items) - 1
        while i > 1:
            parent = i // 2
            if self._items[i] <= self._items[parent]:
                break
            self.swap(i, parent)
            i = parent

    def sift_down(self):
        i = 1
        while i * 2 < len(self._items):
            left = i * 2
            right = left + 1
            if right < len(self._items) and self._items[left] < self._items[right]:
                max_child = right
            else:
                max_child = left

            if self._items[i] < self._items[max_child]:
                self.swap(i, max_child)
                i = max_child
            else:
                break

    def swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]
        # print(self._items)


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    heap = Heap()
    for _ in range(n):
        cmd, *args = map(int, f.readline().split())
        if cmd == 0:
            heap.insert(*args)
        else:
            print(heap.extract_max())
    f.close()
