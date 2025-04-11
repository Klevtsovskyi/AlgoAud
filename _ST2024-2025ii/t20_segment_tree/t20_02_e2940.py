from math import log2, ceil


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k))
        self.n = n = 2 ** p
        self._items = 2 * n * [0]
        for i in range(k):
            self._items[n + i] = array[i]
        # print(self._items)
        for i in range(n - 1, 0, -1):
            self._items[i] = self._items[2 * i] + self._items[2 * i + 1]
        # print(self._items)

    def sum(self, a, b):
        left = a + self.n
        right = b + self.n

        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self._items[left]
            if right % 2 == 0:
                res += self._items[right]

            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

    def add(self, i, item):
        i = self.n + i
        self._items[i] += item
        i = i // 2
        while i > 0:
            self._items[i] += item
            i = i // 2


if __name__ == '__main__':
    f = open("input.txt")
    n, q = map(int, f.readline().split())
    arr = [int(x) for x in f.readline().split()]
    tree = SegmentTree(arr)
    for _ in range(q):
        c, *args = f.readline().split()
        a, b = map(int, args)
        if c == "?":
            print(tree.sum(a - 1, b - 1))
        elif c == "+":
            tree.add(a - 1, b)
    f.close()
