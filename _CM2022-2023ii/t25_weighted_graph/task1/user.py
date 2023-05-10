"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
from math import inf

graph: list


def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph
    graph = [{} for _ in range(vertices)]


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
    n = len(graph)
    distances = [inf for _ in range(n)]
    distances[start] = 0
    for _ in range(n - 1):
        # print(distances)
        relaxed = True
        for i in range(n):
            for j in graph[i]:
                if distances[j] > distances[i] + graph[i][j]:
                    distances[j] = distances[i] + graph[i][j]
                    relaxed = False
        if relaxed:
            break

    if distances[end] < inf:
        return distances[end]
    else:
        return -1


if __name__ == "__main__":
    init(8, 16)
    addEdge(0, 2, 4)
    addEdge(0, 4, 1)
    addEdge(1, 2, 7)
    addEdge(1, 5, 5)
    addEdge(1, 6, 3)
    addEdge(3, 1, 1)
    addEdge(3, 5, 3)
    addEdge(3, 7, 7)
    addEdge(4, 6, 1)
    addEdge(5, 3, 9)
    addEdge(5, 6, 6)
    addEdge(5, 7, 2)
    addEdge(6, 2, 3)
    addEdge(6, 4, 5)
    addEdge(6, 5, 2)
    addEdge(6, 7, 2)
    print(graph)
    print(findDistance(0, 7))
