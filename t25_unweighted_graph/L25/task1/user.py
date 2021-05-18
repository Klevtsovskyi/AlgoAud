"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""


from math import inf


graph = []
n = 0


def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global n, graph
    n = vertices
    graph = [{} for _ in range(n)]


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    graph[source][destination] = weight


def findDistance(start, end):
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    distances = [inf for _ in range(n)]
    distances[start] = 0
    for _ in range(n - 1):
        relaxed = True
        for i in range(n):
            for j in graph[i]:
                if distances[j] > distances[i] + graph[i][j]:
                    distances[j] = distances[i] + graph[i][j]
                    relaxed = False
        if relaxed:
            break
    return -1 if distances[end] == inf else distances[end]


if __name__ == "__main__":
    init(10, 10)
    addEdge(0, 1, 5)
    addEdge(1, 2, 8)
    print(graph)
    print(findDistance(0, 2))
