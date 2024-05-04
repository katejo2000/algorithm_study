import sys

input = sys.stdin.readline

num = input().strip()
nums = []

for ch in num:
    nums.append(int(ch))

if 0 not in nums:
    print("-1")
elif sum(nums) % 3 != 0:
    print("-1")
else:
    nums.sort(reverse=True)
    for item in nums:
        print(item, end='')
