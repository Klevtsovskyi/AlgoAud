''' a11_3_unlimited_stack.py

https://www.e-olymp.com/uk/problems/6124

Реалізуйте структуру даних "стек". Напишіть програму, яка містить опис стека
і моделює роботу стека, реалізувавши усі вказані тут методи. Програма зчитує
послідовність команд і у залежності від команди виконує ту чи іншу операцію.
Після виконання кожної команди програма повинна вивести один рядок. Можливі
команди для програми:

push n - Додати у в стек число n (значення n задається після команди).
       Програма повинна вивести ok.
pop    - Видалити зі стеку останній елемент. Програма повинна вивести
       його значення.
back   - Програма повинна вивести значення останнього елементу,
       не видаляючи його зі стеку.
size   - Програма повинна вивести кількість елементів у стеці.
clear  - Програма повинна очистити стек і вивести ok.
exit   - Програма повинна вивести bye і завершити роботу.

Розмір стеку повмнен бути обмежений лише роміром доступної оперативної пам'яті.
Перед виконанням операцій back та pop програма повинна перевіряти,
чи міститься у стеці хоча б один елемент. Якщо у вхідних даних зустрічається
операція back чи pop, і при цьому стек порожній, то програма повинна замість
числового значення вивести рядок error.

Вхідні дані:
Описані в умові. Див. також приклад вхідних даних.

Вихідні дані:
Описані в умові. Див. також приклад вихідних даних.
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
        return 'ok'

    def pop(self):
        if self.top:
            item, self.top = self.top.item, self.top.next
            self.len -= 1
            return item
        return 'error'

    def back(self):
        return self.top.item if self.top else 'error'

    def size(self):
        return self.len

    def clear(self):
        self.top = None
        self.len = 0
        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        if command.startswith('push'):
            return self.push(int(command[4:]))
        else:
            return getattr(self, command)()


if __name__ == '__main__':
    stack = Stack()

    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for line in input:
                result = stack.execute(line.rstrip())
                print(result, file=output)
                if result == 'bye':
                    break
