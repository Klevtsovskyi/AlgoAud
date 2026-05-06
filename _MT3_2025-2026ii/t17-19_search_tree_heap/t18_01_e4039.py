class Heap:

    def __init__(self):
        self.items = [0]

    def insert(self, item):
        self.items.append(item)
        self.sift_up()

    def extract(self):
        self.swap(1, len(self.items) - 1)
        item = self.items.pop()
        self.sift_down()
        return item

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self):
        i = len(self.items) - 1
        while i > 1:
            parent = i // 2
            if self.items[parent] < self.items[i]:
                self.swap(parent, i)
                i = parent
            else:
                break

    def sift_down(self):
        i = 1
        while i * 2 < len(self.items):
            left = i * 2
            right = left + 1
            if right < len(self.items) and self.items[left] < self.items[right]:
                max_child = right
            else:
                max_child = left

            if self.items[i] < self.items[max_child]:
                self.swap(i, max_child)
                i = max_child
            else:
                break


if __name__ == '__main__':
    f = open("input.txt")
    heap = Heap()
    n = int(f.readline())
    for _ in range(n):
        cmd, *args = map(int, f.readline().split())
        if cmd == 0:
            heap.insert(*args)
        elif cmd == 1:
            print(heap.extract())
        # print(heap.items)
    f.close()
