def solve(array, x):
    return "NO"


n = int(input())
array = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

# print(n)
# print(array)
# print(m)
# print(queries)

for i in range(m):
    print(solve(array, queries[i]))
