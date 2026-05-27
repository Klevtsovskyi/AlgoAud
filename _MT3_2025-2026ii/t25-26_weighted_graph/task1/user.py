"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
import sys

INF = sys.maxsize

graph: list[dict]


def init(vertices, edges):
    """ Ініціалізація графа.

    Викликається один раз на початку виконання програми.
    @param vertices: кількість вершин графа
    @param edges: кількість ребер графа
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
    distances = [INF for _ in range(n)]
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

    # print(distances)
    if distances[end] < INF:
        return distances[end]
    else:
        return -1


if __name__ == '__main__':
    init(7, 0)
    addEdge(1, 2, 3)
    addEdge(1, 3, 1)
    addEdge(1, 5, 10)
    addEdge(2, 6, 4)
    addEdge(3, 4, 2)
    addEdge(4, 1, 8)
    addEdge(4, 3, 2)
    addEdge(4, 5, 6)
    addEdge(5, 2, 23)
    addEdge(5, 6, 15)
    addEdge(6, 2, 4)
    print(graph)
    print(findDistance(4, 6))
