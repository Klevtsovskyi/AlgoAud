from collections import deque


class Tree:

    def __init__(self, key, parent=None):
        self.key = key
        self.children = []
        self.parent = parent

    def dfs(self, key):
        if self.key == key:
            return self
        for child in self.children:
            node = child.dfs(key)
            if node is not None:
                return node

    def dfs_stack(self, key):
        stack = [self]
        while stack:
            node = stack.pop()
            if node.key == key:
                return node
            for child in node.children:
                stack.append(child)

    def bfs(self, key):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self, parent_key, key):
        parent = self.bfs(parent_key)
        node = Tree(key, parent)
        parent.children.append(node)

    def get(self, a, b):
        node = self.bfs(a)
        came_from = None
        while node is not None:
            if node.key == b:
                return node.key
            for child in node.children:
                if child is not came_from and child.bfs(b) is not None:
                    return node.key

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
