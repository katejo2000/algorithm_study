import sys

input = sys.stdin.readline

n = int(input())

queue = []
res = []

for _ in range(n):
    queue.append(int(input()))

# 0. 큐를 정렬한 다음에
# 1. 가장 작은 것 * 길이로 최대 중량 구하기
# 2. 그 다음 작은 것 * 줄어든 길이로 최대 중량 구하기
# 3. 반복해서 가장 큰 값 출력

queue.sort()

for i in range(len(queue)):
    # print(queue[i])
    res.append(queue[i] * (len(queue) - i))

# print(res)
print(max(res))
