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


if __name__ == "__main__":
    with open("input.txt") as f:
        keys = list(map(int, f.readline().split()))
        if keys[0] != 0:
            tree = SearchTree(keys[0])
            i = 0
            while keys[i] != 0:
                tree.insert(keys[i])
                i += 1
            print(tree.second_maximum())
        else:
            print(0)
