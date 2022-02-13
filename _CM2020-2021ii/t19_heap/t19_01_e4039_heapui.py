"""
https://www.e-olymp.com/uk/problems/4039
"""


class Heap:

    def __init__(self):
        self.items = [0]

    # is_empty(self): return len(self.items) == 1
    # is_root(i): return i == 1
    # get_left(i): return i * 2
    # get_right(i): return i * 2 + 1
    # has_left(i): return i * 2 < len(self.items)
    # has_right(i): return i * 2 + 1 < len(self.items)
    # get_parent(i): return i // 2

    def insert(self, item):
        self.items.append(item)
        self.sift_up()

    def extract_max(self):
        if len(self.items) > 1:
            self.swap(1, -1)
            item = self.items.pop()
            self.sift_down()
            return item

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self):
        curr = len(self.items) - 1
        while curr > 1:
            parent = curr // 2
            if self.items[curr] > self.items[parent]:
                self.swap(curr, parent)
                curr = parent
            else:
                break

    def sift_down(self):
        curr = 1
        while curr * 2 < len(self.items):
            child = self.get_max_child(curr)
            if self.items[curr] < self.items[child]:
                self.swap(curr, child)
                curr = child
            else:
                break

    def get_max_child(self, curr):
        left = curr * 2
        right = left + 1
        if right < len(self.items):
            if self.items[left] < self.items[right]:
                return right
        return left


if __name__ == '__main__':
    with open("input.txt") as inp:
        n = int(inp.readline())
        heap = Heap()
        for _ in range(n):
            command, *args = map(int, inp.readline().split())
            if command == 0:
                heap.insert(*args)
            elif command == 1:
                print(heap.extract_max())
