''' a21_01_e2401_breadth_first_search.py

https://www.e-olymp.com/uk/problems/2401

Задано неорієновний граф. Знайдіть найменшу відстань від
однієї заданої вершини до іншої.

Вхідні дані:
У першому рядку міститься три натуральних числа n, s
та f (1 ≤ s, f ≤ n ≤ 100) - кількість вершин у графі і номери початкової та
кінцевої вершин відповідно. Далі у n рядках задано матрицю суміжності графа.
Якщо значення у j-му елементі i-го рядка дорівнює 1, то у графі є направлене
ребро з вершини i до вершини j.

Вихідні дані:
Вивести мінімальну відстань від початкової вершини до кінцевої.
Якщо шляху не існує, виведіть 0.
'''

class Graph:
    ''' Орієнтовний граф зображено у вигляді матриці суміжності.
    '''
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_shortest_distance(self, start, finish):
        ''' Повертає мінімальну відстань від вершини start до finish.'''
        # Використовуємо хвильовий алгоритм
        start -= 1 # Відлік починається з нуля, тому віднімаємо 1
        finish -= 1
        # Словник відстаней: ключ - вершина, значення - відстань до неї від старту
        distaces = {start: 0}
        # Використовуємо чергу для обходу в ширину
        queue = [start]
        while queue:
            current = queue.pop(0)
            # Пробігаємо по всім сусідам та ребрам поточної вершини
            for neighbour, edge in enumerate(self.matrix[current]):
                # Якщо ребро існує і вершини немає в словнику відстаней
                if edge == 1 and neighbour not in distaces:
                    # Додаємо до словника відстаней
                    distaces[neighbour] = distaces[current] + 1
                    # Якщо сусід є кінцем, повертаємо результат
                    if neighbour == finish:
                        return distaces[neighbour]
                    # Інакше додаємо сусіда до черги
                    queue.append(neighbour)
        return 0


if __name__ == '__main__':
    with open('input.txt') as inp:
        n, s, f = map(int, inp.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(graph.get_shortest_distance(s, f))

