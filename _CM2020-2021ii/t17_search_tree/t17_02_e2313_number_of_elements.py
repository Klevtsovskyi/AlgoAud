"""
https://www.e-olymp.com/uk/problems/2313
"""


import sys
sys.setrecursionlimit(100000)


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def has_left(self): return self.left is not None
    def has_right(self): return self.right is not None
    def set_left(self, key): self.left = SearchTree(key)
    def set_right(self, key): self.right = SearchTree(key)

    def insert(self, key):
        node = self
        while True:
            if key == node.key:
                break
            elif key < node.key:
                if node.has_left():
                    node = node.left
                else:
                    node.set_left(key)
                    break
            else:
                if node.has_right():
                    node = node.right
                else:
                    node.set_right(key)
                    break

    def count(self):
        left_count = self.left.count() if self.has_left() else 0
        right_count = self.right.count() if self.has_right() else 0
        return left_count + right_count + 1

    def count_(self):
        _count = 0
        stack = [self]
        while stack:
            node = stack.pop()
            _count += 1
            if node.has_right():
                stack.append(node.right)
            if node.has_left():
                stack.append(node.left)


if __name__ == '__main__':
    lst = [int(n) for n in input().split()]
    if lst[0] == 0:
        print(0)
    else:
        root = SearchTree(lst[0])
        i = 1
        while lst[i] != 0:
            root.insert(lst[i])
            i += 1
        print(root.count_())
