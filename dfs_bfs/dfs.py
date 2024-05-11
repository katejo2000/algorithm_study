from collections import deque


def dfs(graph, start):
    visited = []
    need_visited = deque()
    need_visited.append(start)

    while need_visited:

        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited


def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
