''' a13_3_(6128)_simple_deque.py

Реалізуйте структуру даних "дек". Напишіть програму, яка містить опис дека
і моделює роботу дека, реалізувавши усі вказані тут методи. Програма зчитує
послідовність команд і у залежності від команди виконує ту чи іншу операцію.
Після виконання кожної команди програма повинна вивести один рядок.
Можливі команди для програми:
- push_front - Додати (покласти) у початок дека новий елемент.
               Програма повинна вивести ok.
- push_back  - Додати (покласти) у кінець дека новий елемент.
               Програма повинна вивести ok.
- pop_front  - Дістати з дека перший елемент. Програма повинна
               вивести його значення.
- pop_back   - Дістати з дека останній елемент. Програма повинна
               вивести його значення.
- front      - Взнати значення першого елементу (не видаляючи його).
               Програма повинна вивести його значення.
- back       - Взнати значення останнього клемента (не видаляючи
               його). Програма повинна вивести його значення.
- size       - Вивести кількість елементів у декі.
- clear      - Очистити дек (видалити з нього усі елементи) і вивести ok.
- exit       - Програма повинна вивести bye і завершити роботу.

Гарантується, що кількість елементів у декі у довільний момент не
перевищує 100. Усі операції: pop_front, pop_back, front, back
завжди коректні.

Вхідні дані:
Кожний рядок містить одну команду.

Вихідні дані:
Для кожної команди вивести в окремому рядку відповідний результат.
'''

class Deque:

    def __init__(self): self.items = []
    def push_front(self, item): self.items.insert(0, item); return 'ok'
    def push_back(self, item): self.items.append(item); return 'ok'
    def pop_front(self): return self.items.pop(0)
    def pop_back(self): return self.items.pop()
    def front(self): return self.items[0]
    def back(self): return self.items[-1]
    def size(self): return len(self.items)
    def clear(self): self.items.clear(); return 'ok'
    def exit(self): return 'bye'

    def execute(self, command):
        command = command.split()
        name = command[0]
        args = command[1:]
        return getattr(self, name)(*args)


if __name__ == '__main__':
    deque = Deque()

    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for line in input:
                result = deque.execute(line.rstrip())
                print(result, file=output)
                if result == 'bye':
                    break
