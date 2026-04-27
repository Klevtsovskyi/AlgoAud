from math import ceil, log2


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k)) # k <= 2^p
        n = 1 << p  # 2**p
        self.tree = 2 * n * [0]
        for i in range(k):
            self.tree[i + n] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        self.n = n

    def update(self, i, item):
        i = self.n + i
        self.tree[i] = item
        while i > 1:
            i = i // 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def sum(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
            if right % 2 == 0:
                result += self.tree[right]

            left = (left + 1) // 2
            right = (right - 1) // 2
        return result


if __name__ == '__main__':
    f = open("input.txt")
    n, q = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
    tree = SegmentTree(arr)
    for line in f:
        cmd, a, b = line.split()
        if cmd == "=":
            tree.update(int(a) - 1, int(b))
        elif cmd == "?":
            print(tree.sum(int(a) - 1, int(b) - 1))
    f.close()
