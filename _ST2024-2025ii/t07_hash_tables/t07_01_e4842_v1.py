import math

EMPTY = None


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Dict:

    M = 13

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | str] = [EMPTY for _ in range(size)]
        self._values: list[EMPTY | list[str]] = [EMPTY for _ in range(size)]

    def _rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values
        self.__init__(self._size)

        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.set(_keys[i], _values[i])

    # s = c0c1c2c3...cn
    # h = c0 * M^n + c1 * M^{n-1} + ... c{n-2} * M^2 + c{n-1} * M + cn
    # (((c0)... + c{n-2}) * M + c{n-1}) * M + cn
    # c0c1c2 -> h = c0 * M^2 + c1 * M + c2
    def hash(self, s: str) -> int:
        h = 0
        for c in s:
            h = h * self.M + ord(c)
        return h % self._size

    def set(self, key: str, value: list[str]):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return
            i = (i + 1) % self._size

        self._count += 1
        self._keys[i] = key
        self._values[i] = value

    def get(self, key: str):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size

    def keys(self):
        res = []
        for i in range(self._size):
            if self._keys[i] is not EMPTY:
                res.append(self._keys[i])
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
