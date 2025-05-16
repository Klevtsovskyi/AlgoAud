"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
import sys

INF = sys.maxsize

graph: dict


def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges:  кількість ребер графа
    """
    global graph, n
    n = vertices
    graph = {}


def addEdge(source, destination, weight):
    """ Додає зважене ребро графа

    @param source: вершини з якої виходить ребро
    @param destination: вершина у яку входить ребро
    @param weight: вага ребра
    """
    if source not in graph:
        graph[source] = {}
    if destination not in graph:
        graph[destination] = {}
    graph[source][destination] = weight


def findDistance(start, end):
    """ Знаходить довжину найкоротшого шляху, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: Довжину найкоротшого шляху або -1 якщо шляху між вершинами не існує.
    """
    distances = [INF for _ in range(n + 1)]
    distances[start] = 0

    for _ in range(n - 1):
        relaxed = True
        for i in graph:
            for j in graph[i]:
                if distances[j] > distances[i] + graph[i][j]:
                    distances[j] = distances[i] + graph[i][j]
                    relaxed = False
        if relaxed:
            break

    # print(distances)
    if distances[end] < INF:
        return distances[end]
    else:
        return -1


if __name__ == '__main__':
    init(0, 0)
    addEdge(1, 2, 8)
    addEdge(1, 3, 7)
    addEdge(1, 4, 2)
    addEdge(1, 5, 1)
    addEdge(2, 6, 5)
    addEdge(2, 5, 2)
    addEdge(3, 4, 3)
    addEdge(4, 3, 3)
    addEdge(4, 5, 4)
    addEdge(5, 2, 2)
    addEdge(5, 6, 10)
    print(findDistance(1, 6))
