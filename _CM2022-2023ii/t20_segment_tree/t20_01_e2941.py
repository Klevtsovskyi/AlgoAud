from math import log2, ceil


class SegmentTree:

    def __init__(self, array):
        m = len(array)
        n = 1 << ceil(log2(m))
        self.items = [0] * n + array + [0] * (n - m)
        # print(self.items)
        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]
        # print(self.items)
        self.size = n

    def sum(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1:  # Лівий є правим сином
                result += self.items[left]
            if right % 2 == 0:  # Правий є лівим сином
                result += self.items[right]
            left = (left + 1) // 2
            right = (right - 1) // 2
        return result

    def update(self, i, item):
        i += self.size
        self.items[i] = item
        while i > 1:
            i = i // 2
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]
        # print(self.items)


if __name__ == "__main__":
    with open("input.txt") as f:
        n, q = map(int, f.readline().split())
        arr = list(map(int, f.readline().split()))
        tree = SegmentTree(arr)
        for _ in range(q):
            command, x, y = f.readline().split()
            x = int(x)
            y = int(y)
            if command == "?":
                print(tree.sum(x - 1, y - 1))
            elif command == "=":
                tree.update(x - 1, y)
