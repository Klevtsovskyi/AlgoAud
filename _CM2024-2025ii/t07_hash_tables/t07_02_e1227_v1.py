import math

EMPTY = None


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:

    M = 31

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | str] = [EMPTY for _ in range(size)]

    def _rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.add(_keys[i])

    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = h * self.M + ord(s[i])
        return h % self._size

    def add(self, key: str):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size

        self._count += 1
        self._keys[i] = key

    def __iter__(self):
        res = []
        for i in range(self._size):
            if self._keys[i] is not EMPTY:
                res.append(self._keys[i])
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
