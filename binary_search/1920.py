import sys

input = sys.stdin.readline


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


n = int(input())
ns = sorted(list(map(int, input().split())))

m = int(input())
ms = list(map(int, input().split()))

for m in ms:
    if binary_search(ns, m):
        print(1)
    else:
        print(0)

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# ns = set(map(int, input().split()))  # Convert ns to a set for faster lookup
#
# m = int(input())
# ms = list(map(int, input().split()))
#
# result = []
#
# for m in ms:
#     if m in ns:  # Check if m exists in the set ns
#         result.append("1")
#     else:
#         result.append("0")
#
# for item in result:
#     print(item)
