EMPTY = None


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class Dict:

    M = 29

    def __init__(self, size=11):
        self.size = size
        self._keys = [EMPTY for _ in range(size)]
        self._values = [EMPTY for _ in range(size)]
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

    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2
        _keys = self._keys
        _values = self._values
        self.__init__(self.size)
        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.set(_keys[i], _values[i])

    def set(self, key, value):
        if self.count > 0.5 * self.size:
            self.rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return
            i = (i + 1) % self.size

        self.count += 1
        self._keys[i] = key
        self._values[i] = value

    def get(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self.size
        return None

    def keys(self):
        res = []
        for i in range(self.size):
            if self._keys[i] is not EMPTY:
                res.append(self._keys[i])
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
