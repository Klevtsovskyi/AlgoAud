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

    def leaves(self):
        stack = [self]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                print(node.key, end=" ")
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

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
        print()
    else:
        tree = SearchTree(lst[0])
        for i in range(1, len(lst)):
            if lst[i] == 0:
                break
            tree.insert(lst[i])
        # tree.print()
        tree.leaves()
