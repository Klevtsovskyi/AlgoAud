''' a13_4_(6130)_unlimited_deque.py

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

Розмір дека повинен бути обмежений лише розміром доступної оперативної пам'яті.
Перед виконанням операцій pop_front, pop_back, front, back програма повинна
перевіряти, чи міститься у декі хоча б один елемент. Якщо у вхідних даних
зустрічається операція pop_front, pop_back, front, back, і при цьому дек
порожній, то програма повинна замість числового значення вивести рядок error.
'''

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque:

    def __init__(self):
        self._front = None
        self._back = None
        self._len = 0
        
    def push_front(self, item):
        node = Node(item)
        if self._front:
            self._front.prev = node
            node.next = self._front
        else:
            self._back = node
        self._front = node
        self._len += 1
        return 'ok'
        
    def push_back(self, item):
        node = Node(item)
        if self._back:
            self._back.next = node
            node.prev = self._back
        else:
            self._front = node
        self._back = node
        self._len += 1
        return 'ok'
        
    def pop_front(self):
        if self._front:
            node = self._front
            self._front = node.next
            if self._front:
                self._front.prev = None
            else:
                self._back = None
            self._len -= 1
            return node.item
        return 'error'
    
    def pop_back(self):
        if self._back:
            node = self._back
            self._back = node.prev
            if self._back:
                self._back.next = None
            else:
                self._front = None
            self._len -= 1
            return node.item
        return 'error'
    
    def front(self):
        return self._front.item if self._front else 'error'
    
    def back(self):
        return self._back.item if self._back else 'error'
    
    def size(self):
        return self._len
    
    def clear(self):
        self.__init__()
        return 'ok'
    
    def exit(self):
        return 'bye'

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
