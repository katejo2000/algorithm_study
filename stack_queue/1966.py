import sys
from collections import deque

readline = sys.stdin.readline

times = readline()

for i in range(int(times)):
    count, index = map(int, input().split())  # ["4개", "2번째"]
    prior = list(map(int, input().split()))  # 중요도 : 1 2 3 4 높은게 빠름

    target = [prior[index], index]

    actual = deque()
    queue = deque()

    for j in range(len(prior)):
        queue.append([prior[j], j])  # 중요도, 순서

    while queue:
        big = 0
        for k in range(len(queue)):
            if big < queue[k][0]:
                big = queue[k][0]

        # print("big: ", big)

        curr = queue.popleft()

        if curr[0] < big:
            queue.append(curr)
        else:
            actual.append(curr)

    print(actual.index(target) + 1)
