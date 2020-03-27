''' a12_2_parentheses_balance.py

https://www.e-olymp.com/uk/problems/2479

Є рядок, що містить дужки ( ) та [ ].
Дужковий вираз вважається правильним,якщо:
 - він є порожнім
 - якщо A та B правильні, то AB правильно
 - якщо A правильно, то (A) та [A] правильні
Напишіть програму, яка за вхідним рядком, що містить дужковий вираз,
визначить його правильність. Довжина рядка не більша за 128 символів.

Вхідні дані:
Перший рядок містить кількість тестів n.Кожний з
наступних n рядків містить вираз, який складається із дужок ( ) та [ ].

Вихідні дані:
Для кожного тесту вивести в окремому рядку "Yes",
якщо вираз є правильним і "No" інакше.
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


OPEN_BRACKETS = ('(', '[')
CLOSE_BRACKETS = (')', ']')


def check_brakets(sequence):

    stack = Stack()
    for bracket in sequence:
        if bracket in OPEN_BRACKETS:
            stack.push(bracket)
        elif stack.size():
            for i in range(len(CLOSE_BRACKETS)):
                if bracket == CLOSE_BRACKETS[i]:
                    if stack.pop() != OPEN_BRACKETS[i]:
                        return False
                    break
        else:
            return False
    return False if stack.size() else True


if __name__ == '__main__':
    data = ['([])',
            '(([()])))',
            '([()[]()])()']
    for t in data:
        print('Yes' if check_brakets(t) else 'No')
    '''
    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for _ in range(int(input.readline())):
                print('Yes' if check_brakets(input.readline().rstrip()) else 'No', file=output)
    '''
