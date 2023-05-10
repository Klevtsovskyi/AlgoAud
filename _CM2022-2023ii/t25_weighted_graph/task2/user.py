"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шляху між двома заданими вузлами цього графа
"""
from math import inf
from PriorityQueue import PriorityQueue

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
    distances = [inf for _ in range(n)]
    distances[start] = 0
    sources = {start: -1}
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
    # print(distances)
    # print(sources)

    path = []
    while i != -1:
        path.append(i)
        i = sources[i]
    path.reverse()
    return path


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
    print(getWay(1, 7))
