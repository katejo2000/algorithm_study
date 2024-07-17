import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    sentence = list(input().split())
    print("Case #", end='')
    print(i+1, end='')
    print(": ", end='')
    while sentence:
        print(sentence.pop(), end=' ')
    print()