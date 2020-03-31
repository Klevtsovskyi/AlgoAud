''' a13_2_(6127)_unlimited_queue.py

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

Розмір череги повинен бути обмежений лише розміром доступної оперативної
пам'яті. Перед виконанням операцій front та pop програма повинна перевіряти,
чи міститься у черзі хоча б один елемент. Якщо у вхідних даних зустрічається
операція front чи pop, і при цьому черга порожня, то програма повинна
замість числового значення вивести рядк error.
'''

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._len = 0

    def push(self, item):
        node = Node(item)
        if self._back:
            self._back.next = node
        else:
            self._front = node
        self._back = node
        self._len += 1
        return 'ok'
    
    def pop(self):
        if self._front:
            node = self._front
            self._front = node.next
            if not self._front:
                self._back = None
            self._len -= 1
            return node.item
        return 'error'
    
    def front(self):
        return self._front.item if self._front else 'error'
    
    def size(self):
        return self._len
    
    def clear(self):
        self.__init__()
        return 'ok'
    
    def exit(self):
        return 'bye'

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
