''' a20_02_from_adjacency_list_to_adjacency_matrix.py

https://www.e-olymp.com/uk/problems/3982

Простий орієнтовний граф задано у вигляді списків суміжності.
Виведіть його подання у вигляді матриці суміжності.

Вхідні дані:
У першому рядку міститься кількість вершин n (1 ≤ n ≤ 100).
Далі йдуть n рядків. В i-му рядку міститься опис усіх ребер,
які виходять з i-ої вершини. Опис розпочинається кількістью ребер,
які виходять з вершин. Далі йдуть номери вершин, у які ці ребра йдуть.
Усі вершини нумеруються натуральними числами від 1 до n.

Вихідні дані:
Виведіть матрицю суміжності орієнтовного графа.
'''

class Graph:
    ''' Граф зображено у вигляді словника, де ключ - вершина,
    а значення - множина вершин, до яких йдуть ребра з заданої.
    '''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key, neighbours):
        ''' Додає вершину key з множиною сусідів neighbours.'''
        self.vertices[key] = neighbours

    def get_adjacency_matrix(self):
        ''' Повертає матрицю суміжності графа.'''
        matrix = []
        for i in range(1, len(self.vertices) + 1):
            matrix.append([])
            for j in range(1, len(self.vertices) + 1):
                matrix[i - 1].append(1 if (j in self.vertices[i]) else 0)
        return matrix


if __name__ == '__main__':
    with open('input.txt') as inp:
        graph = Graph()
        n = int(inp.readline())
        for i in range(1, n + 1):
            edges = tuple(map(int, inp.readline().split()))[1:]
            graph.add_vertex(i, set(edges))
        for row in graph.get_adjacency_matrix():
            print(*row)
