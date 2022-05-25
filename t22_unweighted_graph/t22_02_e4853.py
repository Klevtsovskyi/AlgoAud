"""
https://www.eolymp.com/uk/submissions/11113604
"""


from collections import deque


class Graph:

    def __init__(self, size):
        self.vertices = {}
        for i in range(1, size + 1):
            self.vertices[i] = set()

    def add_edge(self, source, destination):
        self.vertices[source].add(destination)
        self.vertices[destination].add(source)

    def get_path(self, start, finish):
        sources = {start: None}
        queue = deque()
        queue.append(start)
        while len(queue) > 0:
            curr = queue.popleft()
            if curr == finish:
                break

            for neighbour in self.vertices[curr]:
                if neighbour not in sources:
                    queue.append(neighbour)
                    sources[neighbour] = curr
        else:
            return -1

        path = []
        while curr is not None:
            path.append(curr)
            curr = sources[curr]

        path.reverse()
        return path


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        a, b = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, f.readline().split()))

        path = graph.get_path(a, b)
        if path == -1:
            print(path)
        else:
            print(len(path) - 1)
            print(*path)
