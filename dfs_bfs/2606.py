import sys
from collections import deque

input = sys.stdin.readline

comps = int(input())
graph = [[False] * (comps + 1) for _ in range(comps + 1)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())

    graph[y][x] = True
    graph[x][y] = True

visited = [False] * (comps + 1)


# queue = deque()
#
#
# def bfs(node):
#     queue.append(node)
#
#     while queue:
#         node = queue.popleft()
#         print("node is", node)
#         visited[node] = True
#
#         for i in range(comps - 1):
#             print("if graph[", node, "][", i, "] ->", graph[node][i], " and not visited[", i, "] ->", not visited[i])
#             if graph[node][i] and not visited[i]:
#                 print("add bfs(", i, ")")
#                 queue.append(i)


def dfs(node):
    visited[node] = True

    for i in range(1, comps+1):
        # print("if graph[", node, "][", i, "] ->", graph[node][i], " and not visited[", i, "] ->", not visited[i])
        if graph[node][i] and not visited[i]:
            # print("go dfs(", i, ")")
            dfs(i)


# print(graph)
dfs(1)
# print(visited)
count = 0

for item in visited:
    if item:
        count += 1

print(count - 1)
