''' a16_01_height_of_the_tree.py

https://www.e-olymp.com/uk/problems/2312

Реалізуйте бінарне дерево пошуку для цілих чисел. Програма отримує на вхід
послідовність цілих чисел і будує з них дерево. Елементи у дерево додаються
відповідно до результату пошуку їх місця. Якщо елемент вже існує в дереві,
додавати його не треба. Балансування дерева не проводиться.

Знайдіть висоту побудованого дерева.

Вхідні дані:
На вхід програма отримує послідовність цілих чисел. Послідовність
завершується числом 0, яке означає кінець вводу, і додавати його у
дерево непотрібно. Гарантується, що вхідна послідовність містить не більш
ніж 10^5 елементів, кожний з яких не перевищує за модулем 2*10^9.

Вихідні дані:
Єдине число – висота отриманого дерева.

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

    def get_height(self):
        ''' Обчислює висоту дерева.'''
        # Дана реалізація використовує рекурсію. Якщо в дереві забагато елементів, буде спровоковане виключення.
        def _height(node):
            left_height = _height(node.get_left()) if node.has_left() else 0
            right_height = _height(node.get_right()) if node.has_right() else 0
            # Висота дерева - це максимум висоти лівого та правого піддерева плюс один
            return max(left_height, right_height) + 1
        return _height(self)


if __name__ == '__main__':
    nodes = tuple(map(int, input().split()))
    if nodes[0] == 0:
        print(0)
    else:
        root = SearchTree(nodes[0])
        i = 1
        while nodes[i] != 0:
            root.insert(nodes[i])
            i += 1
        print(root.get_height())
