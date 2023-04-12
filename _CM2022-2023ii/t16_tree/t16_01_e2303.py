class PrefixTree:

    def __init__(self):
        self.children = {}

    def add_child(self, digit):
        self.children[digit] = PrefixTree()

    def has_child(self, digit):
        return digit in self.children

    def get_child(self, digit):
        return self.children[digit]

    def is_leaf(self):
        return not bool(self.children)

    def add_phone(self, phone: str):
        node = self
        i = 0
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


if __name__ == "__main__":
    with open("input.txt") as f:
        t = int(f.readline())
        for _ in range(t):
            tree = PrefixTree()
            n = int(f.readline())
            result = True
            for __ in range(n):
                phone_number = f.readline().rstrip()
                if result:
                    result = tree.add_phone(phone_number)
            print("YES" if result else "NO")
