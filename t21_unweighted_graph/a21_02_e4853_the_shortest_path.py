''' a21_02_e4853_the_shortest_path.py

https://www.e-olymp.com/uk/problems/4853

Задано неорієнтовний граф. Знайдіть найкоротший шлях від вершини a до вершини b.

Вхідні дані:
У першому рядку знаходиться два цілих числа n та m (1 ≤ n ≤ 5 * 10^4,
1 ≤ m ≤ 10^5) - кількість вершин та ребер відповідно. У другому рядку йдуть
цілі числа a та b - стартова та кінцева вершина відповідно. Далі йде m рядків,
які описують ребра.

Вихідні дані:
Якщо шляху між a та b немає, то виведіть -1. Інакше виведіть у першому рядку
довжину l найкоротшого шляху міжу цими двома вершинами у ребрах, а у другому
рядку виведіть l + 1 число - вершини цього шляху.
'''


class Graph:
    ''' Граф зображено у вигляді словника, де ключ - вершина,
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

    def get_shortest_path(self, start, finish):
        ''' Повертає найкоротший шлях від вершини start до finish.
        Якщо такого шляху не існує повертає None.
        '''
        # Слоник джерел, де ключ - вершина, значення - вершина, з якої прийшли
        sources = {start: None}
        # Використовуємо хвильовий алгоритм
        queue = [start]
        while queue:
            current = queue.pop(0)
            # Пробігаємо по всім сусідам поточної вершини
            for neighbour in self.vertices[current]:
                if neighbour not in sources:
                    queue.append(neighbour)
                    # Запам'ятовуємо вершину, з якої прийшли
                    sources[neighbour] = current
                    if neighbour == finish: # Якщо дійшли до потрібної вершини
                        # Повертаємося назад
                        path = [finish]
                        current = finish
                        while current != start: # Поки не дійшли до початку
                            # Додаємо джерело поточної вершини
                            current = sources[current]
                            path.append(current)
                        path.reverse()
                        return path


if __name__ == '__main__':
    with open('input.txt') as inp:
        n, m = map(int, inp.readline().split())
        a, b = map(int, inp.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, inp.readline().split()))
        path = graph.get_shortest_path(a, b)
        if path:
            print(len(path) - 1)
            print(*path)
        else:
            print(-1)
