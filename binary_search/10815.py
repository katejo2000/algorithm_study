import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()  # Nlog(N)
m = int(input())
nums = deque(map(int, input().split()))

result = deque()

# print(n, m)
# print(cards)
# print(nums)

for num in nums:  # N
    # print("num :", num)
    start = 0
    end = len(cards) - 1  #

    found = False

    # Nlog(N)
    while start <= end:  #
        mid = (start + end) // 2
        # print("mid:", mid, "value:", cards[mid])

        if cards[mid] == num:
            # print("found")
            found = True
            break
        elif cards[mid] > num:
            # print("needs to be smaller:", cards[mid], ">", num)
            end = mid - 1
        else:
            # print("needs to be bigger:", cards[mid], "<", num)
            start = mid + 1

    if found:
        result += "1"
    else:
        result += "0"

for i in result:
    print(i, end=' ')