"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""
import sys
from PriorityQueue import PriorityQueue

INF = sys.maxsize

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
    sources = [-1 for _ in range(n)]
    queue = PriorityQueue()
    queue.insert(start, 0)
    while not queue.empty():
        i = queue.extractMinimum()
        if i == end:
            break
        for j in graph[i]:
            if distances[j] > distances[i] + graph[i][j]:
                distances[j] = distances[i] + graph[i][j]
                sources[j] = i
                if j in queue:
                    queue.updatePriority(j, distances[j])
                else:
                    queue.insert(j, distances[j])
    else:
        return []

    path = []
    i = end
    while i != -1:
        path.append(i)
        i = sources[i]
    path.reverse()
    return path


if __name__ == '__main__':
    init(7, 0)
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
    print(getWay(1, 6))
