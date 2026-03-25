N = 29

EMPTY = "EMPTY"
DELETED = "DELETED"


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class HashTable:

    def __init__(self, size=11):
        self._keys = [EMPTY for _ in range(size)]
        self._values = [EMPTY for _ in range(size)]
        self._size = size
        self._count = 0

    def hash(self, key: str):
        h = 0
        for i in range(len(key)):
            h = h * N + ord(key[i])
        return h % self._size

    def rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values

        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, DELETED):
                self.set(_keys[i], _values[i])

    def set(self, key: str, value: str):
        if self._count > 0.7 * self._size:
            self.rehash()

        i = self.hash(key)
        j = -1
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return

            if j == -1 and self._keys[i] == DELETED:
                j = i

            i = (i + 1) % self._size

        if j == -1:
            j = i
            self._count += 1

        self._keys[j] = key
        self._values[j] = value

    def get(self, key: str):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size
        return None

    def delete(self, key: str):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._keys[i] = DELETED
                return
            i = (i + 1) % self._size

    def keys(self):
        res = []
        for i in range(self._size):
            if self._keys[i] not in (EMPTY, DELETED):
                res.append(self._keys[i])
        return res



if __name__ == '__main__':
    f = open("input.txt")
    dct = HashTable()
    for line in f:
        eng, latins = line.strip().split(" - ")
        latins = latins.split(", ")
        for latin in latins:
            if dct.get(latin) is not None:
                dct.get(latin).append(eng)
            else:
                dct.set(latin, [eng])

    latins = sorted(dct.keys())
    print(len(latins))
    for latin in latins:
        print(latin, end=" - ")
        print(*sorted(dct.get(latin)), sep=", ")
    f.close()
