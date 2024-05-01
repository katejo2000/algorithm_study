import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

sum = 0

sum += nums[0] * (n - 1)

for i in range(1, n):
    sum += nums[i]

print(sum)
