import sys

input = sys.stdin.readline

n, k = map(int, input().split())

count = 0
coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

while k > 0:
    for coin in coins:
        if coin <= k:
            count += k // coin
            k = k % coin

print(count)
