"""
https://www.e-olymp.com/uk/problems/6125
"""


class Queue:

    def __init__(self): self.items = []
    def empty(self): return len(self.items) == 0
    def push(self, n): self.items.append(n); return "ok"
    def pop(self): return self.items.pop(0)
    def front(self): return self.items[0]
    def size(self): return len(self.items)
    def clear(self): self.items.clear(); return "ok"
    def exit(self): return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open("input.txt") as inp:
        queue = Queue()
        for line in inp:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
