class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self,key):
        if key <self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def count(self):
        left_count = 0 if self.left is None else self.left.count()
        right_count = 0 if self.right is None else self.right.count()
        return left_count + right_count + 1


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
        print(self.key, end= " ")
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()




if __name__ == "__main__":
    with open ("input.txt") as f:
        keys = list(map(int, f.readline().split()))
        if keys[0] != 0:
            tree = BinaryTree(keys[0])
            i = 0
            while keys[i] != 0:
                tree.insert(keys[i])
                i += 1
            tree.print()