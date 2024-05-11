import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    money = int(input())

    quarter = money // 25
    money %= 25

    dime = money // 10
    money %= 10

    nickel = money // 5
    money %= 5

    penny = money

    print(quarter, dime, nickel, penny)
