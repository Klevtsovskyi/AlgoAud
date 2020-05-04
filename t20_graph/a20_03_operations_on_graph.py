''' a20_03_operations_on_graph.py

https://www.e-olymp.com/uk/problems/2472

У задачі необхідно створити неорієнтовний граф,
на якому підтримуються наступні операції:
 - AddEdge(u, v) - додати в граф ребро між вершинами (u, v);
 - Vertex(u) - вивести список вершин, суміжних з вершиною u.
Петлі і кратні ребра у графі відсутні.

Вхідні дані:
Перший рядок містить кількість вершин n (1 ≤ n ≤ 10^5) у графі.
У наступному рядку знаходиться кількість операцій k (0 ≤ k ≤ 10^6).
Кожний з наступних рядків задає операцію у форматі:
"1 <число> <число>" або "2 <число>",
які позначають відповідно операції AddEdge(u, v) і Vertex(u).

Гарантується, що сумарна кількість чисел, які необхідно вивести при
виконанні усіх операцій Vertex, не перевищує 2 * 10^5.

Вихідні дані:
Для кожної команди Vertex вивести в окремому рядку вивести список суміжних
вершин вказаної вершини. Вершини списку суміжності можна виводити у
довільному порядку. Якщо для вказаної вершини суміжних немає,
то слід вивести порожній рядок.
'''

# Умова не є коректною.
# Потрібно виводити список сумісних вершин, в порядку додання.


class Graph:
    ''' Граф зображено у вигляді словника, де ключ - вершина,
    а значення - список вершин, до яких йдуть ребра з заданої.
    '''
    def __init__(self, vertex_num):
        self.vertices = {}
        for i in range(1, vertex_num + 1):
            self.vertices[i] = list()

    def add_edge(self, source, destination):
        ''' Додає ребро від вершини source до вершини destination.'''
        self.vertices[source].append(destination)
        self.vertices[destination].append(source)

    def get_neighbours(self, vertex):
        ''' Повертає кортеж всіх вершин, що є сумісними з vertex.'''
        return tuple(neighbour for neighbour in self.vertices[vertex])


if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        graph = Graph(n)
        k = int(inp.readline())
        for _ in range(k):
            command = inp.readline().split()
            if command[0] == '1':
                graph.add_edge(int(command[1]), int(command[2]))
            elif command[0] == '2':
                print(*graph.get_neighbours(int(command[1])))
