"""
https://www.e-olymp.com/uk/problems/4842
"""


class DictNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dict:

    M = 200003
    N = 31

    # ord(c0) + x * (ord(c1) + x * (ord(c2) + ... ) ... )
    @staticmethod
    def hash(s):
        h = 0
        for c in s:
            h = h * Dict.N + ord(c)
        return h % Dict.M

    def __init__(self):
        self.table = [None for _ in range(Dict.M)]

    def add(self, key, value):
        i = Dict.hash(key)
        node = self.table[i]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        node = DictNode(key, value)
        node.next = self.table[i]
        self.table[i] = node

    def get(self, key):
        i = Dict.hash(key)
        node = self.table[i]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

    def keys(self):
        result = []
        for node in self.table:
            while node is not None:
                result.append(node.key)
                node = node.next
        return result

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self[key] is not None else False


if __name__ == '__main__':
    with open("input.txt") as inp:
        dct = Dict()
        for line in inp:
            eng, latins = line.rstrip().split(" - ")
            for latin in latins.split(", "):
                if latin in dct:
                    dct[latin].append(eng)
                else:
                    dct[latin] = [eng]

        lst = sorted(dct.keys())
        print(len(lst))
        for latin in lst:
            print(latin, end=" - ")
            print(*dct[latin], sep=", ")
