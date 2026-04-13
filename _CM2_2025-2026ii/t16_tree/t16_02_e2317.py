
class Tree:
    def __init__(self, key, parent=None):
        self.parent = parent
        self.key = key
        self.children = []

    def __str__(self):
        return str(self.key)

    def dfs(self, key):
        if self.key == key:
            return self
        for child in self.children:
            node = child.dfs(key)
            if node is not None:
                return node

    def add(self, parent_key, key):
        parent = self.dfs(parent_key)
        node = Tree(key, parent)
        parent.children.append(node)

    def get(self, a, b):
        node = self.dfs(a)
        came_from = None

        while node is not None:
            if node.key == b:
                return node.key
            for child in node.children:
                if child is not came_from and child.dfs(b) is not None:
                    return node
            came_from = node
            node = node.parent

    def execute(self, command):
        method, *args = command.split()
        method = method.lower()
        args = map(int, args)
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        tree = Tree(1)
        k = int(f.readline())
        for _ in range(k):
            line = f.readline()
            result = tree.execute(line)
            if result is not None:
                print(result)




