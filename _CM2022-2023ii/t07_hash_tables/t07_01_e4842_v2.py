class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dict:

    X = 13

    def __init__(self, size=100001):
        self._size = size
        self._items = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for c in s:
            h = h * self.X + ord(c)
        return h % self._size

#   cn + c_{n-1} X + c_{n-2} X^{2} + ... + c_0 X^{n} =
#   cn + X (c_{n-1} + X (c_{n-2} + ...) ... + X (c_{0}) ... )

    def set(self, key, value):
        curr = self.hash(key)
        node = self._items[curr]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        node = Node(key, value)
        node.next = self._items[curr]
        self._items[curr] = node

    def get(self, key):
        curr = self.hash(key)
        node = self._items[curr]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

    def keys(self):
        res = []
        for node in self._items:
            while node is not None:
                res.append(node.key)
                node = node.next
        return res

    def __contains__(self, key):
        return False if self.get(key) is None else True

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)


if __name__ == "__main__":
    dct = Dict()
    with open("input.txt") as f:
        for line in f:
            eng, latins = line.strip().split(" - ")
            latins = latins.split(", ")
            for latin in latins:
                if latin in dct:
                    dct[latin].append(eng)
                else:
                    dct[latin] = [eng]

        latins = sorted(dct.keys())
        print(len(latins))
        for latin in latins:
            print(latin, end=" - ")
            print(*dct[latin], sep=", ")
