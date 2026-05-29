from sys import maxsize as INF


def to_graph(samples, n, k):
    matrix = [
        [0 for __ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(i):
            for t in range(k):
                matrix[i][j] += samples[i][t] != samples[j][t]
                matrix[j][i] = matrix[i][j]
    # print(*matrix, sep="\n")
    return matrix


def prim(graph, n):
    visited = [False for _ in range(n)]
    sources = [-1 for _ in range(n)]
    costs = [INF for _ in range(n)]
    costs[0] = 0

    cost = 0
    tree = []
    while True:
        i = -1
        cost_i = INF
        for j in range(n):
            if not visited[j] and costs[j] < cost_i:
                i = j
                cost_i = costs[j]

        if i == -1:
            break

        visited[i] = True
        cost += costs[i]
        tree.append((i, sources[i]))
        for j in range(n):
            if i != j and not visited[j] and costs[j] > graph[i][j]:
                costs[j] = graph[i][j]
                sources[j] = i

    return cost, tree[1:]


def main():
    f = open("input.txt")
    n, k = map(int, f.readline().split())
    samples = []
    for _ in range(n):
        samples.append(f.readline().rstrip())
    graph = to_graph(samples, n, k)
    cost, tree = prim(graph, n)

    print(cost)
    for edge in tree:
        print(*edge)
    f.close()


if __name__ == '__main__':
    main()
