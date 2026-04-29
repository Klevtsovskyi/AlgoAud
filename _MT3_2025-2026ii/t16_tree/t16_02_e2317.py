from collections import deque


class Tree:

    def __init__(self, key):
        self.key = key
        self.children: list[Tree] = []
        self.parent: Tree | None = None

    def bfs(self, key, came_from=None):
        queue: deque[Tree] = deque()
        queue.append(self)
        while len(queue) > 0 :
            node = queue.popleft()
            if node is came_from:
                continue
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)
        return None

    def dfs(self):
        print(self.key, end=" ")
        for child in self.children:
            child.dfs()

    def add(self, parent_key, child_key):
        parent = self.bfs(parent_key)
        if parent is None:
            raise RuntimeError
        node = Tree(child_key)
        node.parent = parent
        parent.children.append(node)

    def get(self, i, j):
        node = self.bfs(i)
        came_from = None
        while node is not None:
            if node.bfs(j, came_from) is not None:
                return node.key
            came_from = node
            node = node.parent
        return 0


if __name__ == '__main__':
    f = open("input.txt")
    tree = Tree(1)
    k = int(f.readline())
    for _ in range(k):
        cmd, *args = f.readline().split()
        a, b = map(int, args)
        if cmd == "ADD":
            tree.add(a, b)
        elif cmd == "GET":
            print(tree.get(a, b))
    # tree.dfs()
    f.close()
