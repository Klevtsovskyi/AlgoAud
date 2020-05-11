''' a22_02_e0982_connectivity.py

https://www.e-olymp.com/uk/problems/982

Перевірити, чи є заданий неорієнтований граф зв'язним, тобто що з довільної
вершини можна по ребрам цього графа потрапити у довільну іншу.

Вхідні дані:
У першому рядку задано кількість вершин n та кількість ребер m у графі
відповідно (1 ≤ n ≤ 100, 1 ≤ m ≤ 10000). Наступні m рядків містять по
два числа ui і vi (1 ≤ ui, vi ≤ n); кожен такий рядок означає,
що у графі існує ребро між вершинами ui і vi.

Вихідні дані:
Виведіть "YES", якщо граф є зв'язним, і "NO" у протилежному випадку.
'''


class Graph:
    ''' Граф має структуру спуску суміжності: словника, де ключ - вершина,
    а значення - список вершин, до яких йдуть ребра з заданої.
    '''
    def __init__(self, vertex_num):
        self.vertices = {}
        for i in range(1, vertex_num + 1):
            self.vertices[i] = set()

    def add_edge(self, source, destination):
        ''' Додає ребро від вершини source до вершини destination.'''
        self.vertices[source].add(destination)
        self.vertices[destination].add(source)

    def is_connected(self):
        ''' Повертає True, якщо граф є зв'язним, False інакше.'''
        # Використовуємо пошук в глибину за допомогою стека

        remaining = set(self.vertices.keys()) # Множина всіх вершин в графі
        stack = [remaining.pop()] # Починаємо з довільної вершини
        # Коли стек стає пустим, означає, що закінчилися вершини в компоненті зв'язності
        while stack:
            current = stack.pop() # Беремо по одній вершині зі стека
            for neighbour in self.vertices[current]: # Пробігаємо по множині сусідів
                if neighbour in remaining:      # Якщо сусід ще не пройдений,
                    stack.append(neighbour)     # додаємо його до стека
                    remaining.remove(neighbour) # і видаляємо з множини, що залишилось опрацювати
        # Якщо було вичерпано всі вершини графа, він є зв'язним
        return not remaining


if __name__ == '__main__':
    with open('input.txt') as inp:
        n, m = map(int, inp.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, inp.readline().split()))
        print('YES' if graph.is_connected() else 'NO')
