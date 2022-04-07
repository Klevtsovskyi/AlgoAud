class Dict:

    X = 29

    def __init__(self, size=200003):
        self._size = size
        self._keys = [None for _ in range(size)]
        self._values = [None for _ in range(size)]

    # (x^n + ord(c0) + x^(n-1) * ord(c1) + x^(n-2) * ord(c2) + ... + ord(cn)) % size
    # ord(cn) + x * (ord(c(n-1)) + x * (ord(c(n-2)) + ... ) ... ) % size
    def hash(self, s):
        h = 0
        for c in s:
            h = h * Dict.X + ord(c)
        return h % self._size

    def set(self, key, value):
        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                self._values[curr] = value
                return
            curr = (curr + 1) % self._size

        self._keys[curr] = key
        self._values[curr] = value

    def get(self, key):
        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                return self._values[curr]
            curr = (curr + 1) % self._size

    def keys(self):
        result = []
        for key in self._keys:
            if key is not None:
                result.append(key)
        return result

    def __contains__(self, key):
        return False if self.get(key) is None else True

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)


if __name__ == "__main__":
    with open("input.txt") as f:
        dct = Dict()
        for line in f:
            eng, latins = line.rstrip().split(" - ")
            latins = latins.split(", ")
            for latin in latins:
                if latin in dct:
                    dct[latin].append(eng)
                else:
                    dct[latin] = [eng]

        keys = sorted(dct.keys())
        print(len(keys))
        for key in keys:
            print(key, end=" - ")
            print(*dct[key], sep=", ")
