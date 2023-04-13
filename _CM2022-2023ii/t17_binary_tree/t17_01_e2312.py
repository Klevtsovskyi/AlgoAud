import sys
from collections import deque

sys.setrecursionlimit(1000000)


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
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return max(left_height, right_height) + 1

    def height_bfs(self):
        max_height = 0
        queue = deque()
        queue.append((self, 1))
        while queue:
            node, _height = queue.popleft()
            if node.left is not None:
                queue.append((node.left, _height + 1))
            if node.right is not None:
                queue.append((node.right, _height + 1))
            if _height > max_height:
                max_height = _height
        return max_height

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()


if __name__ == "__main__":
    with open("input.txt") as f:
        keys = list(map(int, f.readline().split()))
        if keys[0] != 0:
            tree = SearchTree(keys[0])
            i = 0
            while keys[i] != 0:
                tree.insert(keys[i])
                i += 1
            print(tree.height())
        else:
            print(0)
