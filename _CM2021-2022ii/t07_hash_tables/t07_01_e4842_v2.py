class DictNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dict:

    X = 29

    def __init__(self, size=200003):
        self._size = size
        self._table = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for c in s:
            h = h * Dict.X + ord(c)
        return h % self._size

    def set(self, key, value):
        curr = self.hash(key)
        node = self._table[curr]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        node = DictNode(key, value)
        node.next = self._table[curr]
        self._table[curr] = node

    def get(self, key):
        curr = self.hash(key)
        node = self._table[curr]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

    def keys(self):
        result = []
        for node in self._table:
            while node is not None:
                result.append(node.key)
                node = node.next
        return result

    def __contains__(self, key):
        return False if self.get(key) is None else True

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)


if __name__ == "__main__":
    with open("input.txt") as f:
        dct = Dict()
        for line in f:
            eng, latins = line.rstrip().split(" - ")
            latins = latins.split(", ")
            for latin in latins:
                if latin in dct:
                    dct[latin].append(eng)
                else:
                    dct[latin] = [eng]

        keys = sorted(dct.keys())
        print(len(keys))
        for key in keys:
            print(key, end=" - ")
            print(*dct[key], sep=", ")
