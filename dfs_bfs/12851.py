import sys
from collections import deque

input = sys.stdin.readline

# 동생은 k, 수빈이는 n (0 ~ 100000)
# -1, +1, *2
# 가장 빠른 시간, 총 몇 가지?

# 1. 가장 빠른 시간으로 찾는 방법 구하기 - bfs, queue
# 2. 그 시간과 동일한 시간으로 답을 찾는 방법도 고려하기 - 도착시간은 똑같되, 방법이 다른 경우.
#   -> 이미 방문했어도 괜찮다고 해줘야되는데..

n, k = map(int, input().split())

queue = deque()
visited = [False] * 100001
time = [0] * 100001
count = 0
result = 0

queue.append(n)

while queue:
    node = queue.popleft()
    visited[node] = True
    print("took", time[node], "seconds to get to", node)

    if node == k:
        print("**found answer!**")
        print("time took:", time[node])
        result = time[node]
        count += 1
        continue  # 있어도 되고 없어도 되는데 있으면 시간이 단축됨

    # 범위를 넘지 않고, 탐색한 적 없는 경우 큐에 추가
    # 가본적이 있긴 하지만 이것 역시 최단거리인 경우?
    # -> 최단거리 시간과 비교했을 때 시간이 더 걸리지만 않으면 됨! 수업 시간에 배웠던거 생각하기..
    for new in [node - 1, node + 1, node * 2]:
        if 0 <= new <= 100000 and (not visited[new] or time[new] == time[node] + 1):
            queue.append(new)
            visited[new] = True
            time[new] = time[node] + 1

print(result)
print(count)
