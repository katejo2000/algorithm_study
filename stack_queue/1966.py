import sys
from collections import deque

readline = sys.stdin.readline

times = readline()

for i in range(int(times)):
    doc = input().split()  # ["4개", "2번째"]
    prior = input().split()  # 중요도 : 1 2 3 4 높은게 빠름

    target = [int(prior[int(doc[1])]), int(doc[1])]
    # print("target is ", target)

    actual = deque()
    queue = deque()

    for j in range(len(prior)):
        queue.append([int(prior[j]), j])  # 중요도, 순서

    # print(queue)  # [ [1, 0], [2, 1], [3, 2], [4, 3] ]

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

        # print("queue: ", queue)
        # print("actual: ", actual)

    # print("target :", target)
    print(actual.index(target) + 1)
