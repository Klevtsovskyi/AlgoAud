''' a22_01_e4000_depth_search.py

https://www.e-olymp.com/uk/problems/4000

Задано неорієнтовний незважений граф, у якому виділено вершину.
Вам потрібно знайти кількість вершин, які лежать з нею у одній
компоненті зв'язності (включаючи саму вершину).

Вхідні дані:
У першому рядку містяться два цілих числа n та s (1 ≤ s ≤ n ≤ 100),
де n - кількість вершин графа, а s - виділена вершина. У наступних n рядках
записано по n чисел - матриця суміжності графа, у якій цифра "0" позначає
відсутність ребра між вершинами, а цифра "1" - його наявність. Гарантується,
що на головній діагоналі матриці завжди стоять нулі.

Вихідні дані:
Виведіть шукану кількість вершин.
'''

class Graph:
    ''' Неорієнтовний граф має структуру матриці суміжності.
    '''
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_vertices_count(self, vertex):
        ''' Повертає кількість вершин у компоненті зв'язності,
        до якої належить вершина vertex'''
        # Використовуємо пошук в глибину за допомогою стека

        visited = {vertex - 1} # Вершини, які було відвідано (додано до стека за весь час)
        stack = [vertex - 1]   # Вершини, які залишилося опрацювати
        count = 0              # Кількість вершин в компоненті зв'язності
        # Коли стек стає пустим, означає, що закінчилися вершини в компоненті зв'язності
        while stack:
            current = stack.pop() # Беремо по одній вершині зі стека
            count += 1            # За кожну вершину в компоненті зв'язності, додаємо 1
            for neighbour, edge in enumerate(self.matrix[current]):
                if edge:
                    if neighbour not in visited: # Якщо вершина ще не пройдена,
                        stack.append(neighbour)  # додаємо до стека
                        visited.add(neighbour)   # і до множини відвіданих
        return count


if __name__ == '__main__':
    with open('input.txt') as inp:
        n, s = map(int, inp.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(graph.get_vertices_count(s))
