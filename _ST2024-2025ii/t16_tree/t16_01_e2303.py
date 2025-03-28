class PrefixTree:

    def __init__(self):
        self.children = {}

    def has_child(self, d):
         return d in self.children

    def get_child(self, d):
        return self.children[d]

    def set_child(self, d):
        self.children[d] = PrefixTree()

    def is_leaf(self):
        return len(self.children) == 0

    def add_phone(self, phone: str):
        i = 0
        node = self
        while i < len(phone) and node.has_child(phone[i]):
            node = node.get_child(phone[i])
            i += 1

        if i > 0 and node.is_leaf():
            return "NO"
        if i == len(phone):
            return "NO"

        while i < len(phone):
            node.set_child(phone[i])
            node = node.get_child(phone[i])
            i += 1

        return "YES"


if __name__ == '__main__':
    f = open("input.txt")
    t  = int(f.readline())
    for _ in range(t):
        tree = PrefixTree()
        n = int(f.readline())

        compatible = "YES"
        for __ in range(n):
            phone = f.readline().rstrip()
            if compatible == "NO":
                continue
            if tree.add_phone(phone) == "NO":
                compatible = "NO"
        print(compatible)

    f.close()