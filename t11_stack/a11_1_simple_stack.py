''' a11_1_simple_stack.py

https://www.e-olymp.com/uk/problems/6122

Реалізуйте структуру даних "стек". Напишіть програму, яка містить опис стека
та моделює работу стека, реалізувавши усі вказані тут методи. Програма зчитує
послідовність команд і у залежності ві команди виконує ту чи іншу операцію.
Після виконання кожної команди програма повинна вивести один рядок. Мможливі
команди для програми:

push n - Додати у стек число n (значення n задається після команди).
       Програма повиннавивести ok.
pop    - Видалити зі стеку останній елемент. Програма повинна вивести
       його значення.
back   - Програма повинна вивести значення останнього елемента,
       не видаляючи його зі стеку.
size   - Програма повинна вивести кількість елементів у стеці.
clear  - Програма повинна очистити стек і вивести ok.
exit   - Програма повинна вивести bye і завершити роботу.

Гарантується, що набір вхідних команд задовольняє наступним твимогам:
максимальна кількість елементів у стеці у довільний момент не перевищує 100,
усі команди pop та back коректні, тобто при їх виконанні у стеці міститься
хоча б один елемент.

Вхідні дані:
Описані в умові. Див. також приклад вхідних даних.

Вихідні дані:
Описані в умові. Див. також приклад вихідних даних.
'''

class Stack:

    def __init__(self): self._items = []
    def push(self, item): self._items.append(item); return 'ok'
    def pop(self): return self._items.pop()
    def back(self): return self._items[-1]
    def size(self): return len(self._items)
    def clear(self): self._items.clear(); return 'ok'
    def exit(self): return 'bye'

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
