import sys
from collections import deque

input = sys.stdin.readline

s = int(input())

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
# 2 ≤ S ≤ 1000

visited = [[False] * 2001 for _ in range(2001)]
queue = deque([[1, 0, 0]])

# 클립보드 저장은 무조건 처음에 일어나야 함.
# 붙여넣기 : 클립보드 만큼 더하기

# 개수, 클립보드, 시간
visited[1][0] = True


def bfs():
    while queue:
        count, cb, time = queue.popleft()
        # print(count, cb, time)

        if count == s:
            # print("**found**")
            print(time)
            return

        # 붙여넣기, 복사, 삭제
        if 2 <= (count + cb) <= 1000 and not visited[(count + cb)][cb]:
            queue.append([(count + cb), cb, (time + 1)])
            visited[(count + cb)][cb] = True
            # print(visited[(count + cb)][cb])

        if 1 <= count <= 1000 and not visited[(count * 2)][count]:
            queue.append([count, count, (time + 1)])
            # print(visited[(count * 2)][count])

        if 2 <= (count - 1) <= 1000 and not visited[(count - 1)][cb]:
            queue.append([(count - 1), cb, (time + 1)])
            visited[(count - 1)][cb] = True
            # print(visited[(count - 1)][cb])


bfs()

# N [정답]
# 217 [18]
# 325 [19]
# 497 [20]
# 505 [20]
# 553 [21]
# 651 [21]
# 687 [21]
# 973 [23]
# 975 [22]
# 994 [22]
