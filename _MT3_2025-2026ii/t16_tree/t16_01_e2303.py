class PrefixTree:

    def __init__(self):
        self.children: dict[int, PrefixTree] = {}

    def get_child(self, i): return self.children[i]
    def has_child(self, i): return i in self.children
    def add_child(self, i): self.children[i] = PrefixTree()
    def is_leaf(self): return len(self.children) == 0

    def add_phone(self, phone: str):
        i = 0
        node = self
        while i < len(phone) and node.has_child(phone[i]):
            node = node.get_child(phone[i])
            i += 1

        if i == len(phone):
            return False

        if i > 0 and node.is_leaf():
            return False

        while i < len(phone):
            node.add_child(phone[i])
            node = node.get_child(phone[i])
            i += 1

        return True


if __name__ == '__main__':
    f = open("input.txt")
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        tree = PrefixTree()
        result = True
        for __ in range(n):
            phone_number = f.readline().rstrip()
            if result:
                result = tree.add_phone(phone_number)
        if result:
            print("YES")
        else:
            print("NO")

    f.close()
