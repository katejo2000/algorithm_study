import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global curr
    while queue:
        curr = queue.popleft()

        # print("while queue, curr is", curr)

        if graph[curr[1]][curr[0]] == 1:
            for d in range(4):
                x2 = curr[0] + dx[d]
                y2 = curr[1] + dy[d]

                if 0 <= x2 < m and 0 <= y2 < n and graph[y2][x2] == 0:
                    queue.append([x2, y2, curr[2] + 1])
                    # print("append", x2, y2, "to queue")
                    graph[y2][x2] = 1
                    # print(graph)

    for li in graph:
        if 0 in li:
            return -1

    return curr[2]


for a in range(m):
    for b in range(n):
        if graph[b][a] == 1:
            queue.append([a, b, 0])

print(bfs())
