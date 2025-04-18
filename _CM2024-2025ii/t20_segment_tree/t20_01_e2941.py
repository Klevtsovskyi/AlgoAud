import math


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = 1 << math.ceil(math.log2(k))
        self.tree = 2 * n * [0]
        self.size = n

        for i in range(k):
            self.tree[n + i] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def sum(self, left, right):
        left += self.size
        right += self.size

        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
            if right % 2 == 0:
                res += self.tree[right]

            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        i = i // 2
        while i > 1:
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
            i = i // 2


if __name__ == '__main__':
    # arr = [3, 4, 1, 13, 5, 2]
    f = open("input.txt")
    n, t = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
    tree = SegmentTree(arr)
    # print(tree.tree)
    for _ in range(t):
        c, *args = f.readline().split()
        a, b = map(int, args)
        if c == "=":
            tree.update(a - 1, b)
        elif c == "?":
            print(tree.sum(a - 1, b - 1))

    f.close()
