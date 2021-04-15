"""
https://www.e-olymp.com/uk/problems/2316
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

    def print_leaves(self):
        leaves = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node.has_right():
                stack.append(node.right)
            if node.has_left():
                stack.append(node.left)
            if not (node.has_left() or node.has_right()):
                leaves.append(node.key)
        return leaves


if __name__ == '__main__':
    lst = [int(n) for n in input().split()]
    if lst[0] == 0:
        print()
    else:
        root = SearchTree(lst[0])
        i = 1
        while lst[i] != 0:
            root.insert(lst[i])
            i += 1
        print(*root.print_leaves())
