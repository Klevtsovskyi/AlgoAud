''' a18_01_e4039_heapui.py

https://www.e-olymp.com/uk/problems/4039

У цій задачі вам необхідно організувати структуру даних Heap
для зберігання цілих чисел, над якою визначано наступні операції:
Insert(X) - додати в HeapX;
Exctract - дістати з Heap найбільше число (видаливши його при цьому).

Вхідні дані:
У вхідному файлі записано кількість команд N (1 ≤ N ≤ 100000),
потім послідовність з N команд, кожна у своєму рядку.

Кожна команда має такий формат: "0 <число>" або "1", що позначає
відповідно операції Insert (<число>) та Extract. Числа, що додаються,
знаходяться у інтервалі від 1 до 10^7 включно.

Гарантується, що при виконанні команди Extract у структурі
знаходиться по меншій мірі 1 елемент.

Вихідні дані:
У вихідний файл для кожної команди діставання необхідно вивести число,
отримане при виконанні команди Extract.
'''

class Heap:
    ''' Двійкова купа, в якій корінь - максимальний елемент.'''

    def __init__(self): self.items = [None]
    def __len__(self): return len(self.items) - 1
    def is_empty(self): return len(self) == 0
    def is_root(self, i): return i == 1
    def has_left(self, i): return i * 2 <= len(self)
    def has_right(self, i): return i * 2 + 1 <= len(self)
    def get_left(self, i): return i * 2
    def get_right(self, i): return i * 2 + 1
    def get_parent(self, i): return i // 2

    def insert(self, item):
        ''' Додає елемент до купи.'''
        self.items.append(item)
        self.sift_up()

    def extract(self):
        ''' Виймає максимальний елемент з купи.'''
        if not self.is_empty():
            self.swap(1, -1)
            item = self.items.pop()
            self.sift_down()
            return item

    def swap(self, i, j):
        ''' Міняє місцями два елементи в купі.'''
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self):
        ''' Просіює вгору останній елемент купи.'''
        current = len(self)
        while not self.is_root(current):
            parent = self.get_parent(current)
            if self.items[parent] < self.items[current]:
                self.swap(current, parent)
                current = parent
            else:
                break

    def sift_down(self):
        ''' Просіює вниз корінь купи.'''
        current = 1
        while self.has_left(current):
            child = self.get_max_child(current)
            if self.items[current] < self.items[child]:
                self.swap(current, child)
                current = child
            else:
                break

    def get_max_child(self, current):
        ''' Повертає індекс максимального з двох дітей.'''
        left = self.get_left(current)
        if self.has_right(current):
            right = self.get_right(current)
            if self.items[left] > self.items[right]:
                return left
            else:
                return right
        else:
            return left


if __name__ == '__main__':
    with open('input.txt') as inp:
        heap = Heap()
        n = int(inp.readline())
        for _ in range(n):
            command = inp.readline().split()
            if command[0] == '0':
                item = int(command[1])
                heap.insert(item)
            elif command[0] == '1':
                print(heap.extract())
