import sys

readline = sys.stdin.readline

count, length = map(int, readline().split())  # 나우의 수, 가져가려고 하는 길이

trees = list(map(int, readline().split()))  # 나무의 길이들

# trees.sort()  # quick sort

start = 0
end = max(trees)

while start <= end:
    added = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            added += tree - mid

    if added < length:
        end = mid - 1
    else:
        start = mid + 1

print(end)
