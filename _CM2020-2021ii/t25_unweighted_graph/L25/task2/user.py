"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""


from math import inf
from PriorityQueue import PriorityQueue


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


def getWay(start, end):
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    sources = {start: -1}
    distances = [inf for _ in range(n)]
    distances[start] = 0
    pq = PriorityQueue()
    pq.insert(start, 0)
    while not pq.empty():
        i = pq.extractMinimum()
        if i == end:
            break
        for j in graph[i]:
            if distances[i] + graph[i][j] < distances[j]:
                distances[j] = distances[i] + graph[i][j]
                sources[j] = i
                if j in pq:
                    pq.updatePriority(j, distances[j])
                else:
                    pq.insert(j, distances[j])
    if distances[end] == inf:
        return []
    path = [end]
    while end != start:
        end = sources[end]
        path.append(end)
    path.reverse()
    return path
