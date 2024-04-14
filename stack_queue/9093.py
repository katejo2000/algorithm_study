import sys

input = sys.stdin.readline

times = int(input())

for i in range(times):
    sentence = input().split()

    while sentence:
        word = sentence.pop(0)

        for j in range(len(word)):
            print(word[-1-j], end='')

        if sentence:
            print(" ", end='')
        else:
            print('')
