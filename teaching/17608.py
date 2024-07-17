import sys

input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

tallest = 0
count = 0

while nums:
    num = nums.pop()
    if num > tallest:
        count += 1
        tallest = num

print(count)
