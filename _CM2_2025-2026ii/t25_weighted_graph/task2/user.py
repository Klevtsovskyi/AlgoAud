"""
Нехай задано орієнтований зважений граф.
Знайдіть найкоротший шлях між двома заданими вузлами цього графа
"""
import sys
from PriorityQueue import PriorityQueue

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



def getWay(start, end):  # O((n + m) log(n))
    """ Знаходить найкоротший шлях, між двома заданими вершинами графа

    @param start: початкова вершина
    @param end: кінцева вершина
    @return: список вершин шляху або порожній список, якщо шляху між вершинами не існує.
    """
    n = len(graph)
    sources = [-1 for _ in range(n)]
    distances = [INF for _ in range(n)]
    distances[start] = 0
    queue = PriorityQueue()
    queue.insert(start, 0)

    while not queue.empty():        # O(n)
        i = queue.extractMinimum()  # O(n log(n))
        if i == end:
            break
        for j in graph[i]:                                  # O(m)
            if distances[j] > distances[i] + graph[i][j]:
                distances[j] = distances[i] + graph[i][j]
                sources[j] = i
                if j in queue:
                    queue.updatePriority(j, distances[j])  # O(m log(n))
                else:
                    queue.insert(j, distances[j])          # O(m log(n))
    else:
        return []

    way = []
    while i != -1:
        way.append(i)
        i = sources[i]

    way.reverse()
    return way


if __name__ == '__main__':
    init(7, 0)
    addEdge(1, 3, 2)
    addEdge(1, 4, 10)
    addEdge(2, 1, 1)
    addEdge(2, 5, 4)
    addEdge(3, 4, 5)
    addEdge(4, 1, 10)
    addEdge(4, 2, 3)
    addEdge(4, 6, 1)
    addEdge(5, 4, 11)
    addEdge(6, 3, 13)
    addEdge(6, 4, 1)

    print(graph)
    print(getWay(5, 3))

