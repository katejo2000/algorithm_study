import sys

input = sys.stdin.readline

n = int(input())

queue = []
index = 0
count = 0

for _ in range(n):
    value = list(map(int, input().split()))
    queue.append(value)

queue.sort(key=lambda x: x[0])
queue.sort(key=lambda x: x[1])

for item in queue:
    if item[0] >= index:
        count += 1
        index = item[1]

print(count)
