"""
https://www.eolymp.com/uk/submissions/11016354
"""


from collections import deque


class Tree:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def bfs(self, key):
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            node = queue.popleft()
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self, parent_key, child_key):
        parent = self.bfs(parent_key)
        node = Tree(child_key)
        node.parent = parent
        parent.children.append(node)

    def get(self, i, j):
        node = self.bfs(i)
        came_from = None
        while node is not None:
            if node.key == j:
                return node.key

            for child in node.children:
                if child is not came_from:
                    if child.bfs(j) is not None:
                        return node.key

            came_from = node
            node = node.parent

        return came_from.key

    def execute(self, command):
        method, *args = command.split()
        method = method.lower()
        args = map(int, args)
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        k = int(f.readline())
        tree = Tree(1)
        for _ in range(k):
            line = f.readline()
            result = tree.execute(line)
            if result is not None:
                print(result)
