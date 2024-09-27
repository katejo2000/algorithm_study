import sys
import heapq

input = sys.stdin.readline

queue = []
rooms = [0]

n = int(input())

for _ in range(n):
    start, end = map(int, input().split())
    queue.append((start, end))

queue.sort(key=lambda x: (x[0], x[1]))
# print(queue)

# 여기서!!! heapq를 쓰면 rooms 가 자동으로 우선순위 나열이 됨
for start, end in queue:
    # 가장 빠른 시간으로 강의실 예약하기
    if rooms[0] <= start:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    # 예약 가능 강의실이 없는 경우 추가하기
    else:
        heapq.heappush(rooms, end)

print(len(rooms))
