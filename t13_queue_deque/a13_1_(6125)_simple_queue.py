''' a13_1_(6125)_simple_queue.py

Реалізуйте структуру даних "черга". Напишіть програму, яка містить
опис черги і моделює роботу черги, реалізувавши усі вказані тут методи.
Програма зчитує послідовність команд і у залежності від команди виконує
ту чи іншу операцію. Після виконання кожної команди програма повинна
вивести один рядк. Можливі команди для програми:
- push n - Додати у чергу число n (значення n задається після команди).
           Програма повинна вивести ok.
- pop    - Видалити з черги перший елемент.
           Програма повинна вивести його значення.
- front  - Програма повинна вивести значення першого елементу,
           не видаляючи його з черги.
- size   - Програма повинна вивести кількість елементів у черзі.
- clear  - Программа должна очистить очередь и вывести ok.
- exit   - Програма повинна вивести bye і завершити роботу.

Гарантується, що набір вхідних команд задовольняє наступним вимогам:
максимальна кількість елементів у черзі у довільний момент не
перевищує 100, усі команди pop та front коректні, тобто при їх
виконанні у черзі міститься хоча б один елемент.
'''

class Queue:

    def __init__(self): self.items = []
    def push(self, item): self.items.append(item); return 'ok'
    def pop(self): return self.items.pop(0)
    def front(self): return self.items[0]
    def size(self): return len(self.items)
    def clear(self): self.items.clear(); return 'ok'
    def exit(self): return 'bye'

    def execute(self, command):
        if command.startswith('push'):
            return self.push(int(command[4:]))
        else:
            return getattr(self, command)()

if __name__ == '__main__':
    queue = Queue()

    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for line in input:
                result = queue.execute(line.rstrip())
                print(result, file=output)
                if result == 'bye':
                    break
