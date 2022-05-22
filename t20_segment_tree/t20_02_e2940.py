"""
https://www.eolymp.com/uk/submissions/11075340
"""


from math import ceil, log2


class SegmentTree:

    def __init__(self, arr):
        k = len(arr)
        n = 1 << ceil(log2(k))
        self.items = [0] * n + arr + [0] * (n - k)
        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]
        self.size = n

    def sum(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1:  # if left is right child
                result += self.items[left]
            if right % 2 == 0:  # if right is left child
                result += self.items[right]
            left = (left + 1) // 2
            right = (right - 1) // 2
        return result

    def add(self, i, item):
        i += self.size
        self.items[i] += item
        while i > 1:  # while i is not root
            i //= 2
            self.items[i] += item


if __name__ == "__main__":
    with open("input.txt") as f:
        n, q = map(int, f.readline().split())
        array = [int(m) for m in f.readline().split()]
        tree = SegmentTree(array)

        for _ in range(q):
            command, j, t = f.readline().split()
            j = int(j)
            t = int(t)
            if command == "?":
                print(tree.sum(j - 1, t - 1))
            elif command == "+":
                tree.add(j - 1, t)
