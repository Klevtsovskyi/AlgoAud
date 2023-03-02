import math


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Dict:

    X = 13

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys = [None for _ in range(size)]
        self._values = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for c in s:
            h = h * self.X + ord(c)
        return h % self._size

#   cn + c_{n-1} X + c_{n-2} X^{2} + ... + c_0 X^{n} =
#   cn + X (c_{n-1} + X (c_{n-2} + ...) ... + X (c_{0}) ... )

    def _rehash(self):
        _size = self._size
        _keys = self._keys
        _values = self._values

        self._size = 2 * _size + 1
        while is_prime(self._size):
            self._size += 2

        self.__init__(self._size)
        for i in range(_size):
            if _keys[i] is not None:
                self.set(_keys[i], _values[i])

    def set(self, key, value):
        if self._count > 0.7 * self._size:
            self._rehash()

        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                self._values[curr] = value
                return
            curr = (curr + 1) % self._size

        self._keys[curr] = key
        self._values[curr] = value
        self._count += 1

    def get(self, key):
        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                return self._values[curr]
            curr = (curr + 1) % self._size

    def keys(self):
        res = []
        for key in self._keys:
            if key is not None:
                res.append(key)
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
