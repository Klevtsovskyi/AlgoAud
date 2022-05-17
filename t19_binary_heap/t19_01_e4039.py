"""
https://www.eolymp.com/uk/submissions/11062215
"""


class Heap:

    def __init__(self):
        self.items = [None]

    def insert(self, item):
        self.items.append(item)
        self.sift_up()

    def extract_maximum(self):
        if len(self.items) == 1:
            return

        self.swap(1, -1)
        item = self.items.pop()
        self.sift_down()
        return item

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self):
        curr = len(self.items) - 1
        while curr > 1:  # while curr is not root
            parent = curr // 2
            if self.items[parent] < self.items[curr]:
                self.swap(curr, parent)
                curr = parent
            else:
                break

    def sift_down(self):
        curr = 1
        while curr * 2 < len(self.items):  # while curr has left child
            child = self.max_child(curr)
            if self.items[curr] < self.items[child]:
                self.swap(curr, child)
                curr = child
            else:
                break

    def max_child(self, curr):
        left = curr * 2
        right = curr * 2 + 1
        if right < len(self.items):  # if curr has right child
            if self.items[left] < self.items[right]:
                return right
        return left


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        heap = Heap()
        for _ in range(n):
            command, *args = map(int, f.readline().split())
            if command == 0:
                heap.insert(*args)
            elif command == 1:
                print(heap.extract_maximum())
