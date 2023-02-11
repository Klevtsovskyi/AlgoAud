class SetNode:

    def __init__(self, key):
        self.key = key
        self.next = None


class Set:

    X = 29

    def __init__(self, size=200003):
        self._size = size
        self._table = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for c in s:
            h = h * Set.X + ord(c)
        return h % self._size

    def add(self, key):
        curr = self.hash(key)
        node = self._table[curr]
        while node is not None:
            if node.key == key:
                return
            node = node.next

        node = SetNode(key)
        node.next = self._table[curr]
        self._table[curr] = node

    def __iter__(self):
        result = []
        for node in self._table:
            while node is not None:
                result.append(node.key)
                node = node.next
        return iter(result)


if __name__ == "__main__":
    # f = open("input.txt")
    words = Set()
    # for line in f:
    while True:
        try:
            line = input()
            word = ""
            for c in line:
                if c.isalpha():
                    word += c.lower()
                elif word:
                    words.add(word)
                    word = ""
            if word:
                words.add(word)
        except EOFError:
            break

    print(*sorted(words), sep="\n")
