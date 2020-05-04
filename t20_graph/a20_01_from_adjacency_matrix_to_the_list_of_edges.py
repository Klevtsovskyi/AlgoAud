''' a20_01_from_adjacency_matrix_to_the_list_of_edges.py

https://www.e-olymp.com/uk/problems/2471

Простий неорієнтовний граф задано матрицею суміжності,
виведіть його подання у вигляді списку рeбер.

Вхідні дані:
Перший рядок містить кількість вершин n (1 ≤ n ≤ 100) у графі.
Потім йде n рядків по n елементів у кожному - опис матриці суміжності.

Вихідні дані:
Виведіть список ребер, впорядкований по першій вершині у парі вершин,
яка описує ребро.
'''

class Graph:
    ''' Неорієнтовний граф зображено у вигляді матриці суміжності.
    '''
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_list_of_edges(self):
        ''' Повертає список суміжних вершин. Вершини не повторюються.'''
        vertices = []
        n = len(self.matrix)
        for i in range(n):
            neighbors = []
            for j in range(i + 1, n):
                if self.matrix[i][j] == 1:
                    neighbors.append(j)
            vertices.append(neighbors)
        return vertices


if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        vertices = graph.get_list_of_edges()
        for i in range(n):
            for j in vertices[i]:
                print(i + 1, j + 1)
