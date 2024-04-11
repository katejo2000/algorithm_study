import sys

readline = sys.stdin.readline

times = int(readline())

for i in range(times):
    string = list(readline().strip())

    if string[0] == ")" or string[-1] == "(" or (len(string) % 2 != 0):
        # print("start error")
        print("NO")
    else:
        count = 0
        while count < len(string) - 1:
            # print(count, len(string))
            # print(string)

            if string[count] + string[count + 1] == "()":
                string.pop(count)
                string.pop(count)
                # print('delete () at index', count)
                count = 0
            else:
                # print("not a match, move to next index")
                count += 1
        # print(string)
        if len(string) > 0:
            print("NO")
        else:
            print("YES")
