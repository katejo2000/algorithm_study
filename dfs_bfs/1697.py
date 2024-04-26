import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()


def bfs(node, end):
    queue.append(node)

    visited = [False] * 100001
    visited[node] = True

    time = [0] * 100001

    while queue:
        curr = queue.popleft()

        if curr == end:
            return time[curr]

        for next_node in (curr - 1, curr + 1, curr * 2):
            if 0 <= next_node <= 100000 and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                time[next_node] = time[curr] + 1


print(bfs(n, k))
