''' a15_02_(2317)_lca_offline_easy.py

https://www.e-olymp.com/uk/problems/2317

Спочатку є дерево, яке містить лише корінь (вершина з номером 1).
Потрібно навчитись відповідати на наступні запити:

ADD a b - підвісити вершину b за вершину a (гарантується, що вершина a вже існує).
GET a b - повернути LCA вершин a та b.
Усі номери вершин від 1 до N. У кожен момент часу у нас є одне дерево.

Вхідні дані:
У першому рядку вхідного файлу міститься число k - кількість запитів.
Наступні k рядків містять самі запити. Гарантується, що число запитів
кожного з типів не перевищує 1000.

Вихідні дані:
Для кожного запиту типу GET виведіть в окремий рядок одне ціле число -
відповідь на відповідний запит.
'''

# Даний алгоритм не є оптимальним, оскільки для розв'язання задачі достатньо зв'язувати
# кожен вузол зі своїм батьком і необов'язково з дітьми.
# Оптимальніше було б робити структуру дерева у вигляді масиву (списку) або хеш-таблиці (словника).


class Tree:
    ''' Дерево має ієрархічну рекурсивну структуру.
    Кожен вузол має ключ - номер вершини в дереві.
    Вузол має посилання на свого батька.
    Навантаження у вузла відсутнє.
    Піддерева зображені у вигляді списку синів.
    '''

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def has_children(self):
        return bool(self.children)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_child(self, key):
        for child in self.children:
            if child.key == key:
                return child

    def search(self, key):
        ''' Пошук в ширину'''
        queue = []
        queue.append(self)
        while queue:
            node = queue.pop(0)
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self, parent_key, child_key):
        ''' Додає дитину з ключем child_key до вузла з ключем parent_key.
        Такий вузол має бути в дереві'''
        parent = self.search(parent_key)
        parent.add_child(Tree(child_key))

    def get(self, i, j):
        ''' Повертає LCA (найменшого спільного предка) вершин з номерами i, j'''
        node_i = self.search(i)
        node_j = self.search(j)
        while True: # Пробігаємо по предках вузла з ключем j
            while node_j.key >= node_i.key: # Ключі предків i повинні бути завжди не менші за ключі предків j
                if node_i is node_j: # Якщо знайшли перший спільний вузол, задача виконана
                    return node_i.key
                node_j = node_j.parent # Якщо предок вузла j більший за предка вузла i, беремо наступного предка вузла j
            node_i = node_i.parent # Якщо предок вузла j менший за предка вузла i, беремо наступного предка вузла i

    def execute(self, command):
        ''' Виконати команду:
        ADD i j  --> self.add(i, j)
        GET i j  --> self.get(i, j)
        '''
        command = command.split()
        name = command[0].lower()
        args = map(int, command[1:])
        return getattr(self, name)(*args)


if __name__ == '__main__':
    tree = Tree(1)
    with open('input.txt') as inp:
        with open('output.txt', 'w') as out:
            k = int(inp.readline())
            for _ in range(k):
                result = tree.execute(inp.readline())
                if result:
                    print(result, file=out)
