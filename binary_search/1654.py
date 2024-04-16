from collections import deque
import sys

input = sys.stdin.readline

k, n = map(int, input().split())  # 가진거, 필요한거

ropes = deque()  # 모든 길이의 리스트

for _ in range(k):
    ropes.append(int(input()))

start = 1
end = max(ropes)

while start <= end:
    mid = (start + end) // 2
    added = 0

    for item in ropes:
        added += (item // mid)

    print(start, end, mid, "-", added)

    if added < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
