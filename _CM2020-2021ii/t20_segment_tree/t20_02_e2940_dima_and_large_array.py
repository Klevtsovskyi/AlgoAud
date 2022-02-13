"""
https://www.e-olymp.com/uk/problems/2940
"""

from math import log2, ceil


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        self.n = 1 << ceil(log2(k))
        self.items = 2 * self.n * [0]
        for i in range(k):
            self.items[self.n + i] = array[i]
        for i in range(self.n - 1, 0, -1):
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

    def add(self, i, item):
        i += self.n
        while i > 0:
            self.items[i] += item
            i = i // 2

    def sum(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.items[left]
            if right % 2 == 0:
                result += self.items[right]
            left = (left + 1) // 2
            right = (right - 1) // 2
        return result


if __name__ == '__main__':
    with open("input.txt") as inp:
        n, q = map(int, inp.readline().split())
        lst = list(map(int, inp.readline().split()))
        tree = SegmentTree(lst)
        for _ in range(q):
            command, f, t = inp.readline().split()
            f = int(f)
            t = int(t)
            if command == "?":
                print(tree.sum(f - 1, t - 1))
            elif command == "+":
                tree.add(f - 1, t)
