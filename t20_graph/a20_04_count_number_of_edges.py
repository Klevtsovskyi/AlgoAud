''' a20_04_count_number_of_edges.py

https://www.e-olymp.com/en/problems/5072

Орієнтовний граф задано матрицею суміжності. Знайдіть кількість ребер у графі.

Вхідні дані:
Перший рядок містить кількість вершин у графі n (1 ≤ n ≤ 100).
Далі йдуть n рядків по n чисел,
кожне з яких дорівнює 0 або 1 - матриця суміжності графа.

Вихідні дані:
Виведіть кількість ребер у графі.
'''

class Graph:
    ''' Орієнтовний граф зображено у вигляді матриці суміжності.
    '''
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_count_of_edges(self):
        ''' Повертає кількість ребер у графі.'''
        count = 0
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    count += 1
        return count


if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(graph.get_count_of_edges())

