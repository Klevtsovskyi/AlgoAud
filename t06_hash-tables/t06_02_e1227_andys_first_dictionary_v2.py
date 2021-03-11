"""
https://www.e-olymp.com/uk/problems/1227
"""


class SetNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class Set:

    M = 200003
    N = 31

    # ord(c0) + x * (ord(c1) + x * (ord(c2) + ... ) ... )
    @staticmethod
    def hash(s):
        h = 0
        for c in s:
            h = h * Set.N + ord(c)
        return h % Set.M

    def __init__(self):
        self.table = [None for _ in range(Set.M)]

    def add(self, item):
        i = Set.hash(item)
        node = self.table[i]
        while node is not None:
            if node.item == item:
                return
            node = node.next

        node = SetNode(item)
        node.next = self.table[i]
        self.table[i] = node

    def __iter__(self):
        result = []
        for node in self.table:
            while node is not None:
                result.append(node.item)
                node = node.next
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
