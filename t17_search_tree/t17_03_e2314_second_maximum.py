"""
https://www.e-olymp.com/uk/problems/2314
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

    def second_maximum(self):
        parent = node = self
        while node.has_right():
            parent = node
            node = node.right
        if node.has_left():
            node = node.left
            while node.has_right():
                node = node.right
            return node.key
        else:
            return parent.key


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
        print(root.second_maximum())
