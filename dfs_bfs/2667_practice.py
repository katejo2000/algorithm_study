import sys

input = sys.stdin.readline

n = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    nums = input()  # 10101
    for j in range(n):
        graph[i][j + 1] = nums[j]

print(graph)

visited = [[False] * (n + 1) for _ in range(n + 1)]
village = 0
count = 0
house = []


def dfs(x, y):
    global visited, count

    # 탐색 시작
    if graph[x][y] and not visited[x][y]:
        visited[x][y] = True
        count += 1

        goto = connected(x, y)  # []
        for item in goto:
            dfs(item[0], item[1])

    # 끝났으면?
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] and not visited[a][b]:
                dfs(a, b)
                print(count)


def connected(x, y):
    global graph
    result = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for k in range(4):
        x2 = x + dx[k]
        y2 = y + dy[k]

        if 1 <= x2 <= n and 1 <= y2 <= n:
            result.append([x2, y2])

    return result


dfs(1, 1)
