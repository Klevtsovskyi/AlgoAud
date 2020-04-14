''' a16_03_second_maximum.py

https://www.e-olymp.com/en/problems/2314

Реалізуйте бінарне дерево пошуку для цілих чисел. Програма отримує на вхід
послідовність цілих чисел і будує з них дерево. Елементи у дерево додаються
відповідно до результату пошуку їх місця. Якщо елемент вже існує в дереві,
додавати його не треба. Балансування дерева не проводиться.

Виведіть другий за величиною елемент у побудованому дереві.
Гарантується, що він завжди знайдеться.

Вхідні дані:
На вхід програма отримує послідовність цілих чисел. Послідовність
завершується числом 0, яке означає кінець вводу, і додавати його у
дерево непотрібно. Гарантується, що вхідна послідовність містить не більш
ніж 10^5 елементів, кожний з яких не перевищує за модулем 2*10^9.

Вихідні дані:
Другий за величиною елемент у побудованому дереві.

Помітимо, що висота дерева вимірюється в вершинах.
'''

class SearchTree:
    ''' Дерево пошуку має ієрархічну рекурсивну структуру.
    Ключ вузла - номер вершини в дереві.
    '''

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_key(self): return self.key
    def has_left(self): return self.left is not None
    def has_right(self): return self.right is not None
    def get_left(self): return self.left
    def get_right(self): return self.right
    def set_left(self, key): self.left = SearchTree(key)
    def set_right(self, key): self.right = SearchTree(key)

    def insert(self, key):
        ''' Вставляє вузол з ключем key, якщо такого елемента немає в дереві.'''
        node = self
        while True: # Стандартна реалізація нерекурсивної вставки в дерево пошуку
            if key == node.get_key():
                break
            if key < node.get_key():
                if node.has_left():
                    node = node.get_left()
                else:
                    node.set_left(key)
                    break
            else:
                if node.has_right():
                    node = node.get_right()
                else:
                    node.set_right(key)
                    break

    def second_maximum(self):
        ''' Повертає другий за величиною елемент в дереві.'''
        node = self
        # Другий по величині елемент знаходиться завжди з правої сторони
        right_side = [node.get_key()] # Всі такі елементи додаємо у список
        while node.has_right():
            node = node.get_right()
            right_side.append(node.get_key())
        right_side.pop() # Виключаємо зі списку найбільший елемент
        while True: # Тримаємося завжди правої сторони
            if node.has_right():
                node = node.get_right()
                right_side.append(node.get_key())
            elif node.has_left():
                node = node.get_left()
                right_side.append(node.get_key())
            else:
                break
        return max(right_side)


if __name__ == '__main__':
    nodes = tuple(map(int, input().split()))
    root = SearchTree(nodes[0])
    i = 1
    while nodes[i] != 0:
        root.insert(nodes[i])
        i += 1
    print(root.second_maximum())
