import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]  # 0은 없음
visited = [False] * (n + 1)  # 0은 없음
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(node):
    count = 0
    if not visited[node]:
        visited[node] = True
        count += 1

        for k in range(n + 1):
            if graph[node][k] == 1:
                count += dfs(k)

    return count


for i in range(n):
    if not visited[i + 1]:
        result.append(dfs(i + 1))

print(len(result))
