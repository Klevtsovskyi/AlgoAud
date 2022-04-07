class Set:

    X = 29

    def __init__(self, size=200003):
        self._size = size
        self._keys = [None for _ in range(size)]

    def hash(self, s):
        h = 0
        for c in s:
            h = h * Set.X + ord(c)
        return h % self._size

    def add(self, key):
        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                return
            curr = (curr + 1) % self._size

        self._keys[curr] = key

    def __iter__(self):
        result = []
        for key in self._keys:
            if key is not None:
                result.append(key)
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
