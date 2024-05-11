import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())

orders = list(map(int, input().split()))
targets = sorted(orders)
zero = [0] * len(targets)

# print(cards)
# print(targets)

result = dict(zip(targets, zero))
# print(result)

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

# cards 를 오름차순 정렬하면 이진탐색 가능
# 탐색은 오케이.. 그렇다면 결과는? map 을 쓰는게 빠를수도?
# key는 target 값, value는 나타난 만큼에 대해.


for card in cards:
    start = 0
    end = len(targets) - 1

    while start <= end:
        mid = (start + end) // 2

        # print(start, mid, end)
        # print("card, target", card, targets[mid])

        if card < targets[mid]:
            end = mid - 1
        elif card == targets[mid]:
            # print("match!", mid, targets[mid])
            value = result[targets[mid]]
            result[targets[mid]] = value + 1
            break
        else:
            start = mid + 1
    # print("no match :", start, end)

# print(result)

for order in orders:
    print(result[order], end=' ')


# from sys import stdin
# from collections import Counter
#
# # 입력
# _ = stdin.readline()
# N = stdin.readline().split()
# _ = stdin.readline()
# M = stdin.readline().split()
#
# # 카드 수 세기
# C = Counter(N)
#
# # 출력
# print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
# # 출처: https://develop247.tistory.com/352 [재냥이😻:티스토리]
