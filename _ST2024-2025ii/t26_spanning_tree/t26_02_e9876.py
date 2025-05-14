import sys

INF = sys.maxsize


def to_graph(samples, n, m):
    matrix = [
        [0 for __ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                matrix[i][j] += samples[i][k] != samples[j][k]
    return matrix


def prim(graph, n):
    weight = 0
    tree = []
    fixed = [False for _ in range(n)]
    costs = [INF for _ in range(n)]
    costs[0] = 0
    sources = [-1 for _ in range(n)]
    while True:
        i = -1
        cost = INF
        for j in range(n):
            if not fixed[j] and costs[j] < cost:
                i = j
                cost = costs[j]
        if i == -1:
            break

        fixed[i] = True
        weight += costs[i]
        tree.append((sources[i], i))

        for j in range(n):
            if i != j and graph[i][j] < costs[j]:
                costs[j] = graph[i][j]
                sources[j] = i

    return weight, tree[1:]


if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    samples = []
    for _ in range(n):
        samples.append(f.readline().rstrip())
    graph = to_graph(samples, n, m)
    # print(*graph, sep="\n")
    w, t = prim(graph, n)
    print(w)
    for edge in t:
        print(*edge)
    f.close()
