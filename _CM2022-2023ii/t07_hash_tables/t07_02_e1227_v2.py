import math


class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:

    X = 13

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for c in s:
            h = h * self.X + ord(c)
        return h % self._size

#   cn + c_{n-1} X + c_{n-2} X^{2} + ... + c_0 X^{n} =
#   cn + X (c_{n-1} + X (c_{n-2} + ...) ... + X (c_{0}) ... )

    def _rehash(self):
        _size = self._size
        _keys = iter(self)

        self._size = 2 * _size + 1
        while not is_prime(self._size):
            self._size += 2

        self.__init__(self._size)
        for key in _keys:
            self.add(key)

    def add(self, key):
        if self._count > 0.7 * self._size:
            self._rehash()

        curr = self.hash(key)
        node = self._keys[curr]
        while node is not None:
            if node.key == key:
                return
            node = node.next

        node = Node(key)
        node.next = self._keys[curr]
        self._keys[curr] = node
        self._count += 1

    def __iter__(self):
        res = []
        for node in self._keys:
            while node is not None:
                res.append(node.key)
                node = node.next
        return iter(res)


if __name__ == "__main__":
    words = Set()
    # f = open("input.txt")
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
