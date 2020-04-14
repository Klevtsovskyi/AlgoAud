''' a16_04_print_leaves.py

https://www.e-olymp.com/uk/problems/2316

Реалізуйте бінарне дерево пошуку для цілих чисел. Програма отримує на вхід
послідовність цілих чисел і будує з них дерево. Елементи у дерево додаються
відповідно до результату пошуку їх місця. Якщо елемент вже існує в дереві,
додавати його не треба. Балансування дерева не проводиться.

Виведіть для отриманого дерева список усіх листів
(вершин, що не мають нащадків) у порядку зростання.

Вхідні дані:
На вхід програма отримує послідовність цілих чисел. Послідовність
завершується числом 0, яке означає кінець вводу, і додавати його у
дерево непотрібно. Гарантується, що вхідна послідовність містить не більш
ніж 10^5 елементів, кожний з яких не перевищує за модулем 2*10^9.

Вихідні дані:
Виведіть для отриманого дерева список усіх листів у порядку зростання.
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

    def get_leaves(self):
        ''' Повертає список ключів всіх листків дерева у порядку зростання.'''
        # Виконуємо пошук у глибину. Так вихідний список буде вже впорядкованим.
        leaves = []
        def _leaves(node):
            if node.has_left():
                _leaves(node.get_left())
            if node.has_right():
                _leaves(node.get_right())
            if not (node.has_left() or node.has_right()):
                leaves.append(node.get_key()) # Додаємо листок до списку
        _leaves(self)
        return leaves


if __name__ == '__main__':
    nodes = tuple(map(int, input().split()))
    if nodes[0] == 0:
        pass
    else:
        root = SearchTree(nodes[0])
        i = 1
        while nodes[i] != 0:
            root.insert(nodes[i])
            i += 1
        print(*root.get_leaves())
