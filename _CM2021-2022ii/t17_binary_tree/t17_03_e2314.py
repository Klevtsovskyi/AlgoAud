"""
https://www.eolymp.com/uk/submissions/11033025
"""


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

    def second_maximum(self):
        parent = None
        node = self
        while node.right is not None:
            parent = node
            node = node.right

        if node.left is None:
            return parent.key

        node = node.left
        while node.right is not None:
            node = node.right
        return node.key

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
            print(tree.second_maximum())
