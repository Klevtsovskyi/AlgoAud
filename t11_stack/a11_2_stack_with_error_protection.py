''' a11_2_stack_with_error_protection.py

https://www.e-olymp.com/uk/problems/6123

Реалізуйте структуру даних "стек". Напишіть програму, яка містить опис стека
і моделює роботу стека, реалізувавши усі вказані тут методи. Програма зчитує
послідовність команд і у залежності от команди вмконує ту чи іншу операцію.
Пісяе виконання кожної команди програма повинна вивести один рядк. Можливі
команди для програми:

push n - Додати у стек число n (n невід'ємне). Програма повинна вивести ok.
pop    - Видалити зі стеку останній елемент.
       Програма повина вивести його значення.
back   - Програма повинна вивести значення останнього елемента,
       не видаляючи його зі стеку.
size   - Програма повинна вивести кількість елементів у стеку.
clear  - Програма повинна очистити стек і вивести ok.
exit   - Програма аовинна вивести bye і завершити роботу.

Перед виконаням операцій back та pop програма повинна перевіряти,
чи міститься у стеку хоча б один елемент. Якщо у вхідних даних зустрічається
операція back або pop, і при цьому стек порожній, то програма повинна замість
числового значення вивести рядок error.

Вхідні дані:
Кожний рядок містить одну команду.

Вихідні дані:
Для кожної команди вивести в окремому рядку відповідний результат.
'''

class Stack:

    def __init__(self): self._items = []
    def push(self, item): self._items.append(item); return 'ok'
    def pop(self): return self._items.pop() if self._items else 'error'
    def back(self): return self._items[-1] if self._items else 'error'
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
