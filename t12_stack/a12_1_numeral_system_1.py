''' a12_1_numeral_system_1.py

Перевести число a, записане у двійковій системі числення, у шістнадяткову.
Вивести число a у шістнадцятковій системі числення без ведучих нулів.

Вхідні дані:
Число, записане у двійковій системі числення, 0 < довжина числа ≤ 104.

Вихідні дані:
Виведіть число, переведене у шістнадцяткову систему числення, записане за
допомогою символів '0', …, '9' та 'A', …, 'F'.
'''

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.len = 0

    def push(self, item):
        node = Node(item)
        node.next, self.top = self.top, node
        self.len += 1

    def pop(self):
        if self.top:
            item, self.top = self.top.item, self.top.next
            self.len -= 1
            return item

    def back(self):
        return self.top.item if self.top else None

    def size(self):
        return self.len

    def clear(self):
        self.top = None
        self.len = 0


def convert(number: str, from_base=2, to_base=16):

    stack = Stack()

    for d in number:
        stack.push(d)

    decimal = 0
    base = 1
    while stack.size():
        decimal += base * int(stack.pop())
        base *= from_base

    while decimal > 0:
        stack.push(decimal % to_base)
        decimal //= to_base

    converted = ''
    while stack.size():
        converted += get_char(stack.pop())

    return converted

def get_char(digit):
    return str(digit) if digit <= 9 else chr(ord('A') + digit - 10)


if __name__ == '__main__':
    print(convert(input()))

