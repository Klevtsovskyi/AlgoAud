"""
https://www.eolymp.com/uk/submissions/11032894
"""


from collections import deque


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key == node.key:
                return

            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                else:
                    node = node.left

            else:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right

    def count(self):
        _count = 0
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            node = queue.popleft()
            _count += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return _count

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
            print(tree.count())
