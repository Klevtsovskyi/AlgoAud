import sys
sys.setrecursionlimit(100500)


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

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()

    # def height(self):
    #     left_height = 0 if self.left is None else self.left.height()
    #     right_height = 0 if self.right is None else self.right.height()
    #     return max(left_height, right_height) + 1


if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    if lst[0] == 0:
        print(0)
    else:
        tree = SearchTree(lst[0])
        for i in range(1, len(lst) - 1):
            if lst[i] == 0:
                break
            tree.insert(lst[i])
        # print(tree.height())
