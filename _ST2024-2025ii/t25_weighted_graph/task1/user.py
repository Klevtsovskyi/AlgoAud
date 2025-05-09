"""
Нехай задано орієнтований зважений граф.
Знайдіть довжину найкоротшого шляху між двома заданими вузлами цього графа
"""
INF = float("inf")

graph: dict


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
    distances = [INF for _ in range(n)]
    distances[start] = 0

    for _ in range(n - 1):
        # print(distances)
        relaxed = True
        for u in range(n):
            for v in graph[u]:
                if distances[v] > distances[u] + graph[u][v]:
                    distances[v] = distances[u] + graph[u][v]
                    relaxed = False
        if relaxed:
            break

    if distances[end] < INF:
        return distances[end]
    else:
        return -1


if __name__ == '__main__':
    init(6, 8)
    addEdge(0, 1, 1)
    addEdge(0, 4, 5)
    addEdge(0, 5, 3)
    addEdge(1, 2, 5)
    addEdge(1, 3, 2)
    addEdge(1, 0, 1)
    addEdge(2, 0, 7)
    addEdge(2, 4, 2)
    addEdge(3, 5, 3)
    addEdge(5, 0, 3)
    # print(graph)
    print(findDistance(1, 4))
