import sys

input = sys.stdin.readline

n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

# print(nums)

nums.sort()

for item in nums:
    print(item)