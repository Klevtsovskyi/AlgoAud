EMPTY = "EMPTY"


def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class Dict:

    M = 29

    def __init__(self, size=11):
        self._size: int = size
        self._keys: list = [EMPTY for _ in range(size)]
        self._values: list = [EMPTY for _ in range(size)]
        self.count: int = 0

    # H(s) = C0 M^n + C1 M^{n-1} + ... + C[n-1] M + C[n] =
    #      = (C0 M^{n-1} + C1 M^{n-2} + ... + C[n-2] M + C[n-1]) M + C[n] =
    #      = ((C0 M^{n-1} + C1 M^{n-2} + ... + C[n-2]) M + C[n-1]) M + C[n] =
    #      = ((...(C0 M + C1) M + ... + C[n-2]) M + C[n-1]) M + C[n]

    # S = C0C1C2
    # H(S) = C0 M^2 + C1 M + C2 = (C0 M + C1) M + C2
    def hash(self, key: str):
        h = 0
        for i in range(len(key)):
            h = h * self.M + ord(key[i])
        return h % self._size

    def rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values
        self.__init__(self._size)

        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, ):
                self.set(_keys[i], _values[i])

    def set(self, key: str, value: str) -> None:
        if self.count > 0.7 * self._size:
            self.rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return

            i = (i + 1) % self._size

        self.count += 1
        self._keys[i] = key
        self._values[i] = value

    def get(self, key: str) -> str | None:
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size
        return None

    def keys(self):
        res = []
        for i in range(self._size):
            if self._keys[i] is not EMPTY:
                res.append(self._keys[i])
        return res

    def __contains__(self, key):
        return self.get(key) is not None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)


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
