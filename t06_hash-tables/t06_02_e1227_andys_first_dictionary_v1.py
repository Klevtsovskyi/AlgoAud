"""
https://www.e-olymp.com/uk/problems/1227
"""


class Set:

    M = 200003
    N = 31
    K = 1

    # ord(c0) + x * (ord(c1) + x * (ord(c2) + ... ) ... )
    @staticmethod
    def hash(s):
        h = 0
        for c in s:
            h = h * Set.N + ord(c)
        return h % Set.M

    def __init__(self):
        self.items = [None for _ in range(Set.M)]

    def add(self, item):
        cur = Set.hash(item)
        while self.items[cur] is not None:
            if self.items[cur] == item:
                return
            cur = (cur + Set.K) % Set.M
        self.items[cur] = item

    def __iter__(self):
        result = []
        for item in self.items:
            if item is not None:
                result.append(item)
        return iter(result)


if __name__ == '__main__':
    set_of_words = Set()
    # inp = open("input.txt")
    while True:
        try:
            # line = inp.readline()
            # if line == "":
            #     break
            line = input()
            word = ""
            for c in line:
                if c.isalpha():
                    word += c.lower()
                elif word:
                    set_of_words.add(word)
                    word = ""
            if word:
                set_of_words.add(word)
        except EOFError:
            break

    print(*sorted(set_of_words), sep="\n")
