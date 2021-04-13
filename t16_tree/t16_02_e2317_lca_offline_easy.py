"""
https://www.e-olymp.com/uk/problems/2317
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
        while queue:
            node = queue.popleft()
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self, a, b):
        parent = self.bfs(a)
        node = Tree(b)
        node.parent = parent
        parent.children.append(node)

    def get(self, a, b):
        node = self.bfs(a)
        came_from = None
        while node is not None:
            if node.key == b:
                return node.key
            for child in node.children:
                if child is not came_from:
                    if child.bfs(b) is not None:
                        return node.key
            came_from = node
            node = node.parent
        return came_from.key

    def execute(self, command):
        method, *args = command.split()
        method = method.lower()
        args = map(int, args)
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as inp:
        tree = Tree(1)
        k = int(inp.readline())
        for _ in range(k):
            result = tree.execute(inp.readline())
            if result is not None:
                print(result)
