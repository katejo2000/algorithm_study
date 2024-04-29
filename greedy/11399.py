from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

sum = 0

for j in range(1, n+1):
    sum += j * nums[j-1]

print(sum)
