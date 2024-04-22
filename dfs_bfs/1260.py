import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    here, there = map(int, input().split())
    graph[here][there] = True
    graph[there][here] = True


def dfs(node):
    visited[node] = True

    print(node, end=' ')
    for j in range(1, n + 1):
        if not visited[j] and graph[node][j]:
            dfs(j)


def bfs(node):
    visited = [False] * (n + 1)
    queue = [node]
    visited[node] = True

    while queue:
        expand = queue.pop(0)
        print(expand, end=' ')
        for j in range(1, n + 1):
            if not visited[j] and graph[expand][j]:
                queue.append(j)
                visited[j] = True


dfs(v)
print('')
bfs(v)
