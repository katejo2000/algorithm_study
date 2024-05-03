import sys

input = sys.stdin.readline

# 2 : 1
girl, boy, k = map(int, input().split())

team = 0

while girl >= 2 and boy >= 1 and girl + boy >= k + 3:
    print(girl, boy, girl + boy, k)
    girl -= 2
    boy -= 1
    team += 1

# while girl + boy < k:
#     girl += 2
#     boy += 1
#     team -= 1

print("final :", girl, boy, girl + boy, k)
print(team)
