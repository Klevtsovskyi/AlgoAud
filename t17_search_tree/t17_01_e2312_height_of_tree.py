"""
https://www.e-olymp.com/uk/problems/2312
"""


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
        if key < self.key:
            if self.has_left():
                self.left.insert(key)
            else:
                self.set_left(key)
        elif self.key < key:
            if self.has_right():
                self.right.insert(key)
            else:
                self.set_right(key)

    def height(self):
        left_height = self.left.height() if self.has_left() else 0
        right_height = self.right.height() if self.has_right() else 0
        return max(left_height, right_height) + 1


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
        print(root.height())
