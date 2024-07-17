import sys

input = sys.stdin.readline

a, b = input().split()

a5, a6, b5, b6 = a, a, b, b

if "5" in a:
    a6 = a.replace("5", "6")

if "5" in b:
    b6 = b.replace("5", "6")

if "6" in a:
    a5 = a.replace("6", "5")

if "6" in b:
    b5 = b.replace("6", "5")

minAB = int(a5) + int(b5)
maxAB = int(a6) + int(b6)

print(minAB, maxAB)