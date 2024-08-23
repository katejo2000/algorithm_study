import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

# for 문으로 모든 1을 찾고
# 각 1을 기준으로, 주변 8방향 다 +1해주기
# 겹치는 경우, 0이 아닌 작은 수로 결정
# 끝나고 가장 큰 수 -1

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

queue = deque()
mv = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# print(queue)

while queue:
    x, y = queue.popleft()
    node = graph[x][y]
    # print(x, y)
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 0 or graph[nx][ny] > node + 1):
            graph[nx][ny] = node + 1
            queue.append([nx, ny])
            if (node + 1) > mv:
                mv = node + 1

# print(graph)
print(mv - 1)

# 0 0 1 0 <- (0,2)
# 0 0 0 0
# 1 0 0 0
# 0 0 0 0
# 0 0 0 1
