class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Node | None = None


class Dict:

    M = 29

    def __init__(self, size=1000003):
        self.size = size
        self.slots: list[Node | None] = [None for _ in range(size)]
        self.count = 0

    # H(s) = C0 * M^n + C1 * M^{n-1} + ... + C[N-1] * M^1 + CN * M^0
    # ((... M + C[N-2]) * M + C[N-1]) * M + CN
    # S = C0 C1 C2
    # C0 M^2 + C1 M + C2
    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = h * self.M + ord(s[i])
        return h % self.size

    def set(self, key, value):
        i = self.hash(key)
        node = self.slots[i]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        self.count += 1
        new_node = Node(key, value)
        new_node.next = self.slots[i]
        self.slots[i] = new_node

    def get(self, key):
        i = self.hash(key)
        node = self.slots[i]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def keys(self):
        res = []
        for i in range(self.size):
            node = self.slots[i]
            while node is not None:
                res.append(node.key)
                node = node.next
        return res

    def __contains__(self, key):
        return self.get(key) is not None

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__ == '__main__':
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
