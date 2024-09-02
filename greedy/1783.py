import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# o A o o
# o o B o
# S o o o
# o o C o
# o D o o

# 세로가 1이면 이동이 불가. ⇒ 1
# 가로가 1이면 이동이 불가. ⇒ 1
# 세로가 2이면 ⇒ B, C로만 이동 가능
# 세로가 3 이상, 가로가 7 미만이면 ⇒ A, D 로 움직이기
# 가로가 7이상, 세로가 3이상 이면 ⇒ 4번 시행 이후, 가로가 (m-7) 인 경우에 대해 최대

def greedy(n, m):
    # 가로 세로 1이면 이동 불가
    if n == 1 or m == 1:
        return 1

    # 세로가 2이면 B, C로만 이동 가능
    elif n == 2:
        if m >= 7:
            return 4
        else:
            return (m + 1) // 2

    # 가로가 7 미만이면 A, D로 먼저 이동
    elif m < 7:
        if m == 2:
            return 2
        if m == 3:
            return 3
        if m >= 4:
            return 4

    # 가로 7 이상, 세로 3 이상이면 ABCD 이후, 가로가 (m-7) 인 경우에 대해 최대. => A, D 반복하기
    else:
        return m - 2


print(greedy(n, m))
