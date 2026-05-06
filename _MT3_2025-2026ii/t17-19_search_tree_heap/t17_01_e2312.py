from sys import setrecursionlimit

setrecursionlimit(1000000)


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left: SearchTree | None = None
        self.right: SearchTree | None = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = SearchTree(key)
                    break
            elif key > node.key:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = SearchTree(key)
                    break
            else:
                break

    def height(self):
        l = 0 if self.left is None else self.left.height()
        r = 0 if self.right is None else self.right.height()
        return 1 + max(l, r)


if __name__ == '__main__':
    f = open("input.txt")
    lst = list(map(int, f.readline().split()))
    if lst[0] == 0:
        print(0)
    else:
        tree = SearchTree(lst[0])
        for i in range(1, len(lst)):
            if lst[i] == 0:
                break
            tree.insert(lst[i])

        print(tree.height())

    f.close()
