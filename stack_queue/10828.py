import sys
input = sys.stdin.readline

times = int(input())

numbs = []


def push(a):
    numbs.append(a)


def pop():
    if not numbs:
        print(-1)
    else:
        print(numbs.pop())


def size():
    print(len(numbs))


def empty():
    if not numbs:
        print(1)
    else:
        print(0)


def top():
    if not numbs:
        print(-1)
    else:
        print(numbs[-1])


for _ in range(times):
    words = input().split()
    if words[0] == "push":
        push(words[1])
    elif words[0] == "pop":
        pop()
    elif words[0] == "size":
        size()
    elif words[0] == "empty":
        empty()
    elif words[0] == "top":
        top()
