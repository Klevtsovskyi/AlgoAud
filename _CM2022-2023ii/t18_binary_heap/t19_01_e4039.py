class Heap:

    def __init__(self):
        self.items = [None]

    def insert(self, item):
        self.items.append(item)
        # print(self.items)
        self.sift_up()

    def extract_max(self):
        if len(self.items) == 1:
            return
        self.swap(1, -1)
        item = self.items.pop()
        # print(self.items)
        self.sift_down()
        return item

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
        # print(self.items)

    def sift_up(self):
        curr = len(self.items) - 1
        while curr > 1:
            parent = curr // 2
            if self.items[curr] < self.items[parent]:
                break
            self.swap(curr, parent)
            curr = parent

    def sift_down(self):
        curr = 1
        while curr * 2 < len(self.items):
            left = curr * 2
            right = left + 1
            if right < len(self.items) and self.items[left] < self.items[right]:
                child = right
            else:
                child = left
            if self.items[child] < self.items[curr]:
                break
            self.swap(curr, child)
            curr = child


if __name__ == "__main__":
    with open("input.txt") as f:
        heap = Heap()
        n = int(f.readline())
        for _ in range(n):
            command, *args = map(int, f.readline().split())
            if command == 0:
                heap.insert(*args)
            elif command == 1:
                print(heap.extract_max())
