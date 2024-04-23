n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, visited, house_count):
    visited[x][y] = True
    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if x2 <= -1 or x2 >= n or y2 <= -1 or y2 >= n:
            continue
        if not visited[x2][y2] and graph[x2][y2] == 1:
            house_count = dfs(x2, y2, visited, house_count + 1)

    return house_count


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j, visited, 1))

result.sort()

print(len(result))
for i in result:
    print(i)
