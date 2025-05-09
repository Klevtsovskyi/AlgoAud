"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""

from PriorityQueue import PriorityQueue
from math import inf as INF


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


def getWay(start, end):
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    n = len(graph)
    distances = [INF for _ in range(n)]
    distances[start] = 0
    sources = {start: -1}
    queue = PriorityQueue()
    queue.insert(start, 0)
    while not queue.empty():
        u = queue.extractMinimum()
        if u == end:
            break
        for v in graph[u]:
            if distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
                sources[v] = u
                if v in queue:
                    queue.updatePriority(v, distances[v])
                else:
                    queue.insert(v, distances[v])
    else:
        return []

    path = []
    u = end
    while u != -1:
        path.append(u)
        u = sources[u]

    path.reverse()
    return path


if __name__ == '__main__':
    init(6, 8)
    addEdge(0, 1, 1)
    addEdge(0, 4, 6)
    addEdge(0, 5, 3)
    addEdge(1, 2, 5)
    addEdge(1, 3, 2)
    addEdge(1, 0, 1)
    addEdge(2, 0, 7)
    addEdge(2, 4, 1)
    addEdge(3, 5, 3)
    addEdge(5, 0, 3)
    # print(graph)
    print(getWay(1, 4))
