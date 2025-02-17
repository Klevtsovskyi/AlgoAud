class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class Set:

    M = 31

    def __init__(self, size=1000003):
        self._size = size
        self._count = 0
        self._slots: list[None | Node] = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = h * self.M + ord(s[i])
        return h % self._size

    def add(self, key: str):
        i = self.hash(key)
        node = self._slots[i]
        while node is not None:
            if node.key == key:
                return
            node = node.next

        node = Node(key)
        node.next = self._slots[i]
        self._slots[i] = node
        self._count += 1

    def __iter__(self):
        res = []
        for i in range(self._size):
            node = self._slots[i]
            while node is not None:
                res.append(node.key)
                node = node.next
        return iter(res)


if __name__ == '__main__':
    # f = open("input.txt")
    words = Set()
    # for line in f:
    while True:
        word = ""
        try:
            line = input()
        except EOFError:
            break
        for c in line:
            if c.isalpha():
                word += c.lower()
            elif word:
                words.add(word)
                word = ""
        if word:
            words.add(word)

    print(*sorted(words), sep="\n")
    # f.close()
