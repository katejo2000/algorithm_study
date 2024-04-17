import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

result = deque(map(int, input().split()))

sort = sorted(list(set(result)))

hashmap = {}
for i in range(len(sort)):
    hashmap[sort[i]] = i

for item in result:
    print(hashmap[item], end=' ')
