import sys
from collections import deque

sys.setrecursionlimit(1000000)


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                else:
                    node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right
            else:
                break

    def count(self):
        left_count = 0 if self.left is None else self.left.count()
        right_count = 0 if self.right is None else self.right.count()
        return left_count + right_count + 1

    def count_bfs(self):
        count = 0
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            count += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return count


if __name__ == "__main__":
    with open("input.txt") as f:
        keys = list(map(int, f.readline().split()))
        if keys[0] != 0:
            tree = SearchTree(keys[0])
            i = 0
            while keys[i] != 0:
                tree.insert(keys[i])
                i += 1
            print(tree.count_bfs())
        else:
            print(0)
