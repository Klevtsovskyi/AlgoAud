"""
https://www.eolymp.com/uk/submissions/11032757
"""


import sys

sys.setrecursionlimit(10000)


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = SearchTree(key)
            else:
                self.left.insert(key)

        elif key > self.key:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)

    def height(self):
        if self.left is None:
            left_height = 0
        else:
            left_height = self.left.height()

        if self.right is None:
            right_height = 0
        else:
            right_height = self.right.height()

        return max(left_height, right_height) + 1

    def print(self):
        if self.left is not None:
            self.left.print()

        print(self.key, end=" ")

        if self.right is not None:
            self.right.print()


if __name__ == "__main__":
    with open("input.txt") as f:
        keys = [int(n) for n in f.readline().split()]
        if keys[0] == 0:
            print(0)
        else:
            tree = SearchTree(keys[0])
            for i in range(1, len(keys)):
                if keys[i] == 0:
                    break
                tree.insert(keys[i])

            # tree.print()
            # print()
            print(tree.height())
