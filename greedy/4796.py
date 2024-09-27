import sys

input = sys.stdin.readline

days = []

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    times = v // p
    rem = v % p

    # l * times
    # rem 과 l 중 더 작은 수

    days.append(l * times + min(rem, l))

for i in range(len(days)):
    print("Case " + str(i + 1) + ": " + str(days[i]))
