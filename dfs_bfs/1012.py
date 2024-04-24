import sys

sys.setrecursionlimit(3000)

input = sys.stdin.readline

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visited, graph):
    cabbage = 0

    if graph[y][x] and not visited[y][x]:
        visited[y][x] = 1
        cabbage += 1

        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            if 0 <= x2 < m and 0 <= y2 < n:
                cabbage += dfs(x2, y2, visited, graph)

    return cabbage


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    group = []

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1 and not visited[j][i]:
                group.append(dfs(i, j, visited, graph))

    print(len(group))
