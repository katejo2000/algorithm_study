from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[None] * m for _ in range(n)]

for i in range(n):
    line = input().strip()
    for j in range(len(line)):
        graph[i][j] = line[j]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
visited = [[False] * m for _ in range(n)]


def bfs(x, y):
    queue.append([x, y, 1])
    visited[y][x] = True

    while queue:
        curr = queue.popleft()

        if curr[0] == m - 1 and curr[1] == n - 1:
            return curr[2]

        for k in range(4):
            x2 = curr[0] + dx[k]
            y2 = curr[1] + dy[k]

            if 0 <= x2 <= m - 1 and 0 <= y2 <= n - 1 and not visited[y2][x2] and graph[y2][x2] == "1":
                queue.append([x2, y2, curr[2] + 1])
                visited[y2][x2] = True


print(bfs(0, 0))
