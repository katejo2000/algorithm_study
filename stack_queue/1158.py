from collections import deque
import sys

readline = sys.stdin.readline()

do = readline.split()

total = int(do[0])
k = int(do[1])

people = deque(range(1, total + 1))

print("<", end='')
while people:
    for i in range(k - 1):
        people.append(people.popleft())
    print(people.popleft(), end='')
    if len(people) > 0:
        print(", ", end='')

print(">")
