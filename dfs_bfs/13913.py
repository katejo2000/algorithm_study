import sys
from collections import deque

input = sys.stdin.readline

# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

n, k = map(int, input().split())

visited = [False] * 100001
time = [0] * 100001

queue = deque()
queue.append([n, deque([n])])


def bfs():
    while queue:
        node = queue.popleft()  # 5, [5]
        visited[node[0]] = True

        val = node[0]
        lst = node[1]

        if n > k:
            print(n - k)
            for i in range(n - k + 1):
                print(n - i, end=' ')
            return

        if val == k:
            print(time[val])
            for i in node[1]:
                print(i, end=' ')
            return

        for new in [val - 1, val + 1, val * 2]:
            if 0 <= new <= 100000 and not visited[new]:
                queue.append([new, lst + deque([new])])  # 여기서 시간초과?
                visited[new] = True
                time[new] = time[val] + 1


bfs()
