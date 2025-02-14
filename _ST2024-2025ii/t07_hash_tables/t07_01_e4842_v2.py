class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dict:

    M = 13

    def __init__(self, size=1000003):
        self._size = size
        self._slots: list[None | Node] = [None for _ in range(size)]

    def hash(self, s: str) -> int:
        h = 0
        for c in s:
            h = h * self.M + ord(c)
        return h % self._size

    def set(self, key: str, value: list[str]):
        i = self.hash(key)
        node = self._slots[i]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        node = Node(key, value)
        node.next = self._slots[i]
        self._slots[i] = node

    def get(self, key: str):
        i = self.hash(key)
        node = self._slots[i]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

    def keys(self):
        res = []
        for i in range(self._size):
            node = self._slots[i]
            while node is not None:
                res.append(node.key)
                node = node.next
        return res

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True


if __name__ == "__main__":
    f = open("input.txt")
    dct = Dict()
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
        print(*sorted(dct[latin]), sep=", ")
    f.close()
