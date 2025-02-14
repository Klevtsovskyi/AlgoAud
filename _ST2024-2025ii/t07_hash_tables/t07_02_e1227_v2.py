class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class Set:

    M = 13

    def __init__(self, size=1000003):
        self._size = size
        self._slots: list[None | Node] = [None for _ in range(size)]

    def hash(self, s: str) -> int:
        h = 0
        for c in s:
            h = h * self.M + ord(c)
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

    def __iter__(self):
        res = []
        for i in range(self._size):
            node = self._slots[i]
            while node is not None:
                res.append(node.key)
                node = node.next
        return iter(res)


if __name__ == "__main__":
    f = open("input.txt")
    words = Set()
    # while True:
    for line in f:
    #     try:
    #         line = input()
    #     except EOFError:
    #         break
        word = ""
        for c in line:
            if c.isalpha():
                word += c.lower()
            elif word:
                words.add(word)
                word = ""
        if word:
            words.add(word)

    print(*sorted(iter(words)), sep="\n")
    f.close()
