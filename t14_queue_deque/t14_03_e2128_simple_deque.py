"""
https://www.e-olymp.com/uk/problems/6128
"""


class Deque:

    def __init__(self): self.items = []
    def empty(self): return len(self.items) == 0
    def push_front(self, n): self.items.insert(0, n); return "ok"
    def push_back(self, n): self.items.append(n); return "ok"
    def pop_front(self): return self.items.pop(0)
    def pop_back(self): return self.items.pop()
    def front(self): return self.items[0]
    def back(self): return self.items[-1]
    def size(self): return len(self.items)
    def clear(self): self.items.clear(); return "ok"
    def exit(self): return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as inp:
        deque = Deque()
        for line in inp:
            result = deque.execute(line)
            print(result)
            if result == "bye":
                break
