"""
https://www.e-olymp.com/uk/problems/4842
"""


class Dict:

    M = 200003
    N = 31
    K = 1

    # ord(c0) + x * (ord(c1) + x * (ord(c2) + ... ) ... )
    @staticmethod
    def hash(s):
        h = 0
        for c in s:
            h = h * Dict.N + ord(c)
        return h % Dict.M

    def __init__(self):
        self._keys = [None for _ in range(Dict.M)]
        self._values = [None for _ in range(Dict.M)]

    def add(self, key, value):
        cur = Dict.hash(key)
        while self._keys[cur] is not None:
            if self._keys[cur] == key:
                self._values[cur] = value
                return
            cur = (cur + Dict.K) % Dict.M
        self._keys[cur] = key
        self._values[cur] = value

    def get(self, key):
        cur = Dict.hash(key)
        while self._keys[cur] is not None:
            if self._keys[cur] == key:
                return self._values[cur]
            cur = (cur + Dict.K) % Dict.M

    def keys(self):
        result = []
        for key in self._keys:
            if key is not None:
                result.append(key)
        return result

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self[key] is not None else False


if __name__ == '__main__':
    with open("input.txt") as inp:
        dct = Dict()
        for line in inp:
            eng, latins = line.rstrip().split(" - ")
            for latin in latins.split(", "):
                if latin in dct:
                    dct[latin].append(eng)
                else:
                    dct[latin] = [eng]

        lst = sorted(dct.keys())
        print(len(lst))
        for latin in lst:
            print(latin, end=" - ")
            print(*dct[latin], sep=", ")
