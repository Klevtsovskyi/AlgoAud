from collections import deque


class Tree:

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []

    def bfs(self, key, came_from=None):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            if node is came_from:
                continue
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)
        return None

    def add(self, parent_key, key):
        parent = self.bfs(parent_key)
        node = Tree(key, parent)
        parent.children.append(node)

    def lca(self, i, j):
        node = self.bfs(i)
        came_from = None
        while True:
            if node.bfs(j, came_from) is not None:
                return node.key
            came_from = node
            node = node.parent


if __name__ == '__main__':
    f = open("input.txt")
    k = int(f.readline())
    tree = Tree(1)
    for _ in range(k):
        cmd, *args = f.readline().split()
        a, b = map(int, args)
        if cmd == "ADD":
            tree.add(a, b)
        elif cmd == "GET":
            print(tree.lca(a, b))
    f.close()
