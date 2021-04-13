"""
https://www.e-olymp.com/uk/problems/2303
"""


class Tree:

    def __init__(self):
        self.children = {}

    def has_children(self):
        return bool(self.children)

    def has_child(self, key):
        return key in self.children

    def add_child(self, key):
        self.children[key] = Tree()

    def get_child(self, key):
        return self.children[key]

    def clear(self):
        self.children.clear()

    def add(self, phone: str):
        node = self
        i = 0
        # Пробігаємо по ланцюжку існуючих дітей
        while i < len(phone) and node.has_child(phone[i]):
            node = node.get_child(phone[i])
            i += 1
        # Якщо всі цифри номера вже є в довіднику,
        # то даний номер є несумісним
        if i == len(phone):
            return False
        # Якщо в існуючому ланцюжку не залишилось дітей,
        # то даний номер несумісний
        if i > 0 and not node.has_children():
            return False
        # Створюємо ланцюжок
        while i < len(phone):
            node.add_child(phone[i])
            node = node.get_child(phone[i])
            i += 1
        return True


if __name__ == '__main__':
    with open("input.txt") as inp:
        tree = Tree()
        t = int(inp.readline())
        for _ in range(t):
            n = int(inp.readline())
            consistent = True
            for __ in range(n):
                phone = inp.readline().rstrip()
                # Якщо знайшли хоча б один несумісний номер,
                # немає смислу перевіряти далі
                if consistent:
                    consistent = tree.add(phone)
            print("YES" if consistent else "NO")
            tree.clear()
