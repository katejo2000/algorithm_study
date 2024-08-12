import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

# print(graph)

visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    count = 1
    # print("dfs", x, y, "node is", count)
    visited[y][x] = True
    # print("음쓰 발견")

    for j in range(4):
        nx = dx[j]
        ny = dy[j]
        # print("check", x + nx, y + ny)

        if (0 < x + nx < m + 1) and (0 < y + ny < n + 1) and (not visited[y + ny][x + nx]) and (
                graph[y + ny][x + nx] == 1):
            # print("go to", x + nx, y + ny)
            num = dfs(x + nx, y + ny)
            # print("num is", num)
            count += num

    return count


res = []

for y in range(1, n + 1):
    for x in range(1, m + 1):
        if not visited[y][x] and graph[y][x] == 1:
            res.append(dfs(x, y))

print(max(res))
