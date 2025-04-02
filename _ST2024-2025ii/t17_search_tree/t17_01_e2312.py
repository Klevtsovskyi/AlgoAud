import sys

sys.setrecursionlimit(1000000)


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is not None:
                self.left.insert(key)
            else:
                self.left = SearchTree(key)
        elif key > self.key:
            if self.right is not None:
                self.right.insert(key)
            else:
                self.right = SearchTree(key)

    def height(self):
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return max(left_height, right_height) + 1

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()


# 7 3 2 1 9 5 4 6 8 0
if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    if lst[0] == 0:
        print(0)
    else:
        tree = SearchTree(lst[0])
        for i in range(1, len(lst)):
            if lst[i] == 0:
                break
            tree.insert(lst[i])
        # tree.print()
        print(tree.height())
